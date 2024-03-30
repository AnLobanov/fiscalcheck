import os, django
os.environ["DJANGO_SETTINGS_MODULE"] = 'fiscalcheck.settings'
django.setup()
from telebot import TeleBot
from kkm.models import KKM, Settings
from fiscalcheck.settings import TELEGRAM
import datetime

bot = TeleBot(TELEGRAM['token'])
day = Settings.objects.first().days
for kkm in KKM.objects.all():
    if kkm.exp.month == datetime.date.today().month + 1 and kkm.exp.year == datetime.date.today().year:
        bot.send_message(TELEGRAM['channel'], '<b>ФН кассы ' + kkm.name + ' истекает через ' + str(kkm.days) + ' дней!</b>\n\nРегистрационный номер ККМ: ' + kkm.reg + '\nЮридическое лицо: ' + kkm.yl + '\nАдрес магазина: ' + kkm.adr, parse_mode="html")
    