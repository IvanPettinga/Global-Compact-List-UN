import os
from scripts.delisted_participants import scrape_delisted_participants
from scripts.listed_participants import scrape_listed_participants


url_active= 'https://unglobalcompact.org/what-is-gc/participants/search?utf8=%E2%9C%93&search%5Bkeywords%5D=&search%5Breporting_status%5D%5B%5D=active&search%5Bsort_field%5D=&search%5Bsort_direction%5D=asc&search%5Bper_page%5D=50'
url_non_communicating = 'https://unglobalcompact.org/what-is-gc/participants/search?utf8=%E2%9C%93&search%5Bkeywords%5D=&search%5Breporting_status%5D%5B%5D=noncommunicating&search%5Bsort_field%5D=&search%5Bsort_direction%5D=asc&search%5Bper_page%5D=50'
url_delisted= 'https://unglobalcompact.org/what-is-gc/participants/search?utf8=%E2%9C%93&search%5Bkeywords%5D=&search%5Breporting_status%5D%5B%5D=delisted&search%5Bsort_field%5D=&search%5Bsort_direction%5D=asc&search%5Bper_page%5D=50'

result_location = result_location = input("Enter the results path: ")

print("Loading data from webpage, please wait")

listed_participants = scrape_listed_participants()
delisted_participants = scrape_delisted_participants()

listed_participants.to_csv(os.path.join(result_location, "Global_compact_listed.csv"))
delisted_participants.to_csv(os.path.join(result_location, "Global_compact_delisted.csv"))

print("Finished")