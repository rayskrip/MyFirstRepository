import telebot
import datetime
import time
import threading

bot = telebot.TeleBot('введите токен')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, 'Привет! '
                          'Я чат-бот, который будет напоминать тебе '
                          'измерить артериальное давление! Правила измерения: /rules')
    reminder_thread = threading.Thread(target=send_reminders, args=(message.chat.id,))
    reminder_thread.start()


@bot.message_handler(commands=['rules'])
def rules_message(message):
    rules_list = ['туалет перед измерением',
                  'расслабтесь, сидя в кресле (ноги на полу, спина на опоре) в течение 5 минут',
                  'не разговаривайте',
                  'манжета правильного размера на голую руку',
                  'держите руку на уровне сердца']
    bot.reply_to(message, f'Правила измерения: {rules_list}')


def send_reminders(chat_id):
    first_rem = '08:00'
    second_rem = '20:00'
    while True:
        now = datetime.datetime.now().strftime('%H:%M')
        if now == first_rem or now == second_rem:
            bot.send_message(chat_id, 'Напоминание - измерь АД! Правила измерения: /rules')
            rules_message()
            time.sleep(61)
            time.sleep(1)


bot.polling(non_stop=True)
