# import telebot
# from telebot import types

# import requests

# bot = telebot.TeleBot("6022855457:AAEg8AAxmMB29uXczqmBjTMsGLPz51EMHzE")


# @bot.message_handler(commands=["start"])
# def start(message):
#     bot.send_message(message.from_user.id, "hello bul kolik juuwy " + message.from_user.first_name)

# @bot.message_handler(content_types=["text","media","audio"])
# # def getMessage(message):
# #     if message.text == "hello":
# #         bot.send_message(message.from_user.id,"Hello! How are you?")
# #     if message.text == "good":
# #         bot.send_message(message.from_user.id,"ne kino karaisn zaebal")
# #     # if message.text == "how are you?":
#     #     bot.send_message(message.from_user.id, "good and you?")
#     # else:
#     #     bot.send_message(message.from_user.id, "mother fuck")
# def knopka(message):
#     if message.text == "a":
#    # bot.send_message(message.from_user.id,"How are you?")
#         keyboard=types.InlineKeyboardMarkup()
#         key_good=types.InlineKeyboardButton(text="good",callback_data="yes")
#         key_bad=types.InlineKeyboardButton(text="bad",callback_data="no")

#         keyboard.add(key_good)
#         keyboard.add(key_bad)
#     bot.send_message(message.from_user.id,"How are you?",reply_markup=keyboard)

# bot.polling(none_stop=True)

import telebot
from telebot import types

bot = telebot.TeleBot("6208560882:AAGx4d_VJ95SNmXXlaSTnzsVFNFtFGaGjkA")

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.from_user.id, "Hello " + message.from_user.first_name)

@bot.message_handler(content_types=["text"])
# def getMessage(message):
#     if message.text == "hello":
#         # print("hello")
#         bot.send_message(message.from_user.id, "Hello")
#     else:
#         # print("goodbye")
#         bot.send_message(message.from_user.id, "Goodbye")
def knopka(message):
    if message.text == "a":
    # bot.send_message(message.from_user.id, "How are you?")
        keyboard = types.InlineKeyboardMarkup()
        key_good = types.InlineKeyboardButton(text="good", callback_data="yes")
        key_bad = types.InlineKeyboardButton(text="bad", callback_data="no")

        keyboard.add(key_good)
        keyboard.add(key_bad)
        bot.send_message(message.from_user.id, "How are you?", reply_markup=keyboard)

bot.polling(none_stop=True)


