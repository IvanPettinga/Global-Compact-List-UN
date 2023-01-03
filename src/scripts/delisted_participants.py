from bs4 import BeautifulSoup as bs
import requests as rs
import pandas as pd
import time as time
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def scrape_delisted_participants ():
    company_list = []
    sector_list = []
    country_list = []
    year_list = []

    #Receiving the number of entries to determine how many pages to scrape
    webpage_respons_max_pages = rs.get('https://www.unglobalcompact.org/participation/report/cop/create-and-submit/expelled', verify= False)
    content_max_pages = webpage_respons_max_pages.content
    soup_max_pages = bs(content_max_pages, 'html.parser')
    max_pages = soup_max_pages.find_all('h2')

    first_string = max_pages[0].get_text()
    number_of_delisted_participants = int(first_string[-5:])

    max_page_number = number_of_delisted_participants/250

    #iterating through the page numbers appending each table 
    for page_number in range(1,int(max_page_number)):
        time.sleep(1)
        webpage_response = rs.get('https://www.unglobalcompact.org/participation/report/cop/create-and-submit/expelled?page='+str(page_number)+'1&per_page=250',verify= False)
        webpage = webpage_response.content
        soup = bs(webpage, 'html.parser')

        names = soup.find_all(attrs={'class':'participant'}) 
        sector = soup.find_all(attrs={'class':'sector'})
        country = soup.find_all(attrs={'class':'country'})
        year = soup.find_all(attrs={'class':'year'})
        
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
        
    #Save as a dataframe at file location
    dataframe_name = pd.DataFrame(company_list[1:], columns = ['Participant'])
    dataframe_country = pd.DataFrame(country_list[1:], columns = ['Country'])
    dataframe_year = pd.DataFrame(year_list[1:], columns = ['Expelled'])
    dataframe_sector = pd.DataFrame(sector_list[1:], columns = ['Sector'])

    delisted_concatenated_dataframes = pd.concat([dataframe_name, dataframe_sector,dataframe_country,dataframe_year], axis=1)

    return delisted_concatenated_dataframes



