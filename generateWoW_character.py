import random
import pandas as pd

# defining dictionaries for character attributes
data_class = {'Class': ['Warrior', 'Hunter', 'Priest', 'Druid', 'Paladin', 'Warlock', 'Monk', 'Death Knight',
                        'Demon Hunter', 'Mage', 'Shaman', 'Evoker', 'Rogue']}

profession_role = {'Profession': ['Alchemy', 'Blacksmithing', 'Enchanting', 'Engineering', 'Inscription',
                                  'Jewelcrafting', 'Leatherworking', 'Tailoring']}

gathering_p = {'Gather_P': ['Mining', 'Herbalism', 'Skinning']}

# reading the csv file that was created on Excel
race = pd.read_csv('WoW Character roll.csv')

# setting up class restriction on race
race_class_restrictions = {
    'Demon Hunter': ['Human', 'Dwarf', 'Gnome', 'Orc', 'Troll', 'Dracthyr', 'Tauren', 'Undead', 'Vulpera', 'Draenei',
                     'Worgen', 'Pandaren', 'Goblin', 'Void Elf', 'Lightforged Draenei', 'Dark Iron Dwarf', 'Kul Tiran',
                     'Mechagnome', 'Nightborne', 'Highmountain Tauren', "Mag'har Orc", 'Zandalari Troll'],
    'Evoker': ['Human', 'Dwarf', 'Gnome', 'Orc', 'Troll', 'Draenei', 'Tauren', 'Undead', 'Vulpera', 'Night Elf',
               'Worgen', 'Pandaren', 'Goblin', 'Void Elf', 'Lightforged Draenei', 'Dark Iron Dwarf', 'Kul Tiran',
               'Mechagnome', 'Nightborne', 'Highmountain Tauren', "Mag'har Orc", 'Zandalari Troll', 'Blood Elf'],
    'Warrior': ['Dracthyr'],
    'Hunter': ['Dracthyr'],
    'Mage': ['Dracthyr'],
    'Rogue': ['Dracthyr'],
    'Priest': ['Dracthyr'],
    'Warlock': ['Dracthyr'],
    'Paladin': ['Gnome', 'Orc', 'Troll', 'Dracthyr', 'Undead', 'Vulpera', 'Night Elf', 'Worgen', 'Pandaren', 'Goblin',
                'Void Elf', 'Kul Tiran', 'Mechagnome', 'Nightborne', 'Highmountain Tauren', "Mag'har Orc"],
    'Druid': ['Human', 'Dwarf', 'Gnome', 'Orc', 'Troll', 'Dracthyr', 'Undead', 'Vulpera',
              'Pandaren', 'Goblin', 'Void Elf', 'Lightforged Draenei', 'Dark Iron Dwarf',
              'Mechagnome', 'Nightborne', "Mag'har Orc", 'Blood Elf'],
    'Shaman': ['Human', 'Dwarf', 'Gnome', 'Orc', 'Troll', 'Dracthyr', 'Tauren', 'Undead', 'Vulpera', 'Night Elf',
               'Worgen', 'Pandaren', 'Goblin', 'Void Elf', 'Lightforged Draenei', 'Dark Iron Dwarf', 'Kul Tiran',
               'Mechagnome', 'Nightborne', 'Highmountain Tauren', "Mag'har Orc", 'Zandalari Troll', 'Blood Elf'],
    'Monk': ['Dracthyr'],
    'Death Knight': ['Dracthyr']
}

# get the faction distribution
faction = race['Factions'].value_counts()
print(faction)

# randomly select a race to play
r1 = list(race['Race'])
random_race = random.choice(r1)

# get a random class but also check if the class is playable by that race
playable_classes = [c for c in data_class['Class'] if random_race not in race_class_restrictions.get(c, [])]
random_class = random.choice(playable_classes)

# get a random profession and gathering profession
random_profession = random.choice(list(profession_role['Profession']))
random_gath_p = random.choice(list(gathering_p['Gather_P']))


# look at what faction that race belong to
def factions(rand_race):
    race_faction = race.loc[race['Race'] == rand_race, 'Factions'].values[0]
    return race_faction


character = {
    'Faction': factions(random_race),
    'Race': random_race,
    'Class': random_class,
    'Profession': random_profession,
    'Gathering Profession': random_gath_p
}

print("\nCharacter Attributes: ")
for key, value in character.items(): print(f"{key}: {value}")
