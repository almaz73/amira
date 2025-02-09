import asyncio
import logging
import sys
from os import getenv

from aiogram import F
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery


import env
import keyboards as kb
import whorehouse.wb as wb
import utils.wb_analiz as wb_analiz
import utils.ghost as ghost
import utils.citation as citation



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
    print('====message==', message)
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
        return await message.answer(text='Выбери или пиши ост463', reply_markup=kb.keyboard)

    try:
        WB = message.text.upper().find('WB')
        help = message.text.upper().find('HELP')
        ost = message.text.upper().find('OST')
        if not ost: ost = message.text.upper().find('ОСТ')
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



@dp.callback_query(F.data.in_(['game','cit','ost','wb']))
async def process_buttons_press(callback: CallbackQuery):   
    if callback.data == 'wb': await callback.message.answer(wb.getWB())
    if callback.data == 'cit': 
        answer = citation.nextCitation()
        await callback.message.answer("Цитата:\n"+answer, reply_markup=kb.getTranslateLink(answer)) 
    if callback.data == 'game': await callback.message.answer(ghost.start())
    if callback.data == 'ost': 
        await callback.message.answer(text='Выбери или пиши ost463',reply_markup=kb.keyboard) 

@dp.callback_query(F.data.in_(['262','382','463','542','567','755']))
async def process_buttons_press(callback: CallbackQuery):    
    print ('callback', callback.data)
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