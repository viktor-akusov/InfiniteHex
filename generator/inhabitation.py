import random
import enum

class InhabitationTypes(enum.Enum):
    SingleDwelling = 1
    Thorp = 2
    Hamlet = 3
    Village = 4
    Town = 5
    City = 11
    Castle = 12
    RuinsVillage = 13
    RuinsCity = 14
    RuinsShrine = 15
    RuinsTomb = 16
    Uninhabited = 17

def get_inhabitation(d100_roll):
    if(d100_roll >= 1 and d100_roll <= 3):
        return InhabitationTypes.SingleDwelling
    if(d100_roll >= 4 and d100_roll <= 5):
        return InhabitationTypes.Thorp
    if(d100_roll >= 6 and d100_roll <= 7):
        return InhabitationTypes.Hamlet
    if(d100_roll >= 8 and d100_roll <= 9):
        return InhabitationTypes.Village
    if(d100_roll == 10):
        return InhabitationTypes.Town
    if(d100_roll == 11):
        return InhabitationTypes.City
    if(d100_roll >= 12 and d100_roll <= 14):
        return InhabitationTypes.Castle
    if(d100_roll >= 15 and d100_roll <= 6):
        another_d100_roll = random.randint(1, 100)
        if(another_d100_roll >= 1 and another_d100_roll <= 30):
            return InhabitationTypes.RuinsVillage
        if(another_d100_roll >= 31 and another_d100_roll <= 60):
            return InhabitationTypes.RuinsCity
        if(another_d100_roll >= 61 and another_d100_roll <= 85):
            return InhabitationTypes.RuinsShrine
        if(another_d100_roll >= 86 and another_d100_roll <= 100):
            return InhabitationTypes.RuinsTomb
    if(d100_roll >= 17 and d100_roll <= 100):
        return InhabitationTypes.Uninhabited