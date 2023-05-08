import telebot
import datetime
from test.config import Token_tg 

bot = telebot.TeleBot(Token_tg)

user_data = {}

# Define a message handler that asks for the user's name
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(chat_id=message.chat.id, text='What is your name?')
    bot.register_next_step_handler(message, handle_name)

# Define a message handler that asks for the time of the table booking
def handle_name(message):
    # Insert the user's ID, name, and time of the booking and appeal at the end of the array
    user_data = {'id': message.chat.id, 'name': message.text, 'booking_date': '', 'appeal_date': ''}
    with open('text.txt', 'a') as f:
        f.write(str(user_data) + '\n')
    bot.send_message(chat_id=message.chat.id, text='What time do you want to book a table?')
    bot.register_next_step_handler(message, handle_time)

# Define a message handler that records the user's name and time of the table booking
def handle_time(message):
    # Update the user's booking date in the array
    with open('text.txt', 'r') as f:
        lines = f.readlines()
    with open('text.txt', 'w') as f:
        for line in lines:
            if str(message.chat.id) in line:
                user_data = eval(line)
                user_data['booking_date'] = message.text
                f.write(str(user_data) + '\n')
            else:
                f.write(line)
    # Insert the time of the user's message at the end of the array
    with open('text.txt', 'a') as f:
        f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\n')
    # Update the user's appeal date in the array
    with open('text.txt', 'r') as f:
        lines = f.readlines()
    with open('text.txt', 'w') as f:
        for line in lines:
            if str(message.chat.id) in line:
                user_data = eval(line)
                user_data['appeal_date'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                f.write(str(user_data) + '\n')
            else:
                f.write(line)
    bot.send_message(chat_id=message.chat.id, text='Thank you for booking a table!')


bot.infinity_polling()
# bot.polling()