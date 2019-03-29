import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import apiai
import json


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)

logger = logging.getLogger(__name__)
updater = Updater(token='743489192:AAHLzlzm4V15A3Llwo6qZHSl9IQOcWybJ5Y')
dispatcher = updater.dispatcher


def startCommand(bot, context):
    bot.send_message(chat_id=context.message.chat_id, text='Hello udemy')


def textMessage(bot, context):
    request = apiai.ApiAI('875911928:AAECsDWTzTFf8AabCW2szTeNQuVg6fqKSw4').text_request()
    request.lang = 'hindi'
    request.session_id = 'UdemyAiBot'
    request.query = context.message.text

    responce_json = json.loads(request.getresponse().read().decode('utf-8'))
    responce = responce_json['result']['fulfillment']['speech']

    if responce:
        bot.send_message(chat_id=context.message.chat_id, text=responce)
    else:
        bot.send_message(chat_id=context.message.chat_id, text='I do not understand you!')


# Handlers
start_command_handler = CommandHandler('hello', startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)

dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)

updater.start_polling(clean=True)

updater.idle()