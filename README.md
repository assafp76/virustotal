# virustotal

get_scan_id - will get the last scan_id according to the web site name, need to extract the date time too.

get_response - will get the latest responce

get_results - will get the needed kpis

get_categories - will get the categories for each site.

all need to be run inside a loop for each site :
import csv
import requests
reader = csv.reader(open(r'C:\Users\user\Downloads\request1.csv'))
for row in reader:
    print(f'"{row[0]}"')
 
 
 and inserted into sqlite3 db
 
