from aiogram import Bot, Dispatcher, executor, types
from myconfig import PRAC_TOKEN
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
bot = Bot(PRAC_TOKEN)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
b1 = KeyboardButton(text='/help')
b2 = KeyboardButton(text='/vote')
kb.add(b1, b2)

ikb = InlineKeyboardMarkup(row_width=1)
ib1 = InlineKeyboardButton(text='+', callback_data='like')
ib2 = InlineKeyboardButton(text='-', callback_data='dislike')
ikb.add(ib1, ib2)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
       await bot.send_message(chat_id=message.from_user.id,
                              text='welcome to our bot!',
                              reply_markup=kb)

@dp.message_handler(commands=['vote'])
async def vote(message: types.Message):
       await bot.send_photo(chat_id=message.from_user.id,
                            caption='you like this?',
                            photo='https://4kwallpapers.com/images/wallpapers/omen-valorant-pc-games-2020-games-1920x1200-2822.png',
                              reply_markup=ikb)

@dp.callback_query_handler()
async def callback_vote(callback:types.CallbackQuery):
        if callback.data == 'like':
            return await callback.answer(text='you like this')
        await callback.answer('you dont like this photo')

@dp.message_handler()
async def echo(message: types.Message):
        await message.answer(text=message.text)


async def on_startup(_):
        print('go go go')

         
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)
 