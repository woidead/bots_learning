from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup



menukeyboard = ReplyKeyboardMarkup(resize_keyboard=True, input_field_placeholder='нажмите на желаюмую команду')
b1 = KeyboardButton(text='/help')
b2 = KeyboardButton('/description')
b3 = KeyboardButton('/random_agent')
menukeyboard.add(b1, b2, b3)