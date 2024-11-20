import telebot
import sqlite3

bot = telebot.TeleBot("7944738012:AAEJzGXcWOtHwabM4WiBPOMKpYlPYUINm30")

@bot.message_handler(commands = ['start'])
def create_BD(message): #без message нельзя объявлять, потому что он всегда передает message
    conn = sqlite3.connect('Test_BD.sql')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS users (count INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, room TEXT, telegram_id)')
    conn.commit()
    cur.close()
    conn.close()
    bot.register_next_step_handler(message)

def user_greet(message):
    bot.send_message(message.chat.id, 'Привет! Давай знакомиться ... нужно вставить текст приветсвия ')


bot.polling(none_stop=True)