import asyncio
import logging
import sys

from aiogram import F
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

import env
from apps import keyboards as kb
import apps.wb as wb
import apps.wb_analiz as wb_analiz
import apps.ghost as ghost
import apps.citation as citation
import baza.BD_methods as db



TOKEN = env.TELEGRAM_TOKEN

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!", reply_markup=kb.startMenu)

@dp.message(lambda message: message.web_app_data and message.web_app_data.data)
async def echo_miniApp(message: Message) -> None:
    db.visit(message.from_user.first_name, message.from_user.id) # записываем посетителя

    # print('########## message = ', message)  # вся информация о сообщении
    # print(' message.from_user.id',  message.from_user.id)
    # print('== == == message.web_app_data', message.web_app_data)
    # пришло с веб апп

    stores = {}
    arrStores =  message.web_app_data.data.split('🐷')
    ind = 0
    for el in arrStores:
        ind += 1
        arrEl = el.split('🌞')
        if arrEl[0]:
            stores[ind] = {'name': arrEl[0], 'art': arrEl[1], 'token': arrEl[2]}

    # print('Получили из МИНИАПП=',message.web_app_data)
    # print ('stores', stores)
    db.saveDatasFromMiniApp(message.from_user.id, message.web_app_data.data)



@dp.message()
async def echo_handler(message: Message) -> None:
    global currentUUID
    tgId = message.from_user.id
    db.visit(message.from_user.first_name, tgId) # Записываем посетителя


    print('<><><><><><> message.text = ', message.text)
    if not currentUUID: currentUUID = getCurrentUUID()


    # print('message.user.id = ', message.user)
    if message.text == '☸ Wildberies': return await message.answer('Выберите действие', reply_markup=kb.subMenu)
    if message.text == 'set': return await message.answer('Получить данные', reply_markup=kb.getLinkFromBD(tgId))
    if message.text == '↩ Назад': return await message.answer('Другие возможности:\n\n'+kb.links, reply_markup=kb.startMenu)
    if message.text == '✅ Цитата': 
        answer = citation.nextCitation()
        return await message.answer(answer, reply_markup=kb.getTranslateLink(answer)) 
    if message.text == '☝ Ссылки': return await message.answer(kb.links, parse_mode='HTML')
    if message.text == '🐸 Приемка':
        key = env.WB_KEY # Пока ключ берем зашитый в код
        return await message.answer('<b>Прогноз на 14 дней</b>:\n\n' + wb.getWB(key), parse_mode='HTML')
    
    if message.text == '/love': return await message.answer(kb.iloveYou)
    if message.text == '/ost' or  message.text == '🛒 Остатки':
        store_ids = db.wb_get_store(message.from_user.id) 
        print('st o r e _ i d s = ', store_ids)
        if not store_ids: return await message.answer('Нет данных по магазинам, необходимо зайти в "Настройки"')
        else: return await message.answer(text='Выбор магазина:',reply_markup=kb.getOst_stores(tgId))

    # if message.text[-3:] == '###':
    #     return await message.answer('Артикул удален', reply_markup=kbOst.delBt(message.text))
    # elif message.text.find(',')>-1 and message.text[-1] == '#':
    #     return await message.answer('Артикулы добавлены',reply_markup=kbOst.addBts(message.text))


    # if len(message.text)>100 and message.text.find('QifQ.'):
    #     db.wb_add_store(message.from_user.id, message.te xt)
    #     return await message.answer('Токен сохранен')

    if message.text== None :
        print('========None=======')
        return False

    # Если не отловили, пробуем по вхождению букв
    try:
        WB = message.text.upper().find('WB')
        help = message.text.upper().find('HELP')
        ost = message.text.upper().find('OST') 
        if ost < 0: ost = message.text.upper().find('ОСТ')
        game = message.text.upper().find('GAME')
        cit = message.text.upper().find('CIT')
        if ghost.isStarted():
            if not is_number(message.text): return ghost.end()                    
            else: return await message.answer(ghost.ask(int(message.text)))
        if game>-1: return await message.answer(ghost.start())
        if WB>-1:
            ans = wb.getWB(env.WB_KEY)
            await message.answer(ans)
        elif cit>-1:
            answer = citation.nextCitation()
            await message.answer(answer, reply_markup=kb.getTranslateLink(answer))
        elif help>-1:
            await message.answer(f"wb - склады\n ost- Остатки\n ost463- Остатки по артикулу")
        elif ost>-1:
            articulText = message.text[3:]
            if articulText == '0':
                 wb_analiz.getAnaliz('0', currentUUID)
                 await message.answer('Создан новый файл аналитики') 
            elif not articulText:
                await message.answer(
                        text='Выбери или пиши ost463',
                        reply_markup=kb.getOst(tgId)
                        # reply_markup=kb.keyboard
                )
            else:
                ans = wb_analiz.getAnaliz(articulText, currentUUID)
                await message.answer(ans)                    
        else: await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")



# currentUUID = '95bf851b66f647fdbfd2caebdcbdd9f6'
currentUUID = ''
def getCurrentUUID():
    global currentUUID
    if not currentUUID:
        # Если нет выбранного магазина, выбираем первый в списке
        return wb_analiz.getFirstUUID()




#, .in_(['262','382','463','542','567', '755'])
@dp.callback_query(F.data)
async def process_buttons_press(callback: CallbackQuery):
    global currentUUID
    if not currentUUID: currentUUID = getCurrentUUID()
    print('callback.data=0=', callback.data)

    tgId = callback.from_user.id
    if len(callback.data)>7 and callback.data.find('hop::'):
        await callback.message.edit_text(
            text='Выбери или пиши ost463',
            reply_markup=kb.getOst_arts(tgId, callback.data[7:])
        )
        return False
    else:
        print('>>!>>!>>!callback.data=', callback.data)

        # print('DEBUG ____')
        # return  False

        # textAndUUID = callback.data.split('###')
        # currentUUID = textAndUUID[1]
        ans = wb_analiz.getAnaliz(callback.data, currentUUID)
        await callback.message.edit_text(ans)
        await callback.answer()


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())