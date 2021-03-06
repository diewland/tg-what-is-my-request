import os
import jsonpickle
from telegram.ext import Updater, MessageHandler, Filters

HEROKU_APPNAME = 'tg-what-is-my-request'
TOKEN = os.environ.get('TOKEN', 'TOKEN')
PORT = int(os.environ.get('PORT', '5000'))

def echo(bot, update):
    #update.message.reply_text('Bot answer: ' + update.message.text)
    update.message.reply_text(jsonpickle.encode(update.message))


updater = Updater(TOKEN)

# add handlers
updater.dispatcher.add_handler(MessageHandler(Filters.text, echo))

updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN)
updater.bot.setWebhook("https://%s.herokuapp.com/%s" % (HEROKU_APPNAME, TOKEN))
updater.idle()
