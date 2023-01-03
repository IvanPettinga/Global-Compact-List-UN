from bs4 import BeautifulSoup as bs
import requests as rs
import pandas as pd
import time as time
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def scrape_listed_participants ():
    company_list = []
    sector_list = []
    country_list = []
    year_list = []

    #Receiving the number of entries to determine how many pages to scrape
    webpage_respons_max_pages = rs.get('https://www.unglobalcompact.org/what-is-gc/participants')
    content_max_pages = webpage_respons_max_pages.content
    soup_max_pages = bs(content_max_pages, 'html.parser')
    max_pages = soup_max_pages.find_all(attrs={'class':'results-count'}) 

    for page in max_pages:
        page_number = page.get_text()

    max_page_number = int(page_number[:6])/50

    #iterating through the page numbers appending each table 
    for page_number in range(1,int(max_page_number)):
        time.sleep(1)
        webpage_response = rs.get('https://www.unglobalcompact.org/what-is-gc/participants/search?page='+str(page_number)+'&search%5Bkeywords%5D=&search%5Bper_page%5D=50&search%5Bsort_direction%5D=asc&search%5Bsort_field%5D=&utf8=%E2%9C%93')
        webpage = webpage_response.content
        soup = bs(webpage, 'html.parser')

        names = soup.find_all(attrs={'class':'name'}) 
        sector = soup.find_all(attrs={'class':'sector'})
        country = soup.find_all(attrs={'class':'country'})
        year = soup.find_all(attrs={'class':'joined-on'})
    
    for individual_name in names:
        company = individual_name.get_text(strip = True)
        company_list.append(company)

    for individual_sector in sector:
        sector_company = individual_sector.get_text(strip = True)
        sector_list.append(sector_company)

    for individual_country in country:
            country_company = individual_country.get_text(strip = True)
            country_list.append(country_company)
        
    for individual_year in year:
        year_company = individual_year.get_text(strip = True)
        year_list.append(year_company)
    

    dataframe_name = pd.DataFrame(company_list[1:], columns = ['Participant'])
    dataframe_country = pd.DataFrame(country_list[1:], columns = ['Country'])
    dataframe_year = pd.DataFrame(year_list[1:], columns = ['Expelled'])
    dataframe_sector = pd.DataFrame(sector_list[1:], columns = ['Sector'])

    listed_concatenated_dataframes = pd.concat([dataframe_name, dataframe_sector,dataframe_country,dataframe_year], axis=1)

    return listed_concatenated_dataframes



