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
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")


@dp.message()
@dp.message()
async def echo_handler(message: Message) -> None:
    try:
        begin = message.text.upper().find('WB')
        help = message.text.upper().find('HELP')
        ost = message.text.upper().find('OST')
        game = message.text.upper().find('GAME')
        cit = message.text.upper().find('CIT')
        if ghost.isStarted():
            if not is_number(message.text): return ghost.end()                    
            else: return await message.answer(ghost.ask(int(message.text)))
        if game>-1: return await message.answer(ghost.start())

        if begin>-1:
            ans = wb.getWB()        
            await message.answer(ans)
        elif cit>-1:
            await message.answer(citation.nextCitation())
        elif help>-1:
            await message.answer(f"wb - склады\n ost- Остатки\n ost463- Остатки по артикулу")
        elif ost>-1:
            articulText = message.text[3:]
            if articulText == '0':
                 print (' 84848448 СОЗДАВАТЬ БУДЕТ')
                 wb_analiz.getAnaliz('0')
                 await message.answer('Создан новый файл аналитики') 

            elif not articulText:
                await message.answer(
                        text='Выбери или пиши ost463',
                        reply_markup=keyboard
                )
           
            
            else:
                ans = wb_analiz.getAnaliz(articulText)
                await message.answer(ans) 
                


                   
        else: await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")


# Создаем объекты инлайн-кнопок
bt1 = InlineKeyboardButton(text='262',callback_data='262')
bt2 = InlineKeyboardButton(text='382',callback_data='382')
bt3 = InlineKeyboardButton(text='463',callback_data='463')
bt4 = InlineKeyboardButton(text='542',callback_data='542')
bt5 = InlineKeyboardButton(text='567',callback_data='567')
bt6 = InlineKeyboardButton(text='755',callback_data='755')

# Создаем объект инлайн-клавиатуры
keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[bt1, bt2, bt3, bt4, bt5, bt6]]
)


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