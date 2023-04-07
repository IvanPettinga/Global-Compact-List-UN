from bs4 import BeautifulSoup as bs
import requests as rs
import pandas as pd
import urllib3
from http.client import responses


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

    for page in max_pages:
        page_number = page.get_text()

    max_page_number = int(page_number[:6])/50
    return max_page_number

