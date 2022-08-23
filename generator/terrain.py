import random
import enum

class TerrainTypes(enum.Enum):
    Plain = 1
    Scrub = 2
    Forest = 3
    ForestWithHills = 4
    Rough = 5
    Desert = 6
    Hills = 7
    HillsWithForest = 8
    Mountains = 9
    MountainsWithPass = 10
    Marsh = 11
    Pond = 12
    Depression = 13
    
def plain(d20_roll):
    if (d20_roll >= 1 and d20_roll <= 11):
        return TerrainTypes.Plain
    if (d20_roll == 12):
        return TerrainTypes.Scrub
    if (d20_roll == 13):
        return TerrainTypes.Forest
    if (d20_roll == 14):
        return TerrainTypes.Rough
    if (d20_roll == 15):
        return TerrainTypes.Desert
    if (d20_roll == 16):
        return TerrainTypes.Hills
    if (d20_roll == 17):
        return TerrainTypes.Mountains
    if (d20_roll == 18):
        return TerrainTypes.Marsh
    if (d20_roll == 19):
        return TerrainTypes.Pond
    if (d20_roll == 20):
        return TerrainTypes.Depression

def scrub(d20_roll):
    if (d20_roll >= 1 and d20_roll <= 3):
        return TerrainTypes.Plain
    if (d20_roll >= 4 and d20_roll <= 11):
        return TerrainTypes.Scrub
    if (d20_roll >= 12 and d20_roll <= 13):
        return TerrainTypes.Forest
    if (d20_roll == 14):
        return TerrainTypes.Rough
    if (d20_roll == 15):
        return TerrainTypes.Desert
    if (d20_roll == 16):
        return TerrainTypes.Hills
    if (d20_roll == 17):
        return TerrainTypes.Mountains
    if (d20_roll == 18):
        return TerrainTypes.Marsh
    if (d20_roll == 19):
        return TerrainTypes.Pond
    if (d20_roll == 20):
        return TerrainTypes.Depression

def forest(d20_roll):
    if (d20_roll == 1):
        return TerrainTypes.Plain
    if (d20_roll >= 2 and d20_roll <= 4):
        return TerrainTypes.Scrub
    if (d20_roll >= 5 and d20_roll <= 14):
        return TerrainTypes.Forest
    if (d20_roll == 15):
        return TerrainTypes.Rough
    if (d20_roll == 16):
        return TerrainTypes.Hills
    if (d20_roll == 17):
        return TerrainTypes.Mountains
    if (d20_roll == 18):
        return TerrainTypes.Marsh
    if (d20_roll == 19):
        return TerrainTypes.Pond
    if (d20_roll == 20):
        return TerrainTypes.Depression

def rough(d20_roll):
    if (d20_roll >= 1 and d20_roll <= 2):
        return TerrainTypes.Plain
    if (d20_roll >= 3 and d20_roll <= 4):
        return TerrainTypes.Scrub
    if (d20_roll == 5):
        return TerrainTypes.Forest
    if (d20_roll >= 6 and d20_roll <= 8):
        return TerrainTypes.Rough
    if (d20_roll >= 9 and d20_roll <= 10):
        return TerrainTypes.Desert
    if (d20_roll >= 11 and d20_roll <= 15):
        return TerrainTypes.Hills
    if (d20_roll >= 16 and d20_roll <= 17):
        return TerrainTypes.Mountains
    if (d20_roll == 18):
        return TerrainTypes.Marsh
    if (d20_roll == 19):
        return TerrainTypes.Pond
    if (d20_roll == 20):
        return TerrainTypes.Depression

def desert(d20_roll):
    if (d20_roll >= 1 and d20_roll <= 3):
        return TerrainTypes.Plain
    if (d20_roll >= 4 and d20_roll <= 5):
        return TerrainTypes.Scrub
    if (d20_roll >= 6 and d20_roll <= 8):
        return TerrainTypes.Rough
    if (d20_roll >= 9 and d20_roll <= 14):
        return TerrainTypes.Desert
    if (d20_roll == 15):
        return TerrainTypes.Hills
    if (d20_roll >= 16 and d20_roll <= 17):
        return TerrainTypes.Mountains
    if (d20_roll == 18):
        return TerrainTypes.Marsh
    if (d20_roll == 19):
        return TerrainTypes.Pond
    if (d20_roll == 20):
        return TerrainTypes.Depression

def hills(d20_roll):
    if (d20_roll == 1):
        return TerrainTypes.Plain
    if (d20_roll >= 2 and d20_roll <= 3):
        return TerrainTypes.Scrub
    if (d20_roll >= 4 and d20_roll <= 5):
        return TerrainTypes.Forest
    if (d20_roll >= 6 and d20_roll <= 7):
        return TerrainTypes.Rough
    if (d20_roll == 8):
        return TerrainTypes.Desert
    if (d20_roll >= 9 and d20_roll <= 14):
        return TerrainTypes.Hills
    if (d20_roll >= 15 and d20_roll <= 16):
        return TerrainTypes.Mountains
    if (d20_roll == 17):
        return TerrainTypes.Marsh
    if (d20_roll >= 18 and d20_roll <= 19):
        return TerrainTypes.Pond
    if (d20_roll == 20):
        return TerrainTypes.Depression

def mountains(d20_roll):
    if (d20_roll == 1):
        return TerrainTypes.Plain
    if (d20_roll == 2):
        return TerrainTypes.Scrub
    if (d20_roll == 3):
        return TerrainTypes.Forest
    if (d20_roll >= 4 and d20_roll <= 5):
        return TerrainTypes.Rough
    if (d20_roll == 6):
        return TerrainTypes.Desert
    if (d20_roll >= 7 and d20_roll <= 10):
        return TerrainTypes.Hills
    if (d20_roll >= 11 and d20_roll <= 18):
        return TerrainTypes.Mountains
    if (d20_roll >= 18 and d20_roll <= 19):
        return TerrainTypes.Pond
    if (d20_roll == 20):
        return TerrainTypes.Depression

def marsh(d20_roll):
    if (d20_roll >= 1 and d20_roll <= 2):
        return TerrainTypes.Plain
    if (d20_roll >= 3 and d20_roll <= 4):
        return TerrainTypes.Scrub
    if (d20_roll >= 5 and d20_roll <= 6):
        return TerrainTypes.Forest
    if (d20_roll == 7):
        return TerrainTypes.Rough
    if (d20_roll == 8):
        return TerrainTypes.Hills
    if (d20_roll >= 9 and d20_roll <= 15):
        return TerrainTypes.Marsh
    if (d20_roll >= 16 and d20_roll <= 19):
        return TerrainTypes.Pond
    if (d20_roll == 20):
        return TerrainTypes.Depression

def get_terrain(terrain, d20_roll):
    result = None
    if (terrain == TerrainTypes.Plain):
        result = plain(d20_roll)
    if (terrain == TerrainTypes.Scrub):
        result = scrub(d20_roll)
    if (terrain == TerrainTypes.Forest):
        result = forest(d20_roll)
    if (terrain == TerrainTypes.Rough):
        result = rough(d20_roll)
    if (terrain == TerrainTypes.Desert):
        result = desert(d20_roll)
    if (terrain == TerrainTypes.Hills):
        result = hills(d20_roll)
    if (terrain == TerrainTypes.Mountains):
        result = mountains(d20_roll)
    if (terrain == TerrainTypes.Marsh):
        result = marsh(d20_roll)
    if (result == TerrainTypes.Forest):
        d10_roll = random.randint(1, 10)
        if (d10_roll == 1):
            result = TerrainTypes.ForestWithHills
    if (result == TerrainTypes.Hills):
        d10_roll = random.randint(1, 10)
        if (d10_roll == 1):
            result = TerrainTypes.HillsWithForest
    if (result == TerrainTypes.Forest):
        another_d20_roll = random.randint(1, 20)
        if (another_d20_roll == 1):
            result = TerrainTypes.MountainsWithPass
    return result