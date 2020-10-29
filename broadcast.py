#!/usr/bin/env python

#this script allow you to send Broadcast notification to all user.

from telegram.ext import Updater,CommandHandler,MessageHandler,MessageHandler
from telegram import Chat, Message, ChatPermissions
import secrets
import texts
from database import dbmanage
from scraper import Scraper, do_scraping
from circular import Circular

updater = Updater(secrets.TOKEN, use_context=True)

db = dbmanage()
chats = db.getChats()
circular = db.getCircularFromId(35)
db.close()

for chat in chats:
    updater.bot.sendMessage(chat_id=chat[0], text=texts.circularText.format(circular.id,circular.name,circular.date,circular.link))
    updater.bot.sendMessage(chat_id=chat[0], text="Si è verificato un problema durante la lettura della circolare n.35 pubblicata questa mattina. Ci scusiamo per il ritardo. Per segnalare problemi di questo tipo nel caso in cui si ripropongano contattare @Feld_Maresciallo. Grazie.")


