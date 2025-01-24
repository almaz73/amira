import requests
from datetime import datetime
import env
import locale

locale.setlocale(locale.LC_TIME, 'Russian')  # Русификация

TG_KEY = env.TELEGRAM_TOKEN
TG_CHAT = env.TELEGRAM_CHAT

date = '24.05.2022'
date2 = '2025-01-18T00:00:00Z'
date = datetime.strptime(date, "%d.%m.%Y")

new_date = date.strftime("%Y.%m.%d")
print('_1=', new_date)

text = "2025-02-01T00:00:00Z"

days = ['Пн','Вт','Ср','Чт','Пт','Сб','Вс']
def getSimpleDate(text):
    print('DEF text', text)
    date_object = datetime.strptime(text, "%Y-%m-%dT%H:%M:%SZ")
   
    day = date_object.weekday()
    formatted_date = date_object.strftime("%d.%m.%y") +' ['+days[day]+']'
    
    print('DEF  formatted_date = ', formatted_date)
    print('day', days[day])
    return formatted_date




# Parse the text into a datetime object
date_object = datetime.strptime(text, "%Y-%m-%dT%H:%M:%SZ")
print('date_object', date_object)

# Parse the text into a datetime object
# date_object = datetime.strptime(text3, "%Y-%m-%d %H:%M:%S%z")
date_object = datetime.strptime(text, "%Y-%m-%dT%H:%M:%SZ")

print('_2_3=', date_object)

print('text', text)
print('_3=', getSimpleDate(text))
