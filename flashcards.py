# import the json module from python3
import json

# open the file and parse the JSON
with open('me-capitals.json', 'r') as f:
    data = json.load(f)

for i in data["cards"]:
    guess = input(i["q"] + " > ")

    if guess.lower() == i["a"].lower():
        print("Correct!")
    else:
        print("Incorrect! The correct answer was", i["a"])