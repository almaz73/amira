from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton, WebAppInfo
from baza import BD_methods

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
            KeyboardButton(text='☝ Настройки', web_app=WebAppInfo(url="https://fmap.ru/tg_wbFree/WBfreeStore.html")),
            # KeyboardButton(text='☝ Настройки', web_app=WebAppInfo(url="https://fmap.ru/tg_wbFree/WBfreeStore.html?d=Магазин1🌞123,222,333,444🌞1🐷Маг2🌞12,2,🌞🐷")),
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

iloveYou = """░░░░░░░░░░░░░░░░
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
bt1 = InlineKeyboardButton(text='262', callback_data='262')
bt2 = InlineKeyboardButton(text='382', callback_data='382')
bt3 = InlineKeyboardButton(text='463', callback_data='463')
bt4 = InlineKeyboardButton(text='542', callback_data='542')
bt5 = InlineKeyboardButton(text='567', callback_data='567')
bt6 = InlineKeyboardButton(text='755', callback_data='755')
keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[bt1, bt2, bt3, bt4, bt5, bt6]]
)


## метод для получения данных из базы для miniAPP
def getLinkFromBD(tgId):
    link = BD_methods.getSavedStoresBeforeEdit(tgId)
    # link = "SHOP_1🌞123,777🌞exist🐷Shop_2🌞12,2,7🌞exist🐷"
    return InlineKeyboardMarkup(
        inline_keyboard=[[
            InlineKeyboardButton(text='из базы данных',
                                 web_app=WebAppInfo(url="https://fmap.ru/tg_wbFree/WBfreeStore.html?d=" + link))
        ]]
    )


## Метод для получения списка магазинова пользователя
def getOst_stores(tgId):
    list = BD_methods.wb_get_arts(tgId)
    bts=[]
    for i in list:
        print('i', i[0])
        bts.append(InlineKeyboardButton(text=i[0], callback_data='shop:::'+i[0]))
    return InlineKeyboardMarkup(inline_keyboard=[bts])

## Метод для получения остатков пользователя по uuid магазина
def getOst_arts(tgId, storeName):
    list = BD_methods.wb_get_arts(tgId)
    bts = []
    for i in list:
        print('i', i)
        if storeName == i[0]:
            for k in i[1].split(','):
                bts.append(InlineKeyboardButton(text=k, callback_data=k +'###' + storeName+'###'+i[2]))
    return InlineKeyboardMarkup(inline_keyboard=[bts])

# print(getOst(777))
# print(getOst_arts(777, 'SHOP_1'))

# def createOstButtons(keys):
#     print('keys = ', keys)
#     return InlineKeyboardMarkup(inline_keyboard=[[bt1, bt2, bt3]])


def getTranslateLink(answer):
    return InlineKeyboardMarkup(
        inline_keyboard=[[
            InlineKeyboardButton(
                text='Перевод',
                url=f"https://translate.google.ru/?sl=en&tl=ru&text={answer}&op=translate")
        ]]
    )


