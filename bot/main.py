# нужно доработать тут еще

import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
import env


TOKEN = env.TELEGRAM_TOKEN

# All handlers should be attached to the Router (or Dispatcher)

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    
    # Большинство объектов событий имеют псевдонимы для методов API, которые можно вызывать в контексте событий
    # Например, если вы хотите ответить на входящее сообщение, вы можете использовать псевдоним `message.answer(...)`
    # и целевой чат будет передан в :ref:`aiogram.methods.send_message.SendMessage`
    # метод автоматически или вызовите метод API напрямую через
    # Экземпляр бота: `bot.send_message(chat_id=message.chat.id, ...)`
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")


@dp.message()
async def echo_handler(message: Message) -> None:
    """
    Обработчик перешлет полученное сообщение обратно отправителю

    По умолчанию обработчик сообщений будет обрабатывать все типы сообщений (например, текст, фото, наклейку и т. д.)
    """
    try:
        print('??? message', message)
        print('??? message.chat', message.chat)

        # Отправить копию полученного сообщения
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # Но не все типы поддерживают копирование, поэтому нужно это обработать
        await message.answer("Nice try!")


async def main() -> None:
    # Инициализируйте экземпляр бота со свойствами бота по умолчанию, которые будут переданы всем вызовам API.
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # И события запуска диспетчеризации
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
