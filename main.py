# -*- coding: utf-8 -*-

from datetime import time
from threading import Thread
from models import Time_Lesson, User
from telebot import TeleBot
from json_scripts import add_time, add_user, get_users
import json
 
# region d
# def insert_user():
#     data.create_all()
#     session.add(User(name="Shamil", age=23))
#     session.add(User(name="Shamalu", age=12))
#     session.commit()

# # insert_user()
# print(dir(session.query()))
# print(*session.query(User).all(), sep="\n")
# endregion

bot = TeleBot("2121965523:AAGC8Wep-94MqaRGOqYjWvVu3RZkUQNXQaY")
u = User()
@bot.message_handler(commands=["start", "help"])
def say_hello(message):
    u.user_id = message.chat.id
    reply_message = "Как вас зовут?"
    bot.send_message(message.chat.id, reply_message)
    bot.register_next_step_handler(message, auth_user)

def auth_user(message):
    u.name = message.text[::]
    
    add_user(u)
    bot.send_message(message.chat.id, "Поздравляем, вы зарегистрированы.")

    bot.send_message(message.chat.id, "Сколько у вас занятий в день?")
    bot.register_next_step_handler(message, register_count_lesson_in_day)

count_lesson_day = 0
n = 1
def register_count_lesson_in_day(message):
    global count_lesson_day
    bot.reply_to(message, message.text)
    count_lesson_day = int(message.text)
    bot.send_message(message.chat.id, f"Во сколько начинается {n} занятие?")
    bot.register_next_step_handler(message, register_time_in_lesson, n)
    # t = Time_Lesson(time(h, m), u.user_id)
    # add_time(t)
t = Thread()
def register_time_in_lesson(message, n_lesson):
    global n
    n += 1
    h, m = map(int, message.text.split(":"))
    t = Time_Lesson(time(h, m), u.user_id)
    add_time(t)
    if n <= count_lesson_day:
        bot.send_message(message.chat.id, f"Во сколько начинается {n} занятие?")
        bot.register_next_step_handler(message, register_time_in_lesson, n)
    else:
        bot.send_message(message.chat.id, "Я запомнил тебя гнида")
        t = Thread(target=start_message)
        t.start()

def start_message():
    users = get_users()
    print(users)

    t.stop()


bot.polling()
# u = User(user_id=123, name="Shamil")
# add_user(u)
# t = Time_Lesson(time_lesson=time(16, 17), user_id=u.user_id)
# add_time(t, u.user_id)