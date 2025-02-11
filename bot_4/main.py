import asyncio
import logging
import sys
from os import getenv

from aiogram import F
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery


import env
import keyboards as kb
import whorehouse.wb as wb
import utils.wb_analiz as wb_analiz
import utils.ghost as ghost
import utils.citation as citation
import baza.db as db



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



@dp.message()
async def echo_handler(message: Message) -> None:
    db.visit(message.from_user.first_name, message.from_user.id) # Записываем посетителя 
  

    # print('message.user.id = ', message.user)
    if message.text == '☸ Wildberies': return await message.answer('Выберите действие', reply_markup=kb.subMenu)
    if message.text == '↩ Назад': return await message.answer('Выберите действие', reply_markup=kb.startMenu)
    if message.text == '✅ Цитата': 
        answer = citation.nextCitation()
        return await message.answer(answer, reply_markup=kb.getTranslateLink(answer)) 
    if message.text == '☝ Ссылки': return await message.answer(kb.links, parse_mode='HTML')    
    if message.text == '🐸 Приемка': return await message.answer(wb.getWB())
    # if message.text == '🔧 Мои Планы': return await message.answer(kb.links, parse_mode='HTML')
    
    if message.text == '/love': return await message.answer(kb.iloveYou)
    if message.text == '/ost' or  message.text == '🛒 Остатки':
        store_ids = db.wb_get_store(message.from_user.id) 
        print('store_ids = ', store_ids)
        if not store_ids: return await message.answer('Необходимо скопировать токен для чтения данных по API из настроек продавца. Тогда можно будет увидеть остатки товаров из этого магазина')
        else: return await message.answer(text='Выбери или пиши ост463', 
                                           reply_markup=kb.createOstButtons(store_ids))

    if len(message.text)>100 and message.text.find('QifQ.'): 
        db.wb_add_store(message.from_user.id, message.text)
        return await message.answer('Токен сохранен')

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
            ans = wb.getWB()        
            await message.answer(ans)
        elif cit>-1:
            await message.answer(citation.nextCitation())
        elif help>-1:
            await message.answer(f"wb - склады\n ost- Остатки\n ost463- Остатки по артикулу")
        elif ost>-1:
            articulText = message.text[3:]
            if articulText == '0':
                 wb_analiz.getAnaliz('0')
                 await message.answer('Создан новый файл аналитики') 
            elif not articulText:
                await message.answer(
                        text='Выбери или пиши ost463',
                        reply_markup=kb.keyboard
                )
            else:
                ans = wb_analiz.getAnaliz(articulText)
                await message.answer(ans)                    
        else: await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")


#, .in_(['262','382','463','542','567', '755'])
@dp.callback_query(F.data)
async def process_buttons_press(callback: CallbackQuery):    
    print ('callback.data', callback.data)    
    ans = wb_analiz.getAnaliz(callback.data)
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