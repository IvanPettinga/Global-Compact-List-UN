import numpy as np
from bs4 import BeautifulSoup as bs
import requests as rs
import pandas as pd
import time as time
import os

result_location = input("Enter the results path: ")
page_results = []
company_list = []

#Receiving the number of entries to determine how many pages to scrape
webpage_respons_max_pages = rs.get('https://www.unglobalcompact.org/what-is-gc/participants')
content_max_pages = webpage_respons_max_pages.content
soup_max_pages = bs(content_max_pages, 'html.parser')
max_pages = soup_max_pages.find_all(attrs={'class':'results-count'}) 

for page in max_pages:
    page_number = page.get_text()

max_page_number = 2

#int(page_number[:6])/50

#iterating through the page numbers appending each table 
for page_number in range(1,int(max_page_number)):
    time.sleep(4)
    webpage_response = rs.get('https://www.unglobalcompact.org/what-is-gc/participants/search?page='+str(page_number)+'&search%5Bkeywords%5D=&search%5Bper_page%5D=50&search%5Bsort_direction%5D=asc&search%5Bsort_field%5D=&utf8=%E2%9C%93')
    webpage = webpage_response.content
    soup = bs(webpage, 'html.parser')
    names = soup.find_all(attrs={'class':'name'}) 
    
    for individual_name in names:
        company = individual_name.get_text()
        company_list.append(company)
    
    page_results.append(names)


dataframe = pd.DataFrame(company_list[1:], columns = ['Name'])
dataframe.to_csv(os.path.join(result_location, "Global_compact_list.csv"))
