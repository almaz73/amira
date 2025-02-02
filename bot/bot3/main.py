import asyncio
import logging
import sys
import time

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

import env
import wb
import wb_ost


TOKEN = env.TELEGRAM_TOKEN

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")

global taskId

@dp.message()
async def echo_handler(message: Message) -> None:
    try:
        begin = message.text.upper().find('WB')
        help = message.text.upper().find('HELP')
        ost = message.text.upper().find('OST')
        if begin>-1:
            ans = wb.getWB()        
            await message.answer(ans)
        elif help>-1:
            await message.answer(f"wb - склады\n ost- Остатки\n ost463- Остатки по артикулу")
        elif ost>-1:
            print('taskId=', taskId)
            if not taskId: 
                taskId = wb_ost.startOst()
                print ('taskId', taskId)
                await message.answer(' 🌷 Отчет создан, можно делать анализ')
            else:
                message.answer(' 🌷 на анализ')          
                print(' На анализ')                  
                ans = wb_ost.getOst(taskId, message.text[3:])
                await message.answer(ans[4000:])
                   
        else: await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())


    