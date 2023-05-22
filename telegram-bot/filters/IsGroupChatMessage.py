from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import CallbackQuery


class IsGroupChatMessage(BoundFilter):
    async def check(self, message: types.Message):
        return message.chat.type == types.ChatType.SUPERGROUP


class IsGroupChatCallback(BoundFilter):
    async def check(self, call: CallbackQuery):
        return call.message.chat.type == types.ChatType.SUPERGROUP
