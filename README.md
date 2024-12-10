# Scraping the NYC DOE's Galaxy Website
The code contained in this repository scrapes FY 2025 budgets for each of New York City's public K-12 schools. The website can be accessed here: https://www.nycenet.edu/offices/d_chanc_oper/budget/DBOR/galaxy/galaxyallocation/default.aspx

## Before scraping
- Download the School Year 2024-25 Final Enrollment Projects CSV file, which contains school codes that you'll need to complete the scrape. The CSV file can be downloaded here: https://infohub.nyced.org/reports/financial/financial-data-and-reports/sy-2024-25-final-enrollment-projections. Store it in the same folder as the Python file. I've called the folder on my PC "galaxy-allocations," for example.
- Clean up the CSV. In particular, you'll want to make sure that you've separated the district code from the school code in the DBN column. To do that, create a new column and use the =RIGHT function to select only the last 4 characters in the strings stored in the DBN column. (I've also added a cleaned Excel file, so this step is optional.)

## Process
Open the file in a text editor such as Visual Studio code, navigate to the folder where you've stored the project files, then run "python galaxy_scraper.py" in your terminal. It takes a little over an hour for the process to complete. 

### Step-by-step process
1. Import libraries
2. Open the enrollment file using pandas, create a new df
3. Loop through the enrollment df's "school_code" column, append the base URL and each code to an empty list
4. Loop through the school codes again, this time adding a counter so we don't get a timeout error.
5. Request each school's link
6. Grab the school name, category allocation and dollar amount of each category allocation
7. Write each to a CSV
