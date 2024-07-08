 #Write the following Python dictionary to a JSON file:
import json

# My new line for the dictionary
CartoniDict = {'Alabarda Spaziale': 'Sofia'}

# I read the file and put the content into allData variable
with open('CartoniSofia.json', 'r') as json_file:
    allData = json.load(json_file)
print(allData)
allData = allData | CartoniDict

# I open the file in W and I add all.
with open('CartoniSofia.json', 'w') as json_file:
    json.dump(allData, json_file, indent=4)
print(allData)