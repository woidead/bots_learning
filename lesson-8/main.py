from aiogram import Bot, Dispatcher, executor, types
from myconfig import PRAC_TOKEN
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

bot = Bot(PRAC_TOKEN)
dp = Dispatcher(bot)
HELP_COMMAND = """
<b>/start</b> - <em>старт</em> 
<b>/help</b> - <em>команды бота</em> 
<b>/description</b> - <em>описание</em> 
<b>/pic</b> - <em>пикча</em> 
"""
kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('/help')
b2 = KeyboardButton('/description')
b3 = KeyboardButton('/pic')
kb.add(b1).insert(b2).add(b3)

@dp.message_handler(commands=['start'])
async def start_command(message:types.Message):
        await bot.send_message(
                        chat_id=message.from_user.id, 
                        text='Добро пожаловать в нашего бота', 
                        reply_markup=kb,
        )


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
        await bot.send_message( 
                        message.from_user.id, 
                        text=HELP_COMMAND, 
                        parse_mode="HTML",
                        reply_markup=ReplyKeyboardRemove()
                        )




@dp.message_handler(commands=['description'])
async def description(message: types.Message):
        await bot.send_message(
                                chat_id=message.from_user.id,
                                text='Наш бот умеет отправлять фотографии'
                                )
        await message.delete()


@dp.message_handler(commands=['pic'])
async def send_img(message: types.Message):
    await bot.send_photo(   
                            chat_id=message.chat.id,
                            photo='https://pbs.twimg.com/tweet_video_thumb/EueUPkrWYAIIzj0?format=jpg&name=large',
                            caption='смотри на почиту'
                        )
    await message.delete()

    
@dp.message_handler(content_types=['sticker'])
async def send_img(message: types.Message):
    await bot.send_photo(   
                            chat_id=message.chat.id,
                            photo='https://pbs.twimg.com/tweet_video_thumb/EueUPkrWYAIIzj0?format=jpg&name=large',
                            caption='смотри на почиту'
                        )
    await message.delete()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)
