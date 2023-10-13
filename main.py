import telebot
import get_response_chat

API_TOKEN = '6471650866:AAHTPdx44_SCleVHTcMjKq0rUT-Kvq08uB8'

bot = telebot.TeleBot(API_TOKEN)
# history_messages = {'system': {"role": "system", "content": "You are a helpful assistant."}}


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'hi')


@bot.message_handler(func=lambda message: True)
def send_message(message):
    history_messages = get_response_chat.load_messages_file(message.chat.id)
    if message.chat.id not in history_messages:
        history_messages[str(message.chat.id)] = []
    user_history = history_messages[str(message.chat.id)]
    # user_history.append({'role': 'system', 'content': "You are a helpful assistant."})
    user_history.append({"role": "user", "content": message.text})
    response = get_response_chat.send_message_and_update_history(user_history)
    bot.send_message(message.chat.id, response)
    user_history.append({"role": "assistant", "content": response})
    get_response_chat.save_messages_user(message.chat.id, user_history)


bot.infinity_polling()