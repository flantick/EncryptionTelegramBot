import telebot
import config
import founder
import aes
import hashing
import gist
import ecp
from telebot import types

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("/help")
    markup.add(item1)

    bot.send_message(message.chat.id, config.WELLCOMEMESSAGE, reply_markup=markup)


@bot.message_handler(commands=['help'])
def helping(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("/help")
    markup.add(item1)

    bot.send_message(message.chat.id, config.HELP, reply_markup=markup)


@bot.message_handler(commands=['help_aes'])
def fernethelp(message):
    bot.send_message(message.chat.id, config.HELPAES)


@bot.message_handler(commands=['help_gost'])
def hosthelpp(message):
    bot.send_message(message.chat.id, config.GOSTHELP)


@bot.message_handler(commands=['help_hash'])
def hashhelpp(message):
    bot.send_message(message.chat.id, config.HASHHELP)


@bot.message_handler(commands=['help_sign'])
def hashhelpp(message):
    bot.send_message(message.chat.id, config.HELPSIGN)


@bot.message_handler(commands=['aesen'])
def ferneten(message):
    bot.send_message(message.chat.id, aes.aescrypt(founder.foundclef(message.text), founder.foundreport(message.text), True))


@bot.message_handler(commands=['aesde'])
def fernetende(message):
    bot.send_message(message.chat.id, aes.aescrypt(founder.foundclef(message.text), founder.foundreport(message.text), False))


@bot.message_handler(commands=['gosten'])
def asycrypt(message):
    bot.send_message(message.chat.id, gist.gostcrypt(founder.foundclef(message.text), founder.foundreport(message.text), True))


@bot.message_handler(commands=['gostde'])
def asydecrypt(message):
    bot.send_message(message.chat.id, gist.gostcrypt(founder.foundclef(message.text), founder.foundreport(message.text), False))


@bot.message_handler(commands=['mksign'])
def msign(message):
    bot.send_message(message.chat.id, ecp.mksign(founder.foundclef(message.text), founder.foundreport(message.text)))


@bot.message_handler(commands=['vrfsign'])
def vrsign(message):
    bot.send_message(message.chat.id, ecp.vrfsign(founder.foundkey1(message.text), founder.foundkey2(message.text), founder.foundreport(message.text), founder.foundsignature(message.text)))


@bot.message_handler(commands=['hash'])
def hashreport(message):
    bot.send_message(message.chat.id, hashing.hash(founder.foundclef(message.text), founder.foundreport(message.text)))


bot.polling(none_stop=True)