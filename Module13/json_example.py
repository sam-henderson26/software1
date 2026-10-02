import json

save_data = {
    "player": "Sam",
    "level": "3",
    "items": ["axe", "gold", "wood"]
}

with open("Module13/savedata.json", "w") as file:
    json.dump(save_data, file)

#with open("Module13/savedata.json", "r") as file:
    #file_data = json.load(file)
#print(f"Player: {file_data["player"]}")
