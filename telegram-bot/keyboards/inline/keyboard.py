from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

kb_inline = InlineKeyboardMarkup(row_width=1,
                                 inline_keyboard=[
                                     [
                                         InlineKeyboardButton(text='Test', callback_data='Test'),
                                     ],
                                     [
                                         InlineKeyboardButton(text='Test', callback_data='Test'),
                                     ],
                                     [
                                         InlineKeyboardButton(text='Test', callback_data='Test'),
                                     ],
                                 ])
