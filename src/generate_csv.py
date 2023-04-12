import os
import pandas as pd
from scripts.functions import check_url_status 
from scripts.functions import get_entries

active= 'https://unglobalcompact.org/what-is-gc/participants/search?page=1&search%5Bkeywords%5D=&search%5Bper_page%5D=50&search%5Breporting_status%5D%5B%5D=active&search%5Bsort_direction%5D=asc&search%5Bsort_field%5D=&utf8=%E2%9C%93'
non_communicating = 'https://unglobalcompact.org/what-is-gc/participants/search?page=1&search%5Bkeywords%5D=&search%5Bper_page%5D=50&search%5Breporting_status%5D%5B%5D=noncommunicating&search%5Bsort_direction%5D=asc&search%5Bsort_field%5D=&utf8=%E2%9C%93'
delisted = 'https://unglobalcompact.org/what-is-gc/participants/search?page=1&search%5Bkeywords%5D=&search%5Breporting_status%5D%5B%5D=delisted&search%5Bsort_field%5D=&search%5Bsort_direction%5D=asc&search%5Bper_page%5D=50'

print('Welcome to the webscraping model of the Global Compact List')
result_location = result_location = input("Enter the results path: ")
print("Loading data from webpage, please wait")

global_compact_list = pd.DataFrame(columns= ['Participant','Country','Year','Sector'])

urls = [active, non_communicating, delisted]

status_map = {urls[0]: 'active', urls[1]: 'non_communicating', urls[2]: 'delisted'}

for statusframe in urls:
    if check_url_status(statusframe) == 'status: OK':
        entries = get_entries(statusframe)
        entries['Status'] = status_map[statusframe]
        global_compact_list = pd.concat([global_compact_list, entries])
    else:
        print("The website URL is not accessible")

global_compact_list = global_compact_list.replace(',', '.', regex=True)
global_compact_list.to_csv(os.path.join(result_location, "Global Compact List.csv"), index=False)

print("Finished")