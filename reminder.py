from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import logging

updater = Updater(token='635134354:AAFCoCiT5-3TfssZ6o5u12nPuNRc8A4IFIg')
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Welcome to the Reminder Bot.")

def remind(bot, update, args):
    initial_input = ' '.join(args)
    if initial_input.find(":P:") == -1:
        bot.send_message(chat_id=update.message.chat_id, text="I can't remind with nothing to remind!")
        return
    else:
        arg_input = initial_input.split(":P:")
        bot.send_message(chat_id=update.message.chat_id, text="ANNOUNCEMENT:\n\n" + arg_input[0] + "\n\nThis is a " + arg_input[1].upper() + " level of urgency")

    bot.deleteMessage(update.message.chat_id, update.message.message_id)

start_handler = CommandHandler('start', start)
remind_handler = CommandHandler('remind', remind, pass_args=True)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(remind_handler)

updater.start_polling()
updater.idle()
