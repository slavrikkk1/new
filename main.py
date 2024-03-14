import pyautogui as pg
from telebot import *
import time
import os

token = '6473588607:AAEAX8YUxI615O5R9g4VESlik_kOBKVvmPo'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def buttons(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('OFF пк')
    btn2 = types.KeyboardButton('Xbox Games')
    btn3 = types.KeyboardButton('3')
    markup.add(btn1)
    markup.add(btn2)
    bot.send_message(message.chat.id, 'выполнено подключение к пк', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def main_menu(message):
    # ---processing of the main buttons---
    if message.chat.type == ('private'):  # checking for a private message
        if message.text == 'OFF пк':
            os.system('shutdown -s')
            # time.sleep(2)
            # pg.typewrite(["winleft"])
            # pg.moveTo(1222, 979, 0.1)
            # pg.click()
            # pg.moveTo(1037, 883, 0.1)
            # pg.doubleClick()

        if message.text == 'Xbox Games':
            time.sleep(1)
            pg.typewrite(['winleft'])
            pg.moveTo(726, 341, 0.5)
            pg.click()
            time.sleep(2.3)
            pg.click()
            pg.click()
            pg.typewrite('Xbox')
            pg.moveTo(969, 643, 0.5)
            pg.click()

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('запустить Forza 4')
            btn2 = types.KeyboardButton('закрыть')
            btn3 = types.KeyboardButton('главная')
            markup.row(btn1, btn2)
            markup.add(btn3)
            bot.send_message(message.chat.id, 'Xbox запущен', reply_markup=markup)

        if message.text == 'главная':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('OFF пк')
            btn2 = types.KeyboardButton('Xbox Games')
            btn3 = types.KeyboardButton('3')
            markup.add(btn1)
            markup.add(btn2)
            bot.send_message(message.chat.id, 'выберите функцию', reply_markup=markup)

        if message.text == 'запустить Forza 4':
            pg.moveTo(129, 357, 0.5)
            pg.click()


bot.polling(none_stop=True)  # does not stop the cod