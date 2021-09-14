from telegram.ext import Updater, Dispatcher, CommandHandler, MessageHandler, Filters
from const import TOKEN
from func import *
upd = Updater(token=TOKEN, workers=4)
ds = upd.dispatcher
ds.add_handler(CommandHandler('start', start))
ds.add_handler(CommandHandler('score', score))
ds.add_handler(MessageHandler(Filters.text, press_f))

updater.start_polling(clean=True)
updater.idle()
