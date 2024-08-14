# CO2 Emissions and Air Travel Emission Intensity Analysis

This project analyzes CO2 emissions per GDP by region and air travel emission intensity in Europe. The analysis uses data from the Emissions Database for Global Atmospheric Research (EDGAR) and UDP - Air Travel Emission Intensity datasets.

## Project Overview

The goal of this project is to understand and compare the trends in CO2 emissions per GDP across different regions and air travel emission intensities in Europe. The analysis is performed using an automated data pipeline that processes, cleans, and transforms the data to generate meaningful insights.

## Data Sources

1. **EDGAR v4.3.2_FT_2016 (fossil CO2 and GHG time-series)**
   - Publisher: Joint Research Centre
   - URL: [EDGAR Dataset](https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/EDGAR/datasets/v432_FT2016/EDGARv432_FT2016_CO2_per_GDP_emissions_1970-2016.csv)

2. **UDP - Air Travel Emission Intensity**
   - Publisher: Joint Research Centre
   - URL: [UDP Dataset](https://urban.jrc.ec.europa.eu/api/udp/v2/en/data/?databrick_id=739&nutslevel=0&ts=TOURISM&nutsversion=-1&mpx=1&nutslevel=9&format=csv)

## Data Pipeline [here](https://github.com/ShubhangiMore0402/Project1-MADE/blob/main/project/auto_datapipeline.py)
The data pipeline involves several steps:
1. **Data Ingestion**: Collecting raw data from multiple sources.
2. **Data Cleaning**: Removing duplicates, handling missing values, and normalizing data.
3. **Data Transformation**: Aggregating and calculating CO2 emissions per GDP and air travel emission intensity.
4. **Error Handling**: Implementing checks to manage changing input data and errors during processing.
5. **Data Loading**: Storing the processed data in a structured format for analysis.

## Testing [here](https://github.com/ShubhangiMore0402/Project1-MADE/blob/main/project/automated_testing.py)
To ensure the reliability and accuracy of the data pipeline, the following testing strategies were implemented:
1. **Unit Tests**: Individual functions and components were tested to ensure they work as expected.
2. **Integration Tests**: The entire data pipeline was tested end-to-end to verify that all steps work together seamlessly.
3. **Validation Checks**: Various data validation checks were performed to ensure data quality and consistency.
4. **Error Handling**: Robust error handling mechanisms were put in place to manage and log any issues that arise during data processing.

## Analysis
### CO2 Emissions per GDP (2013-2016)
- **Method**: Filtered out countries with values above 300, selected the top 15 countries by CO2 emissions per GDP.
- **Results**: Identified leading countries with high CO2 emissions relative to their GDP.

### Air Travel Emission Intensity Trends (2019-2022)
- **Method**: Analyzed emission intensity trends for European regions by selecting top 15 regions, filtering out regions with values above 300.
- **Results**: Observed trends and fluctuations in air travel emissions over four years.

## Results and Visualizations
### Figures
1. **CO2 Emissions per GDP by Region (2013-2016)**: A line plot showing trends over time.
2. **Air Travel Emission Intensity Trends in Europe (2019-2022)**: A line plot showing trends over time.

## Conclusion
The analysis reveals significant insights into CO2 emissions and air travel emission intensities, highlighting key regions and countries contributing to global emissions. These findings can inform policy decisions and environmental strategies.

## How to Run the Project
1. **Clone the Repository**: `https://github.com/ShubhangiMore0402/Project1-MADE.git`
2. **Install Dependencies**: `pip install -r requirements.txt`
3. **Run the Data Pipeline**: `python data_pipeline.py`
4. **Run Tests**: `pytest tests/`

## License
This project is licensed under the [CC BY 4.0 License](LICENSE).




