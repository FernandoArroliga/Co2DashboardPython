# CO2 Emissions Dashboard

A Python dashboard built using `panel`, `hvplot`, `pandas`, `numpy`, and `jupyter-lab`, displaying visualizations and insights from a CO2 emissions dataset.

![PanelDashboard](panel_python_project.jpeg)

## Table of Contents

- [Introduction](#introduction)
- [Dataset](#Dataset)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Introduction

This project is a Python-based dashboard utilizing various powerful libraries to visualize and analyze CO2 emissions data. The following libraries have been utilized to create an interactive and informative dashboard:

- **Panel**: Panel is a high-level app and dashboarding solution for Python that allows developers to create interactive web apps and dashboards from various sources of data.

- **Hvplot**: Hvplot is a high-level plotting API built on top of Bokeh and Pandas that provides a quick and convenient way to generate interactive plots.

- **Pandas**: Pandas is a fast, powerful, and flexible open-source data analysis and manipulation tool built on top of the Python programming language. It is extensively used for data wrangling and analysis in this project.

- **NumPy**: NumPy is a fundamental package for scientific computing in Python, providing support for arrays, matrices, and a variety of mathematical functions to operate on these data structures.

- **Jupyter Lab**: Jupyter Lab is an open-source web application that allows users to create and share documents that contain live code, equations, visualizations, and narrative text. It is a great environment for interactive computing and supports Jupyter notebooks.

## Dataset

The dataset used for this project contains comprehensive data on CO2 emissions, population, GDP, and related metrics for different countries across various years. Here's a brief overview of the dataset columns related to CO2 emissions:

- **Country**: The name of the country.
- **Year**: The year for which the data is recorded.
- **Population**: The population of the country in that year.
- **CO2 Emissions (Total)**: Total CO2 emissions for that year in metric tons.
- **CO2 Emissions per Capita**: CO2 emissions per capita, representing the average emissions per person in metric tons.

The dataset offers valuable insights into the trends and patterns of CO2 emissions globally, allowing for in-depth analysis and visualization of the environmental impact of different countries over time.

For a more detailed understanding of the dataset and its structure, please refer to the dataset documentation.

For more information on CO2 emissions, you can visit reputable sources such as the [United Nations Framework Convention on Climate Change (UNFCCC)](https://unfccc.int/) and the [Environmental Protection Agency (EPA)](https://www.epa.gov/ghgemissions).

...


## Features

- Visualization of CO2 emissions data by country and year
- Interactive plots to explore trends and patterns
- Metrics and statistics on CO2 emissions
- ...

## Installation

To get started with the CO2 Emissions Dashboard, follow these steps:

1. **Clone the Repository:**

   First, clone this repository to your local machine using Git:

   ```bash
   git clone https://github.com/FernandoArroliga/Co2DashboardPython.git

2. **Create a Virtual Environment (Optional but Recommended):**

   It's a good practice to create a virtual environment for this project to manage dependencies. Using virtualenv:

   ```bash
   python -m venv env

3. **Activate the Virtual Environment:**
   Activate the virtual environment to isolate dependencies for this project:
   
- Windows:
   ```bash
   .\env\Scripts\activate

- Linux/macOS:
   ```bash
   source env/bin/activate

4. **Install Dependencies:**
   Use pip to install the necessary Python packages from the provided requirements file:
   ```bash
   pip install -r requirements.txt

5. **Launch JupyterLab:**
   Start the JupyterLab environment to run the dashboard application:
   ```bash
      jupyter-lab

6. **Open the Dashboard Notebook:**
   Within JupyterLab, navigate to the project directory and open the Jupyter notebook
   file Co2DashboardPython.ipynb. Run the notebook to interact with the CO2 Emissions Dashboard.

7. **Explore the Dashboard:**
   Interact with the dashboard to explore the CO2 emissions data, visualizations, and gain insights
   into the environmental impact across different countries and years.

   Feel free to modify the environment setup based on your preference or the specific requirements of your system.

## Usage

To use and run the CO2 Emissions Dashboard, follow these steps:

1. **Project Files Overview:**

   In the repository, you will find the following files:
   - `dashboard.py`: Contains the script to create and run the dashboard on the server.
   - `Co2DashboardPython.ipynb`: Jupyter notebook containing the dashboard script.
   - `cleaning_the_dataset.py`: Python script to clean the dataset.
   - `owid-co2-data.csv`: CO2 emissions dataset (raw data).
   - `cleaned_data.csv`: Cleaned dataset stored after running `cleaning_the_dataset.py`.

2. **Cleaning the Dataset:**

   Run the Python script `cleaning_the_dataset.py` to clean the raw dataset and generate the cleaned dataset file `cleaned_data.csv`:

   ```bash
   python cleaning_the_dataset.py

3. **Running the Dashboard:**
   To run the dashboard using Python, execute the dashboard.py script from the command line:
   ```bash
      python dashboard.py


## License

This project is licensed under the **MIT License**. 

The MIT License is a permissive open-source license that allows users to do almost anything they want with the project's code, provided they include the original copyright and license notice in any copy of the project. It's known for its simplicity and flexibility, making it a popular choice for many open-source projects.

### MIT License Summary

- **Permission**: Users can use, modify, copy, distribute, and sublicense the code with or without modifications.
- **Liability**: The code is provided "as is," without any warranty or liability.
- **Copyright Notice**: Users must include the original copyright and license notice in all copies or substantial portions of the project.

For more details, you can refer to the [MIT License](LICENSE) file.

Feel free to use and contribute to this project, following the terms of the MIT License.

