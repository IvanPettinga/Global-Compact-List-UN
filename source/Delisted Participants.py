import numpy as np
from bs4 import BeautifulSoup as bs
import requests as rs
import pandas as pd
import time as time
import os


result_location = result_location = input("Enter the results path: ")
print("Loading data from webpage, please wait")
page_results = []
company_list = []
page_numbers = []

#Receiving the number of entries to determine how many pages to scrape
webpage_respons_max_pages = rs.get('https://www.unglobalcompact.org/participation/report/cop/create-and-submit/expelled')
content_max_pages = webpage_respons_max_pages.content
soup_max_pages = bs(content_max_pages, 'html.parser')
max_pages = soup_max_pages.find_all('h2')

first_string = max_pages[0].get_text()
number_of_delisted_participants = int(first_string[-5:])

max_page_number = number_of_delisted_participants/250

#iterating through the page numbers appending each table 


for page_number in range(1,int(max_page_number)):
    time.sleep(4)
    webpage_response = rs.get('https://www.unglobalcompact.org/participation/report/cop/create-and-submit/expelled?page='+str(page_number)+'1&per_page=250')
    webpage = webpage_response.content
    soup = bs(webpage, 'html.parser')
    names = soup.find_all(attrs={'class':'name'}) 
    
    for individual_name in names:
        company = individual_name.get_text()
        company_list.append(company)
    
    page_results.append(names)


dataframe = pd.DataFrame(company_list[1:], columns = ['Name'])
dataframe.to_csv(os.path.join(result_location, "Global_compact_delisted.csv"))
print("Finished")

