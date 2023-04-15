from aiogram import Bot, Dispatcher, executor, types
from myconfig import PRAC_TOKEN
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

bot = Bot(PRAC_TOKEN)
dp = Dispatcher(bot)
kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.add(KeyboardButton('/help')).insert(KeyboardButton('/pic')).add(KeyboardButton('❤️'))


HELP_COMMAND = """
<b>/start</b> - <em>старт</em> 
<b>/help</b> - <em>команды бота</em> 
<b>/description</b> - <em>описание</em> 
<b>/pic</b> - <em>пикча</em> 
"""


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
        await bot.send_message( 
                                message.from_user.id, 
                                text="""добро пожаловать в нашего бота
                                        нажми /help для продолжения работы """,
                                reply_markup=kb
                                )


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
        await bot.send_message(
                                message.from_user.id, 
                                text = HELP_COMMAND,
                                parse_mode='HTML'
        )


@dp.message_handler(commands=['pic'])
async def picture(message: types.Message):
        await bot.send_photo(
                                message.from_user.id,
                                photo='https://pbs.twimg.com/tweet_video_thumb/EueUPkrWYAIIzj0?format=jpg&name=large',
                                caption='yo!'      
        )
        await bot.send_message(
                                message.from_user.id,
                                text='hello'
        )


@dp.message_handler()
async def hearth(message: types.Message):
        if message.text == '❤️':
                await bot.send_sticker(
                        message.from_user.id,
                        sticker='CAACAgQAAxkBAAEHz49j8msXdITJc9tV2jWSrVVH8-9mFgACrREAAqbxcR71s3o6qSc2WS4E'
                )

async def on_startup(_):
        print('go go go')

        
if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=False)
