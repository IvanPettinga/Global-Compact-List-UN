import os
from scripts.delisted_participants import scrape_delisted_participants
from scripts.listed_participants import scrape_listed_participants

result_location = result_location = input("Enter the results path: ")

print("Loading data from webpage, please wait")

listed_participants = scrape_listed_participants()
delisted_participants = scrape_delisted_participants()

listed_participants.to_csv(os.path.join(result_location, "Global_compact_listed.csv"))
delisted_participants.to_csv(os.path.join(result_location, "Global_compact_delisted.csv"))

print("Finished")