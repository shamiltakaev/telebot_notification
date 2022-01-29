from json_scripts import add_time, add_user, get_users
from models import Time_Lesson, User
from telebot import TeleBot
from threading import Thread
from time import sleep, strftime

bot = TeleBot("2121965523:AAGC8Wep-94MqaRGOqYjWvVu3RZkUQNXQaY")


@bot.message_handler(commands=["notif"])
def notif(message):
    global thread

    if not thread.is_alive():
        thread.start()


@bot.message_handler(commands=["start", "help"])
def say_hello(message):
    global n
    n = 1
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


thread = Thread()


def register_time_in_lesson(message, n_lesson):
    global n, thread
    n += 1
    # h, m = map(int, message.text.split(":"))
    t = Time_Lesson(message.text, u.user_id)
    add_time(t)
    if n <= count_lesson_day:
        bot.send_message(
            message.chat.id, f"Во сколько начинается {n} занятие?")
        bot.register_next_step_handler(message, register_time_in_lesson, n)
    else:
        bot.send_message(message.chat.id, "Я запомнил тебя гнида")

        if not thread.is_alive():
            thread.start()


def start_message():
    while True:
        users = get_users()
        # print(strftime("%H:%M"))
        for key, value in users.items():
            # print(key[5:], value)
            if strftime("%H:%M") in value["times"]:
                bot.send_message(key[5:], "Сколько детей присутствовало на занятии?")
                dict(users).pop(key)
        sleep(60)

    return


thread = Thread(target=start_message)
u = User()

thread.start()
bot.polling()
# u = User(user_id=123, name="Shamil")
# add_user(u)
# t = Time_Lesson(time_lesson=time(16, 17), user_id=u.user_id)
# add_time(t, u.user_id)
