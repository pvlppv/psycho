from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_default = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Test'),
        ],
        [
            KeyboardButton(text='Test')
        ],
        [
            KeyboardButton(text='Test'),
        ]
    ],
    resize_keyboard=True
)
