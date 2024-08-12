import telebot
from telebot import types

token = '6432706061:AAF3FmH1uMfjYtEQrce8h4yOltdGFzRNFOI'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def hello(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    keyboard.add(types.KeyboardButton('Sponsor💳'), types.KeyboardButton('Buy NFT💎'))
    bot.send_message(message.chat.id, 'If you would like to support me, you can sponsor me here. (Only Ethereum)', reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def main_menu(message):
   if message.text == 'Sponsor💳':
       bot.send_photo(message.chat.id,open('QRWallet.png','rb'))
       bot.send_message(message.chat.id, '0xD6b9967036A64818A359CDbCA06EcB513651F655')
   elif message.text == 'Buy NFT💎':
      bot.send_message(message.chat.id, 'https://opensea.io/0x2713E97f1cCF7602876BD8C0768d9B961865B853')

bot.polling(none_stop=True)
