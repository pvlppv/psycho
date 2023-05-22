from aiogram.dispatcher.filters.state import StatesGroup, State


class state(StatesGroup):
    name = State()
    username = State()
