from bs4 import BeautifulSoup as bs
import requests as rs
import pandas as pd
import urllib3
from http.client import responses
import time as time

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def check_url_status(url):
    try:
        response = rs.head(url, verify=False)
        response.raise_for_status()
        return "status: OK"
    except Exception as e:
        return str(e)

def get_parameters (url):
    #make request and get content
    webpage_respons_max_pages = rs.get(url, verify= False)
    content = webpage_respons_max_pages.content

    #parse with beautifulsoup 
    soup = bs(content, 'html.parser')
              
    #get max number of pages and search options
    max_pages = soup.find_all(attrs={'class':'results-count'})
    max_searches = soup.find_all(attrs={'id':'search_per_page'})
    
    for search in max_searches:
        max_searches = search.get_text()

    for page in max_pages:
        page_number = page.get_text()

    number_of_options_searches = int(''.join([n for n in max_searches if n.isdigit()][-2:]))
    number_of_entries = int(''.join([n for n in page_number if n.isdigit()]))
    number_of_requests = (round(number_of_entries/number_of_options_searches))

    return number_of_requests

def get_entries (url):
    requests = get_parameters(url) + 1
    
    company_list = []
    sector_list = []
    country_list = []
    year_list = []

    for page_number in range(1,int(3)): #requests
        time.sleep(1)
        page_string = 'search?page=1'
        replacement = 'search?page=' + str(page_number)
        url_for_current_page = url.replace(page_string, replacement)
        print(str(page_number) + ' of the ' + str(requests) + ' requests completed')
        webpage_response = rs.get(url_for_current_page)
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

    data = {
        "Participant": company_list[1:],
        "Country": country_list[1:],
        "Year": year_list[1:],
        "Sector": sector_list[1:],
    }

    df = pd.DataFrame(data)
    return df