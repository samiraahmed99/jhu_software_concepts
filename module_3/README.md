## Name and JHED ID  
**Name:** Samira Ahmed  
**JHED ID:** CD02EC

---

## Module Info  
**Module:** EN.605.256 – Modern Software Concepts in Python  
**Assignment:** PostgreSQL + Flask Web App – GradCafe Admissions Analysis  
**Due Date:** June 08, 2025

---

## Project Overview

This project builds on prior work from Module 2, where data from [TheGradCafe](https://www.thegradcafe.com/survey/) was scraped and cleaned into a structured JSON format.

Here in Module 3, the goal was to:
1. Load that cleaned data into a PostgreSQL database using `psycopg2`
2. Write SQL queries to answer meaningful questions about graduate school admissions
3. Display the query results on a styled Flask webpage

---

## Setup Instructions
1. Clone this repository.
2. Open your terminal and navigate into the project folder: <br>
`cd jhu_software_concepts/module_3`
3. Create and activate a virtual environment, then install dependencies: <br>
`python -m venv venv` <br>
`source venv/bin/activate` <br>
`pip install -r requirements.txt` <br>
4. Install PostgreSQL (if not already installed) for macOS:: <br> 
`brew install postgresql` <br>
`brew services start postgresql` <br>
Ensure a database exists named `postgres` and a role exists matching your username (e.g., `samiraahmed`). <br>

## Copy JSON File from Module 2
1. Copy the JSON file into this module's directory with: <br>
`cp ../module_2/applicant_data.json .` <br>

## Data Pipeline
1. Run `load_data.py` <br>
This script:
+ Connects to your PostgreSQL database using psycopg2 
+ Creates a table named applicants
+ Loads all entries from applicant_data.json into the table
+ Run with:
  + `python load_data.py`

## Query Data 
1. Answered questions in a limitations.pdf where the analysis comes from `query_data.py` <br>
This script:
+ Connects to the PostgreSQL database
+ Runs a series of SQL queries to answer seven key questions (e.g., acceptance rates, average GPAs)
+ Outputs the answers to the console
+ Run with:
  + `python query_data.py`

## Create a Flask Web App
1. Create a Flask web app: `app.py` <br>
This script:
+ Connects to the database
+ Executes the same seven queries as `query_data.py`
+ Renders results in a modern, styled webpage (`templates`/`index.html`)
+ Start the app with:
  + `python app.py`
+ Then open your browser to:
  + http://localhost:8000

## SQL Questions Answered

**The site answers questions such as:**

1. How many entries were submitted for Fall 2025?
2. What percentage were from international students?
3. What were the average GPA, GRE, GRE V, and GRE AW?
4. What was the average GPA of American applicants?
5. What percent of Fall 2025 submissions were acceptances?
6. What was the average GPA of accepted students?
7. How many applicants applied to Johns Hopkins University for a Masters in Computer Science?
All queries are defined in `app.py` and reused in `query_data.py` and answers about inherent limitations are given
in a limitations.pdf.

## Credits
+ Data originally sourced from [TheGradCafe](https://www.thegradcafe.com/survey/)
+ Scraping logic developed in Module 2 using `scrape.py` and `clean.py`

