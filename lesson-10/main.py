from aiogram import Bot, Dispatcher, executor, types
from myconfig import PRAC_TOKEN
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

bot = Bot(PRAC_TOKEN)
dp = Dispatcher(bot)

ikb = InlineKeyboardMarkup(row_width=1)
b1 =  InlineKeyboardButton(
        text='my ig',
        url='https://www.instagram.com/woidead/'
)
b2 = InlineKeyboardButton(
        text='my tg',
        url='woidead.t.me'
)
ikb.add(b1, b2)
@dp.message_handler(commands=['start'])
async def echo(message: types.Message):
        await bot.send_message(
                chat_id=message.chat.id, 
                text='hello world',
                reply_markup=ikb,

        )


async def on_startup(_):
        print('go go go')

        
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup)
