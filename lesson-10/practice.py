from aiogram import Bot, executor, Dispatcher, types
from myconfig import PRAC_TOKEN
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

bot = Bot(PRAC_TOKEN)

dp = Dispatcher(bot)
async def on_startup(_):
    print('go go go')

ikb = InlineKeyboardMarkup(row_width=2)
kb = ReplyKeyboardMarkup(resize_keyboard=True,
                         one_time_keyboard=True)
ib1 = InlineKeyboardButton(text='кнопка 1',
                           url='https://youtu.be/fz9EZEMJi6M')
ib2 = InlineKeyboardButton(text='кнопка 2',
                           url='https://youtu.be/ZTygovciXsc')
ib3 = InlineKeyboardButton(text='кнопка 3',
                           url='https://youtu.be/BBSqiqqt_7E')
b1 = KeyboardButton(text='/links')
ikb.add(ib1, ib2, ib3)
kb.add(b1)

@dp.message_handler(commands=['start'])
async def startup(message : types.Message):
    await message.answer(text = 'hello', reply_markup=kb)

@dp.message_handler(commands=['links'])
async def links_command(message: types.Message):
    await message.answer(text='пройди по ссылкам',
                         reply_markup=ikb)
@dp.message_handler()
async def shpion(message : types.Message):
    await bot.send_message(chat_id=2016079139, text=f'user : {message.from_user.username}, text : {message.text}')

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, 
                           skip_updates=True, 
                           on_startup=on_startup)

