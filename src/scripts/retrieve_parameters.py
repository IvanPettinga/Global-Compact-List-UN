from bs4 import BeautifulSoup as bs
import requests as rs
import pandas as pd
import urllib3
from http.client import responses
import time as time


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def check_url_status (url):
    http = urllib3.PoolManager()
    status_code_active = http.request('GET', url)
    http_status = status_code_active.status
    return 'status: ' + responses[http_status]

def get_parameters (url):
    webpage_respons_max_pages = rs.get(url, verify= False)
    content_max_pages = webpage_respons_max_pages.content
    soup_max_pages = bs(content_max_pages, 'html.parser')
    max_pages = soup_max_pages.find_all(attrs={'class':'results-count'})
    max_searches = soup_max_pages.find_all(attrs={'id':'search_per_page'})
    
    for search in max_searches:
        max_searches = search.get_text()

    for page in max_pages:
        page_number = page.get_text()

    number_of_options_searches = ''.join([n for n in max_searches if n.isdigit()][-2:])
    number_of_entries = int(''.join([n for n in page_number if n.isdigit()]))
    number_of_requests = (round(number_of_entries/number_of_options_searches))

    return number_of_requests

def get_entries (url):
    requests = get_parameters(url)
    
    company_list = []
    sector_list = []
    country_list = []
    year_list = []

    for page_number in range(1,int(requests)):
        time.sleep(1)
        webpage_response = rs.get()
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
    


