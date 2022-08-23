import random
from .terrain import TerrainTypes, get_terrain
from .inhabitation import InhabitationTypes, get_inhabitation

class Hex:
    def __init__(self, prev_terrain):
        d20_roll = random.randint(1, 20)
        self.terrain = get_terrain(prev_terrain, d20_roll)
        d100_roll = random.randint(1, 100)
        self.inhabitation = get_inhabitation(d100_roll)
    
    def next_hex(self):
        result = """
Местность: {}
Примеры: {}
Обитаемость: {}
        """
        place = None
        examples = None
        inhabitation = "Нет"
        if (self.terrain == TerrainTypes.Plain):
            place = "Равнина"
            examples = "Тундра, степь, саванна, прерии, луга и т.д."
        if (self.terrain == TerrainTypes.Scrub):
            place = "Низкая поросль"
            examples = "Кусты, заросли папоротников, вельды и т.д."
        if (self.terrain == TerrainTypes.Forest):
            place = "Лес"
            examples = "Хвойные, джунгли, тропические леса и т.д."
        if (self.terrain == TerrainTypes.Rough):
            place = "Бесплодные земли"
            examples = "Предыдущая местность, но \"плохая\". К примеру: Зеленый лес - мертвый сухостой."
        if (self.terrain == TerrainTypes.Desert):
            place = "Пустыня"
            examples = "Пустоши, пески, снежные равнины и т.д."
        if (self.terrain == TerrainTypes.Hills):
            place = "Холмы"
            examples = "Дюны, утесы, хребты, зеленые холмы и т.д."
        if (self.terrain == TerrainTypes.Mountains):
            place = "Горы"
            examples = "Ледники, скальные вершины, столовые горы и т.д."
        if (self.terrain == TerrainTypes.Marsh):
            place = "Болота"
            examples = "Топи, трясина, торфянники и т.д."
        if (self.terrain == TerrainTypes.ForestWithHills):
            place = "Холмистый лес"
            examples = "Лес расположенный на холмах. Отличается постоянным перепадом высот."
        if (self.terrain == TerrainTypes.HillsWithForest):
            place = "Лесистые холмы"
            examples = "Различные неровные поверхности с перепадами высот, покрытые местами лесом."
        if (self.terrain == TerrainTypes.MountainsWithPass):
            place = "Горы с проходом"
            examples = "Высокие горы с дорогой ведущей через них."
        if (self.terrain == TerrainTypes.Depression):
            place = "Низина"
            examples = "Та же местность, но с низиной (каньон, ущелье, провал и т.д.) В случае болота - это озеро."
        if (self.terrain == TerrainTypes.Pond):
            place = "Водоем"
            examples = "Озеро, пруд, а может и выход к морю."

        if(self.inhabitation == InhabitationTypes.SingleDwelling):
            inhabitation = "Одинокое жилище"
        if(self.inhabitation == InhabitationTypes.Thorp):
            inhabitation = "Маленькая деревушка"
        if(self.inhabitation == InhabitationTypes.Hamlet):
            inhabitation = "Деревня"
        if(self.inhabitation == InhabitationTypes.Village):
            inhabitation = "Село"
        if(self.inhabitation == InhabitationTypes.Town):
            inhabitation = "Небольшой город"
        if(self.inhabitation == InhabitationTypes.City):
            inhabitation = "Город"
        if(self.inhabitation == InhabitationTypes.Castle):
            inhabitation = "Замок"
        if(self.inhabitation == InhabitationTypes.RuinsVillage):
            inhabitation = "Руины деревни"
        if(self.inhabitation == InhabitationTypes.RuinsCity):
            inhabitation = "Руины города"
        if(self.inhabitation == InhabitationTypes.RuinsShrine):
            inhabitation = "Руины святыни"
        if(self.inhabitation == InhabitationTypes.RuinsTomb):
            inhabitation = "Руины гробницы"

        return result.format(place, examples, inhabitation)
