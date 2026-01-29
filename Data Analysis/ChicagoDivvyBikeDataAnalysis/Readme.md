# Divvy Bike Share Analysis 

## Project Overview

This project provides a comprehensive analysis of the Chicago Divvy bike share system using data from 2014-2016. The analysis includes:

- **Data Wrangling**: Cleaning, preprocessing, and feature engineering
- **Temporal Analysis**: Patterns by hour, day, month, and season
- **User Behavior Analysis**: Trip duration, user types, and usage patterns
- **Station Analysis**: Popular stations and capacity utilization
- **Socioeconomic Correlation**: Relationship between bike usage and demographic factors
- **Statistical Testing**: Hypothesis testing and correlation analysis


## Requirements

### Python Environment
```bash
Python 3.6+
```

### Required Libraries
```bash
pip install pandas numpy matplotlib seaborn scipy
```

## Usage

### Basic Usage

```python
from divvy_analysis_clean import DivvyAnalysis

# Initialize analyzer
analyzer = DivvyAnalysis()

# Load and prepare data
analyzer.load_and_prepare_data('path/to/your/divvy_data.csv')

# Generate full report with all visualizations
stats = analyzer.generate_full_report(output_dir='plots')

# Print summary statistics
print(f"Total trips analyzed: {stats['total_trips']:,}")
print(f"Date range: {stats['date_range']}")
print(f"Average trip duration: {stats['avg_trip_duration_min']:.1f} minutes")
```

### Individual Analyses

You can also run individual analysis components:

```python
# Generate only temporal patterns
analyzer.plot_temporal_patterns(output_dir='plots')

# Generate only user behavior analysis
analyzer.plot_user_behavior(output_dir='plots')

# Generate only heatmaps
analyzer.plot_heatmap_analysis(output_dir='plots')

# Generate only station analysis
analyzer.plot_top_stations(output_dir='plots', top_n=15)

# Get summary statistics only
stats = analyzer.generate_summary_statistics()
```

## Data Format

The script expects a CSV file with the following columns (minimum):

### Required Columns
- `trip_id`: Unique trip identifier
- `starttime`: Trip start timestamp (datetime)
- `stoptime`: Trip end timestamp (datetime)
- `tripduration`: Trip duration in seconds

### Optional Columns (for enhanced analysis)
- `from_station_id`, `from_station_name`: Start station information
- `to_station_id`, `to_station_name`: End station information
- `usertype`: User type (Subscriber/Casual)
- `gender`: User gender
- `birthyear`: User birth year
- `dpcapacity_start`, `dpcapacity_end`: Station capacities

## Key Features

### 1. Data Cleaning & Preparation
- Automatic datetime parsing
- Missing value handling
- Duplicate removal
- Data type conversion and validation
- Reversed timestamp correction

### 2. Feature Engineering
- Comprehensive temporal features (Year, Month, Day, Hour, etc.)
- Season classification
- Weekday/Weekend categorization
- Holiday identification
- Trip duration normalization

### 3. Visualizations

**Temporal Patterns** :
<img width="4771" height="3572" alt="temporal_patterns" src="https://github.com/user-attachments/assets/a4c55686-9f58-4cc8-85c5-05a035face9c" />

- Monthly trip distribution
- Hourly usage patterns
- Day of week analysis
- Seasonal distribution

**User Behavior** :
<img width="4771" height="3573" alt="user_behavior" src="https://github.com/user-attachments/assets/4fb2f605-5df2-4e17-aff3-31c2531d97d7" />

- Trip duration histogram
- User type breakdown
- Weekday vs Weekend patterns
- Gender distribution (if available)

**Heatmaps** :
<img width="5251" height="1772" alt="heatmap_analysis" src="https://github.com/user-attachments/assets/0baca5ca-b825-4e67-8c52-d0d3fdc65358" />

- Day of week vs Hour
- Month vs Day of week

**Station Analysis** :
<img width="4767" height="3565" alt="station_capacity_analysis" src="https://github.com/user-attachments/assets/9d2a4b78-ac65-4023-9c1c-a9928ad85780" />

- Top start stations
- Top end stations

### 4. Statistical Analysis

The code supports various statistical analyses:
- Descriptive statistics
- Hypothesis testing
- Correlation analysis
- Distribution fitting
<img width="5367" height="3539" alt="statistical_hypothesis_testing" src="https://github.com/user-attachments/assets/4bbce1a4-f105-4ff8-a71c-58f41956795a" />
<img width="5367" height="3538" alt="statistical_distribution_fitting" src="https://github.com/user-attachments/assets/11f42d05-d8d0-4034-9d96-8e375f3397dd" />
<img width="4409" height="3357" alt="statistical_descriptive_analysis" src="https://github.com/user-attachments/assets/9068286a-3b7e-4840-9e0a-672f11a4667e" />
<img width="5328" height="3540" alt="statistical_correlation_analysis" src="https://github.com/user-attachments/assets/aa420cd5-7f92-41c2-879d-c9bca080c93f" />

## Output

The `generate_full_report()` function creates:

1. **Four visualization files** (PNG format, 300 DPI):
   - `temporal_patterns.png`
   - `user_behavior.png`
   - `heatmap_analysis.png`
   - `top_stations.png`

2. **Summary statistics dictionary** with:
   - Total trip count
   - Date range
   - Average and median trip duration
   - User type distribution
   - Peak usage times
   - Most popular stations

## Key Findings Summary

### Temporal Patterns
- **Seasonal**: Summer accounts for ~45% of annual trips
- **Daily**: Peak hours at 7-9 AM and 4-7 PM (commuter pattern)
- **Weekly**: Higher weekday usage, especially Wed-Thu

### User Behavior
- **Duration**: Median trip ~10-12 minutes
- **User Types**: 75-80% subscribers, 20-25% casual
- **Patterns**: Subscribers = commuters, Casual = recreational

### Recommendations
1. **Capacity Management**: Focus on top 20 stations during peak hours
2. **Seasonal Planning**: Prepare for 5x winter-to-summer increase
3. **Service Optimization**: Different strategies for commuters vs recreational users
4. **Expansion**: Target high-density, educated, higher-income areas

## Advanced Customization

### Modify Color Schemes
```python
import seaborn as sns
sns.set_palette("your_palette_name")
```

### Change Figure Sizes
```python
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (16, 8)  # width, height in inches
```

### Add Custom Analyses
The `DivvyAnalysis` class is designed to be extensible. Add your own methods:

```python
class ExtendedDivvyAnalysis(DivvyAnalysis):
    def custom_analysis(self):
        # Your custom analysis here
        pass
```

## Troubleshooting

### Common Issues

**Issue**: Memory error when loading large datasets
**Solution**: Use `pd.read_csv()` with `chunksize` parameter for iterative processing

**Issue**: Missing visualizations
**Solution**: Ensure output directory exists and has write permissions

**Issue**: Date parsing errors
**Solution**: Check date format in CSV, may need to specify format in `pd.read_csv()`

## Citation

If you use this analysis in your work, please cite:
```
Chicago Divvy Bike Share Analysis (2014-2016)
Comprehensive Data Analysis & Visualization Report
Analysis Period: 2014-2016
```

## License

This analysis code is provided for educational and research purposes.
