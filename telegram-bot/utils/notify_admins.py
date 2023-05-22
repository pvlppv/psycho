import logging

from aiogram import Dispatcher

from data.config import admins


async def on_startup_notify(dp: Dispatcher):
    for admin in admins:
        try:
            text = '<b>Bot is on.</b>'
            await dp.bot.send_message(chat_id=admin, text=text)
        except Exception as err:
            logging.exception(err)


async def on_shutdown_notify(dp: Dispatcher):
    for admin in admins:
        try:
            text = '<b>Bot is off.</b>'
            await dp.bot.send_message(chat_id=admin, text=text)
        except Exception as err:
            logging.exception(err)
