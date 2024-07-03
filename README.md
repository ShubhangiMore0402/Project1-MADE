# Exercise Badges

![](https://byob.yarr.is/ShubhangiMore0402/Project1-MADE/score_ex1) ![](https://byob.yarr.is/ShubhangiMore0402/Project1-MADE/score_ex2) ![](https://byob.yarr.is/ShubhangiMore0402/Project1-MADE/score_ex3) ![](https://byob.yarr.is/ShubhangiMore0402/Project1-MADE/score_ex4) ![](https://byob.yarr.is/ShubhangiMore0402/Project1-MADE/score_ex5)

# Methods of Advanced Data Engineering Template Project

This template project provides some structure for your open data project in the MADE module at FAU.
This repository contains (a) a data science project that is developed by the student over the course of the semester, and (b) the exercises that are submitted over the course of the semester.
Before you begin, make sure you have [Python](https://www.python.org/) and [Jayvee](https://github.com/jvalue/jayvee) installed. We will work with [Jupyter notebooks](https://jupyter.org/). The easiest way to do so is to set up [VSCode](https://code.visualstudio.com/) with the [Jupyter extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter).

To get started, please follow these steps:
1. Create your own fork of this repository. Feel free to rename the repository right after creation, before you let the teaching instructors know your repository URL. **Do not rename the repository during the semester**.
2. Setup the exercise feedback by changing the exercise badge sources in the `README.md` file following the patter `![](https://byob.yarr.is/<github-user-name>/<github-repo>/score_ex<exercise-number>)`. 
For example, if your user is _myuser_ and your repo is _myrepo_, then update the badge for _exercise 1_ to `![](https://byob.yarr.is/myrepo/myuser/score_ex1)`. Proceed with the remaining badges accordingly.


## Project Work
Your data engineering project will run alongside lectures during the semester. We will ask you to regularly submit project work as milestones so you can reasonably pace your work. All project work submissions **must** be placed in the `project` folder.

### Exporting a Jupyter Notebook
Jupyter Notebooks can be exported using `nbconvert` (`pip install nbconvert`). For example, to export the example notebook to html: `jupyter nbconvert --to html examples/final-report-example.ipynb --embed-images --output final-report.html`


## Exercises
During the semester you will need to complete exercises using [Jayvee](https://github.com/jvalue/jayvee). You **must** place your submission in the `exercises` folder in your repository and name them according to their number from one to five: `exercise<number from 1-5>.jv`.

In regular intervalls, exercises will be given as homework to complete during the semester. Details and deadlines will be discussed in the lecture, also see the [course schedule](https://made.uni1.de/). At the end of the semester, you will therefore have the following files in your repository:

1. `./exercises/exercise1.jv`
2. `./exercises/exercise2.jv`
3. `./exercises/exercise3.jv`
4. `./exercises/exercise4.jv`
5. `./exercises/exercise5.jv`

### Exercise Feedback
We provide automated exercise feedback using a GitHub action (that is defined in `.github/workflows/exercise-feedback.yml`). 

To view your exercise feedback, navigate to Actions -> Exercise Feedback in your repository.

The exercise feedback is executed whenever you make a change in files in the `exercise` folder and push your local changes to the repository on GitHub. To see the feedback, open the latest GitHub Action run, open the `exercise-feedback` job and `Exercise Feedback` step. You should see command line output that contains output like this:

```sh
Found exercises/exercise1.jv, executing model...
Found output file airports.sqlite, grading...
Grading Exercise 1
	Overall points 17 of 17
	---
	By category:
		Shape: 4 of 4
		Types: 13 of 13
```
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

## Data Pipeline
The data pipeline involves several steps:
1. **Data Ingestion**: Collecting raw data from multiple sources.
2. **Data Cleaning**: Removing duplicates, handling missing values, and normalizing data.
3. **Data Transformation**: Aggregating and calculating CO2 emissions per GDP and air travel emission intensity.
4. **Error Handling**: Implementing checks to manage changing input data and errors during processing.
5. **Data Loading**: Storing the processed data in a structured format for analysis.

## Testing
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
1. **CO2 Emissions per GDP by Region (2015-2016)**: A line plot showing trends over time.
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




