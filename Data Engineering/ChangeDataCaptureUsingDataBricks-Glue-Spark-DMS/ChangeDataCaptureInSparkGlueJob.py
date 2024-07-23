'''


The code is a PySpark program designed to handle Change Data Capture (CDC) operations on data stored in Amazon S3. The program reads data from an S3 bucket, processes it based on the file name (initial load or updates), and then writes the processed data back to an S3 bucket. 


Here’s a detailed breakdown of what each part of the code is doing:
Argument Parsing:
Used getResolvedOptions from awsglue.utils to parse the S3 bucket and file path arguments.

SparkSession Initialization:
Initialized a SparkSession with the app name "CDC".

File Paths Construction:
Constructed the input and output file paths using f-strings for readability.

Initial Data Load:
If the file name contains "LOAD", read the CSV file, rename columns, and write it to the output path in S3.
Specified header=False when reading CSV to handle files without headers.

Update Handling:
Read the update CSV file and rename columns.
Read the existing data from the output path and rename columns.
Used .collect() to bring the update DataFrame to the driver node for processing row by row.
Extracted action, id, FullName, and City once per row to avoid repeated access.

Data Writing:
After processing, wrote the final DataFrame back to the specified output path in S3.
Specified header=True when writing CSV to include headers in the output file.
'''

from awsglue.utils import getResolvedOptions
import sys
from pyspark.sql.functions import when
from pyspark.sql import SparkSession

# Parse arguments passed to the script
args = getResolvedOptions(sys.argv, ['s3_target_path_key', 's3_target_path_bucket'])
bucket = args['s3_target_path_bucket']
fileName = args['s3_target_path_key']

print(bucket, fileName)

# Initialize a SparkSession
spark = SparkSession.builder.appName("ChangeDataCapture").getOrCreate()

# Construct the S3 file paths for input and output
inputFilePath = f"s3a://{bucket}/{fileName}"
finalFilePath = f"s3a://pyspark-cdc-output-file/output"

# Load initial data
if "LOAD" in fileName:
    # Read the CSV file from the specified S3 path
    fileload_df = spark.read.csv(inputFilePath, header=False)
    
    # Rename columns for consistency
    fileload_df = fileload_df.withColumnRenamed("_c0", "id") \
               .withColumnRenamed("_c1", "FullName") \
               .withColumnRenamed("_c2", "City")
    
    # Write the data back to the specified output path in S3
    fileload_df.write.mode("overwrite").csv(finalFilePath, header=True)
else:
    # Read the update CSV file from the specified S3 path
    update_df = spark.read.csv(inputFilePath, header=False)
    
    # Rename columns for consistency
    update_df = update_df.withColumnRenamed("_c0", "action") \
             .withColumnRenamed("_c1", "id") \
             .withColumnRenamed("_c2", "FullName") \
             .withColumnRenamed("_c3", "City")
    
    # Read the existing data from the output path in S3
    finalFileUpdate_df = spark.read.csv(finalFilePath, header=True)
    
    # Process each row in the update DataFrame
    update_df_local = update_df.collect()
    for row in update_df_local:
        action = row["action"]
        row_id = row["id"]
        full_name = row["FullName"]
        city = row["City"]
        
        if action == 'U':
            # Update existing rows
            finalFileUpdate_df = finalFileUpdate_df.withColumn("FullName", when(finalFileUpdate_df["id"] == row_id, full_name).otherwise(finalFileUpdate_df["FullName"]))
            finalFileUpdate_df = finalFileUpdate_df.withColumn("City", when(finalFileUpdate_df["id"] == row_id, city).otherwise(finalFileUpdate_df["City"]))
        
        elif action == 'I':
            # Insert new rows
            new_row = [(row_id, full_name, city)]
            columns = ['id', 'FullName', 'City']
            newdf = spark.createDataFrame(new_row, columns)
            finalFileUpdate_df = finalFileUpdate_df.union(newdf)
        
        elif action == 'D':
            # Delete rows
            finalFileUpdate_df = finalFileUpdate_df.filter(finalFileUpdate_df.id != row_id)
    
    # Write the final DataFrame back to the specified output path in S3
    finalFileUpdate_df.write.mode("overwrite").csv(finalFilePath, header=True)
