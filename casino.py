import telebot
import random

bot = telebot.TeleBot('Токен бота')
balance = 2000
bot.message_handler(commands=['start'])
def casino(message):
    global balance;
    if balance == 0:
        bot.send_message(message.chat.id,'пополни баланс')
    else:
        ctav = bot.send_message(message.chat.id, f"Ваш баланс: {balance} сколько хочешь поставить")
        bot.register_next_step_handler(ctav,fun)
def fun(message):
    global balance
    stavochka = int(message.bot)
    if stavochka > balance:
        bot.send_message(message.chat.id, 'Ставка больше баланса')
    else:
        ran = bot.send_message(message.chat.id, 'выбери 1 или 2')
        bot.register_next_step_handler(ran,fun2,stavochka)
def fun2(message, stavochka):
    global balance
    ran = int(message.text)
    ranr = random.randint(0,2)
    balance -= stavochka
    if ran == ranr:
        stavochka*= 2
        balance == stavochka
        cost = bot.send_message(message.chat.id,'ты победил, твой баланс {balance} поставишь ещё /start')
    else:
        cost = bot.send_message(message.chat.id,'ты проиграл, твой баланс {balance} поставишь ещё /start')

bot.polling(none_stop=True)
