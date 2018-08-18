import json
import random

json_file = open("factory-sets.json", "r")
json_string = json_file.read()
json_file.close()

pokemon_format_file = open("showdown_format.txt", "r")
pokemon_format_string = pokemon_format_file.read()
pokemon_format_file.close()

all_sets = json.loads(json_string)
potential_formats = all_sets.keys()

def get_mon(pokedict):
    set = pokedict

    pokemon = set["species"]
    item = random.choice(set["item"])
    ability = random.choice(set["ability"])
    nature = set["nature"]

    move1 = random.choice(set["moves"][0])
    try:
        move2 = random.choice(set["moves"][1])
        move3 = random.choice(set["moves"][2])
        move4 = random.choice(set["moves"][3])
    except IndexError:
        #this error most likely occurs when ditto is called, as there is only one possible move for it
        #will investigate this bug further
        print("\n PROBLEM. HERE IS THE MON:\n" + pokemon)
        move2 = ""
        move3 = ""
        move4 = ""

    EVS = set["evs"]

    stats = {"hp" : 0, "atk" : 0, "spa" : 0, "def" : 0, "spa" : 0, "spd" : 0, "spe" : 0}

    for key in EVS.keys():
        stats[key] = EVS[key]

    return pokemon_format_string.format(
        pokemon = pokemon,
        item = item,
        ability = ability,
        nature = nature,
        move1 = move1,
        move2 = move2,
        move3 = move3,
        move4 = move4,
        **stats
    )

def get_team(format):
    if format not in potential_formats:
        raise KeyError("Format not supported!")

    output = ""
    hasmega = False
    team = {}
    count = 0

    while count < 6:
        pokemon_to_add = random.choice(list(all_sets[format].keys()))
        isInTeam = False
        for xmon in team.keys():
            if pokemon_to_add in xmon:
                isInTeam = True
                break
            elif "arceus" in pokemon_to_add:
                if pokemon_to_add[:5] in xmon:
                    isInTeam = True
                    break

        if isInTeam == False:
            pokemon_set_to_add = random.choice(all_sets[format][pokemon_to_add]["sets"])

            #check if holding mega stone
            if pokemon_set_to_add["item"][0].startswith(pokemon_set_to_add["species"][0:3]):
                if hasmega == False:
                    team[pokemon_to_add] = pokemon_set_to_add
                    hasmega = True
                    count +=1
            else:
                team[pokemon_to_add] = pokemon_set_to_add
                count +=1

    for mon in team:
        output += get_mon(team[mon]) + "\n"
    return output
