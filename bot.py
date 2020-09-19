#!/urs/bin/env python
from telegram.ext import Updater,CommandHandler,MessageHandler,MessageHandler
from telegram import Chat, Message, ChatPermissions
import secrets
import texts
from database import dbmanage
from scraper import Scraper, do_scraping
from circular import Circular
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

#command handler
def start(update, context):
    user = update.message.from_user
    chat  = update.message.chat
    db = dbmanage()
    if(db.checkChat(chat)==False):
        db.addChat(chat)
    db.close()
    update.message.reply_text(texts.startMessage.format(user.first_name))
def ping(update, context):
    update.message.reply_text(texts.pong)
def help(update, context):
    update.message.reply_text(texts.help)

# function that send messages to all user with circular information
def sendCircularNotification(updater, circular):
    db = dbmanage()
    chats = db.getChats()
    db.close()
    for chat in chats:
        updater.bot.sendMessage(chat_id=chat[0], text=texts.circularText.format(circular.id,circular.name,circular.date,circular.link))

#initialize stuff
updater = Updater(secrets.TOKEN, use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("ping", ping))
dispatcher.add_handler(CommandHandler("help", help))

# schedule scraping operation
def scrapringProtocol():
    newCircular = do_scraping()
    for c in newCircular:
        sendCircularNotification(updater,c)



# scheduler 
sched = BackgroundScheduler()
sched.add_job(scrapringProtocol,"interval", hours=1, id="job1")
sched.start()


#start bot
updater.start_polling()
updater.idle()
print("hello world")