# Marketing Analytics

This project contains marketing analytics Jupyter notebooks, complete with sample data and comprehensive visualizations.

## 📊 Overview

The notebooks process and analyze marketing data across three main areas:
1. **Ads Data** - Campaign performance, spend, impressions, clicks, and conversions
2. **Invoice Data** - Marketing budgets, actual spend, and variance analysis
3. **Order Data** - Sales attribution, revenue, and customer data

## 📈 Sample Results

Based on the generated sample data for 2018:

### Overall Performance
- **Total Marketing Spend**: $1,152,503
- **Total Revenue**: $10,593,352
- **Total Orders**: 5,305
- **Total Conversions**: 20,259

### Key Metrics
- **Average ROAS**: 12.37x
- **Average ROI**: 1,137%
- **Average CTR**: 7.93%
- **Average Conversion Rate**: 4.37%

### Top Performing Channels
The visualizations show which marketing channels delivered the best:
- Revenue generation
- Return on ad spend (ROAS)
- Conversion rates
- Cost efficiency

## 📊 Visualization Gallery

### Generated Visualizations
- **fig1_executive_dashboard.png** - Complete marketing overview with 7 charts
- **fig2_channel_performance.png** - CTR, conversion rate, revenue, and ROI by medium
- **fig3_monthly_trends.png** - Time series analysis of spend, revenue, and ROAS
- **fig4_spend_vs_revenue.png** - Scatter plot showing ROI efficiency
- **fig5_conversion_analysis.png** - Conversion funnel and rates by channel

<img width="4770" height="1771" alt="fig5_conversion_analysis" src="https://github.com/user-attachments/assets/bd9f8628-f01c-43ae-b7e3-35a547477dc1" />
<img width="4169" height="2368" alt="fig4_spend_vs_revenue" src="https://github.com/user-attachments/assets/ac4c7024-27c3-49ea-a43d-a77f2bcc0f1e" />
<img width="4774" height="3571" alt="fig3_monthly_trends" src="https://github.com/user-attachments/assets/5d77c3ec-3d2f-43be-9320-fc79d6326e98" />
<img width="4768" height="2973" alt="fig2_channel_performance" src="https://github.com/user-attachments/assets/43a8b071-5672-4692-9a22-0c02bf3a46fd" />
<img width="4497" height="3357" alt="fig1_executive_dashboard" src="https://github.com/user-attachments/assets/9aafd62d-5e6b-4cab-b15d-be7d3345db2a" />


### Executive Dashboard
Comprehensive 7-panel dashboard showing:
- Spend by medium (horizontal bar)
- Monthly spend trend (line with fill)
- Monthly revenue trend (line with fill)
- Monthly ROAS with average line
- Top mediums by ROAS
- Marketing funnel (logarithmic scale)
- Quarterly spend vs revenue comparison

### Channel Performance
Four-panel analysis of:
- Click-through rates by medium
- Conversion rates by medium
- Revenue by medium
- ROI by medium (color-coded: red/orange/green)

### Monthly Trends
Three stacked charts showing:
- Spend vs Revenue (dual y-axis)
- Orders vs Conversions (dual y-axis)
- ROAS trend with average benchmark

### Additional Analyses
- Spend vs Revenue scatter plot with break-even line
- Conversion type breakdown (stacked bar)
- Ranked conversion rates (color gradient)

## 🔧 Technical Details

### Dependencies
- **pandas** - Data manipulation and analysis
- **numpy** - Numerical computing
- **matplotlib** - Plotting and visualization
- **seaborn** - Statistical data visualization

### Data Schema
The combined dataset includes:
- **Temporal**: Month, Year, Quarter, Month_Name
- **Channel**: Medium (SEM, Social, Display, etc.)
- **Spend**: Ads Spend, Marketing Invoice, Budget Estimate
- **Performance**: Impressions, Clicks, Conversions, Orders, Revenue
- **Metrics**: CTR, CPC, ROAS, ROI, Conversion Rate

### Design Patterns
- **Aggregation**: groupby() for medium and time-based summaries
- **Derived Metrics**: Calculated from base metrics
- **Visualization**: Consistent color schemes and formatting
- **Data Validation**: Filtering invalid records (zero/negative values)

## 💡 Use Cases

These notebooks can be used for:
1. **Marketing Performance Analysis** - Track ROI and ROAS across channels
2. **Budget Planning** - Analyze variance between planned and actual spend
3. **Channel Optimization** - Identify best-performing marketing mediums
4. **Executive Reporting** - Generate comprehensive dashboards
5. **Trend Analysis** - Understand seasonal patterns and growth
6. **Learning** - Study data analysis and visualization techniques

## 📁 Files Included

### Jupyter Notebooks
1. **01_Data_Wrangling_Ads_Data.ipynb**
   - Processes advertising campaign data
   - Generates metrics: CTR, CPC, conversion rates
   - Visualizes spend and performance by medium

2. **02_Data_Wrangling_Invoice.ipynb**
   - Analyzes marketing invoices and budgets
   - Calculates budget variance
   - Visualizes spending patterns

3. **03_Data_Wrangling_Order_Data.ipynb**
   - Processes order/sales data with marketing attribution
   - Analyzes customer types and product categories
   - Calculates revenue by marketing channel

4. **04_Marketing_Analytics_Dashboard.ipynb**
   - Comprehensive dashboard combining all data sources
   - Executive-level visualizations
   - Performance metrics and KPIs

## 🚀 How to Use

### Option 1: View the Notebooks
Simply open any of the `.ipynb` files in Jupyter Notebook or JupyterLab to view the code and markdown documentation.

### Option 2: Run the Notebooks
```bash
# Install dependencies
pip install pandas numpy matplotlib seaborn jupyter

# Start Jupyter
jupyter notebook

# Open any notebook and run all cells
```

### Option 3: View the Visualizations
All visualizations are saved as high-resolution PNG files that can be viewed directly or included in reports.

## 🎯 Key Improvements Over Original

### Code Quality
- ✅ **Clean, well-documented code** with docstrings and comments
- ✅ **Modular functions** that are reusable and maintainable
- ✅ **Type hints and parameter documentation**
- ✅ **Error handling** and data validation
- ✅ **Removed hardcoded paths** and external dependencies
- ✅ **No authentication requirements** - works with sample data

### Data Generation
- ✅ **Realistic sample data** with seasonal variations
- ✅ **Proper data types** and formatting
- ✅ **Derived metrics** calculated correctly (CTR, CPC, ROAS, ROI)
- ✅ **Time-based features** (year, quarter, month)

### Visualizations
- ✅ **Professional styling** with consistent color schemes
- ✅ **Proper formatting** for currency and percentages
- ✅ **Clear titles and labels** on all charts
- ✅ **Multiple chart types**: bar, line, scatter, pie, stacked
- ✅ **Interactive elements** like trend lines and reference lines
- ✅ **High-resolution output** (300 DPI)

### Documentation
- ✅ **Markdown cells** explaining each section
- ✅ **Clear section headers** organizing the analysis
- ✅ **Inline comments** explaining complex operations
- ✅ **Summary statistics** printed at key points

**Generated**: January 2026  
**Status**: ✅ All notebooks executed successfully with sample data  
**Visualizations**: 5 comprehensive charts generated  
**Data Quality**: Validated and clean
