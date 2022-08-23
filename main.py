import telebot
from telebot import types
from generator.terrain import TerrainTypes
from generator.hex_result import Hex
from .config import SECRET_TOKEN

bot = telebot.TeleBot(SECRET_TOKEN)

@bot.message_handler(commands=["start"])
def start(m, res=False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    plain=types.KeyboardButton("Равнина")
    markup.add(plain)
    
    scrub=types.KeyboardButton("Низкая поросль")
    markup.add(scrub)
    
    forest=types.KeyboardButton("Лес")
    markup.add(forest)
    
    rough=types.KeyboardButton("Бесплодные земли")
    markup.add(rough)
    
    desert=types.KeyboardButton("Пустыня")
    markup.add(desert)
    
    hills=types.KeyboardButton("Холмы")
    markup.add(hills)
    
    mountains=types.KeyboardButton("Горы")
    markup.add(mountains)
    
    marsh=types.KeyboardButton("Болота")
    markup.add(marsh)

    bot.send_message(m.chat.id, 'Выберите местность, в которой сейчас находятся игроки.',  reply_markup=markup)

@bot.message_handler(commands=["help"])
def start(m, res=False):
     bot.send_message(m.chat.id,
     """
Ваши игроки вышли за границы продуманного поля гексов?
Вы не знаете как вести кампанию дальше? Не беда!
Этот бот, работающий по таблице дикой местности Гигакса подскажет 
вам где очутились игроки! Запустите бота командой /start,
Выберите местность, которая больше всего похожа на ту, где
оказались персонажи игрков. Вуаля! Вы получили ответ на вопрос, в
какой местности они окажутся далее! Учтите, что этот бот лишь
дает подсказки а не прямое руководство к действию. Понимайте
его слова адекватно вашей кампании (если игроки бредут по пустыне,
то возникшая гора никак не может быть ледником).
     """
     )

@bot.message_handler(content_types=["text"])
def handle_text(message):
    if(message.text == "Равнина"):
        bot.send_message(message.chat.id, Hex(TerrainTypes.Plain).next_hex())
    if(message.text == "Низкая поросль"):
        bot.send_message(message.chat.id, Hex(TerrainTypes.Scrub).next_hex())
    if(message.text == "Лес"):
        bot.send_message(message.chat.id, Hex(TerrainTypes.Forest).next_hex())
    if(message.text == "Бесплодные земли"):
        bot.send_message(message.chat.id, Hex(TerrainTypes.Rough).next_hex())
    if(message.text == "Пустыня"):
        bot.send_message(message.chat.id, Hex(TerrainTypes.Desert).next_hex())
    if(message.text == "Холмы"):
        bot.send_message(message.chat.id, Hex(TerrainTypes.Hills).next_hex())
    if(message.text == "Горы"):
        bot.send_message(message.chat.id, Hex(TerrainTypes.Mountains).next_hex())
    if(message.text == "Болота"):
        bot.send_message(message.chat.id, Hex(TerrainTypes.Marsh).next_hex())

bot.polling(none_stop=True, interval=0)