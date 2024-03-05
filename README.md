# Submission

Here's my submission to Dicoding's course (Belajar Analisis Data dengan Python/Learn Data Analysis with Python) final project.

Dataset used: [Bike Sharing Dataset](https://drive.google.com/file/d/1RaBmV6Q6FYWU4HWZs80Suqd7KQC34diQ/view) ([Source](https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset)). I use the day.csv for the daily data, not the hourly data. The dataset is also available on this repository (Bike-sharing-dataset).

## What's within this repository
1. `/data` Directory, includes the dataset used for the analysis
2. `/dashboard` Directory, includes the `dashboard.py` file to be ran with `streamlit`
3. `CompleteAnalysisData`, the notebook file used to work with the raw data, analyse, and processing the data.
4. `requirement.txt`, contains the required libraries to work with the notebook and dashboard file.

## Quick Overview
This project analyses the daily number of bike rents around Portugal. The data will be checked for duplicates and missing values, then rename some of the headers and change discrete values into readable string, and then analysed. The whole process are also within the markdown inside the notebook file.

## Setup the environment
1. Create a virtual environment
2. Type:
```pip install numpy pandas scipy matplotlib seaborn jupyter streamlit```

## To run the streamlit
```streamlit run .\dashboard.py```
You can also check the dashboard [Here](https://sijesimochi.streamlit.app) without needing to download the whole zip.