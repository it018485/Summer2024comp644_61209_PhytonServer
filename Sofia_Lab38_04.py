 #Write the following Python dictionary to a JSON file:
import json

# Create the dictionary
CartoniDict = {'Batman': 'Bruce', 'WonderWoman': 'Diana', 'Superman': 'Clark'}

# Save the dictionary to a JSON file
with open('CartoniSofia.json', 'w') as json_file:
    json.dump(CartoniDict, json_file, indent=4)
