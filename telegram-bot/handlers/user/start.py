from aiogram import types

from filters import IsPrivateChatMessage
from loader import dp
from utils.misc import rate_limit


@rate_limit(limit=1, key='/start')
@dp.message_handler(IsPrivateChatMessage(), text='/start')
async def start(message: types.Message):
    await message.answer(f'Start!')
