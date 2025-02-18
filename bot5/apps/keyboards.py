from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton


startMenu = ReplyKeyboardMarkup(
  keyboard=[
    [
      KeyboardButton(text='✅ Цитата'),
      KeyboardButton(text='☸ Wildberies')
    ]
  ],
  resize_keyboard=True,
  one_time_keyboard=False,
  input_field_placeholder='Начальное меню'
)

subMenu = ReplyKeyboardMarkup(
  keyboard=[
    [
      KeyboardButton(text='↩ Назад'),     
      KeyboardButton(text='🐸 Приемка')
    ],
    [
      KeyboardButton(text='☝ Ссылки'),
      KeyboardButton(text='🛒 Остатки')
    ]
  ],
  resize_keyboard=True,
  one_time_keyboard=False,
  input_field_placeholder='Подменю'
)


# инлайн-команды
# h1 = InlineKeyboardButton(text='Цитата',callback_data='cit')
# h2 = InlineKeyboardButton(text='Игра',callback_data='game')
# h3 = InlineKeyboardButton(text='Склад',callback_data='wb')
# h4 = InlineKeyboardButton(text='Топ товары',callback_data='ost')
# help_commands = InlineKeyboardMarkup(
#     inline_keyboard=[[h1,h2],[h3, h4]]
# )

links = """/cit - Случайная цитата
/wb - склад WB (приемка)
/ost - Остатки по товарам (ost463)
/game - игра 'Угадай число
/love - I love You'"""

iloveYou="""░░░░░░░░░░░░░░░░
▄▄▄░░░░▄▄▄░░░▄▄▄
██▀░░▄█████▄████
█░░░████████████
█░░░████████████
█░░░▀███████████
█▄░░░░▀█████████
████░░░░▀█████▀░
░░░░░░░░░░▀█▀░░░
░░░░░░░▄▄░░░░░░░
█░██▀▄█▀▀█▄░▀█░█
█▄█▀▄█░░░░█▄░█░█
░█░░██░░░░██░█░█
░█░░░█▄░░▄█░░█░█
███▄░░▀██▀░░░▀█▀
░░░░░░░░░░░░░░░░"""


# Создаем объекты инлайн-кнопок
bt1 = InlineKeyboardButton(text='262',callback_data='262')
bt2 = InlineKeyboardButton(text='382',callback_data='382')
bt3 = InlineKeyboardButton(text='463',callback_data='463')
bt4 = InlineKeyboardButton(text='542',callback_data='542')
bt5 = InlineKeyboardButton(text='567',callback_data='567')
bt6 = InlineKeyboardButton(text='755',callback_data='755')
keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[bt1, bt2, bt3, bt4, bt5, bt6]]
)

# def createOstButtons(keys):
#     print('keys = ', keys)
#     return InlineKeyboardMarkup(inline_keyboard=[[bt1, bt2, bt3]])
   



def getTranslateLink(answer):
  return InlineKeyboardMarkup(
            inline_keyboard= [[
                InlineKeyboardButton(
                    text='Перевод', 
                    url=f"https://translate.google.ru/?sl=en&tl=ru&text={answer}&op=translate")
            ]]
        ) 

