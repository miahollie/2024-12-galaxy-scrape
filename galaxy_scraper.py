## import libraries
import csv
import requests
import pandas as pd
from bs4 import BeautifulSoup
from random import randrange
import time

## read in 2025 enrollment projections data, which stores school codes
enrollment = pd.read_excel("enrollment_2025.xlsx")

## assign column with the school codes to a new variable
school_codes = enrollment["school_code"]

## create an empty list
links = []

## append links to the empty list
for code in school_codes:
    base_url = "https://www.nycenet.edu/offices/d_chanc_oper/budget/dbor/galaxy/galaxyallocation/default.aspx?DDBSSS_INPUT="
    links.append(f"{base_url}{code}")

## create the rest of the empty lists we'll need
total_links = len(links)
broken_url = []
rows = []

## loop through the links first
for counter, code in enumerate(school_codes, start = 1):
    target_link = f"{base_url}{code}"
    print(f" Scraping {counter} of {total_links}: {code}: {target_link}")
    try:
         response = requests.get(target_link)
         soup = BeautifulSoup(response.text, "html.parser")
         tables = soup.find("span", id = "message")
         school_name = tables.find("h2", style="margin-bottom:0px;font-size:1.25em;padding-bottom:5px;").get_text()
         line_items = tables.find_all("tr")
         for item in line_items:
            try:
                data = item.get_text().split("$")
                categories = data[0]
                dollars = data[1]
                row = {'school_name': school_name, 'categories': categories, 'dollars': dollars}
                rows.append(row)
            except IndexError:
                dollars = 'null'
         with open ("galaxy_allocations_2025.csv", "w+") as csvfile: 
            fieldnames = ["school_name", "categories", "dollars"] 
            writer = csv.DictWriter(csvfile, fieldnames = fieldnames) 
            writer.writeheader() 
            for row in rows: 
                writer.writerow(row)
    except:
        print(f"{target_link} didn't work, appending to broken links list...")
        broken_url.append(target_link)
    finally:
        snooze = randrange(1,5)
        print(f"Snoozing for {snooze} seconds")
        time.sleep(snooze)

print(f"done scraping..")


