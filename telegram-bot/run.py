async def on_startup(dp):
    import filters
    filters.setup(dp)

    import middlewares
    middlewares.setup(dp)

    from utils.notify_admins import on_startup_notify
    await on_startup_notify(dp)

    # from utils.set_bot_commands import set_default_commands
    # await set_default_commands(dp)

    print('Bot is on.')


async def on_shutdown(dp):
    from utils.notify_admins import on_shutdown_notify
    await on_shutdown_notify(dp)
    print('Bot is off.')


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown, skip_updates=True)
