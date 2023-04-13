import os
import pandas as pd
from scripts.functions import check_url_status, get_entries

# Define URLs for the different participant statuses
urls = [
    'https://unglobalcompact.org/what-is-gc/participants/search?page=1&search%5Bkeywords%5D=&search%5Bper_page%5D=50&search%5Breporting_status%5D%5B%5D=active&search%5Bsort_direction%5D=asc&search%5Bsort_field%5D=&utf8=%E2%9C%93',
    'https://unglobalcompact.org/what-is-gc/participants/search?page=1&search%5Bkeywords%5D=&search%5Bper_page%5D=50&search%5Breporting_status%5D%5B%5D=noncommunicating&search%5Bsort_direction%5D=asc&search%5Bsort_field%5D=&utf8=%E2%9C%93',
    'https://unglobalcompact.org/what-is-gc/participants/search?page=1&search%5Bkeywords%5D=&search%5Breporting_status%5D%5B%5D=delisted&search%5Bsort_field%5D=&search%5Bsort_direction%5D=asc&search%5Bper_page%5D=50'
]

# Define a mapping of URLs to participant statuses
status_map = {
    urls[0]: 'active',
    urls[1]: 'non_communicating',
    urls[2]: 'delisted'
}

# Create an empty DataFrame to hold the participant data
global_compact_list = pd.DataFrame(columns=['Participant', 'Country', 'Year', 'Sector', 'Status'])

# Get the output directory from the user
result_location = input("Enter the output directory path: ")

# Scrape participant data for each status URL
for status_url in urls:
    # Check if the URL is accessible
    if check_url_status(status_url) == 'status: OK':
        # Scrape the participant data for this status
        status_entries = get_entries(status_url)
        # Add the participant status to the DataFrame
        status_entries['Status'] = status_map[status_url]
        # Concatenate the participant data for this status with the overall DataFrame
        global_compact_list = pd.concat([global_compact_list, status_entries])
    else:
        print("The website URL is not accessible")

# Save the participant data as an Excel file in the output directory
global_compact_list.to_excel(os.path.join(result_location, "Global Compact List.xlsx"), index=False)

print("Finished")
