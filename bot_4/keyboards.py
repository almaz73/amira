from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton

trlink = InlineKeyboardMarkup(
    inline_keyboard= [[
        InlineKeyboardButton(text='transp', url='https://translate.google.ru/?sl=en&tl=ru&text=He wants to run&op=translate')
    ]]
) 

startMenu = ReplyKeyboardMarkup(
  keyboard=[
    [
      KeyboardButton(text='✅ Цитата'),
      KeyboardButton(text='🐸 Меню')
    ]
  ],
  resize_keyboard=True,
  one_time_keyboard=False,
  input_field_placeholder='Начальное меню'
)

subMenu = ReplyKeyboardMarkup(
  keyboard=[
    [
      KeyboardButton(text='🔧 Настройки'),
      KeyboardButton(text='☸ Wildberies')
    ],
    [
       KeyboardButton(text='↩ Назад')
    ]
  ],
  resize_keyboard=True,
  one_time_keyboard=False,
  input_field_placeholder='Подменю'
)

