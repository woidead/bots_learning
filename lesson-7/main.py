from aiogram import Bot, Dispatcher, executor, types
from myconfig import PRAC_TOKEN

bot = Bot(PRAC_TOKEN)
dp = Dispatcher(bot)
HELP_COMMAND = """
<b>/start</b> - <em>старт</em> 
<b>/help</b> - <em>команды бота</em> 
<b>/pic</b> - <em>пикча</em> 
"""

# @dp.message_handler()
# async def echo(message: types.Message):
#         # await message.answer(text=message.text)
#         await bot.send_message(chat_id=message.chat.id,
#         text="hello!") # туда куда писали в группу или в лс
#         await bot.send_message(chat_id=message.from_user.id,
#         text="hello!") # всегда в лс


@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    try :
        await bot.send_message( 
                            chat_id=message.from_user.id, 
                            text=HELP_COMMAND, 
                            parse_mode="HTML"
                            )
    except:
        await bot.send_message( 
                            chat_id=message.chat.id, 
                            text=HELP_COMMAND, 
                            parse_mode="HTML"
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


@dp.message_handler(commands=['loc'])
async def send_loc(message: types.Message):
    await bot.send_location(
                            chat_id=message.chat.id, 
                            latitude=69,
                            longitude=69)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False) # не брать обновления когда бот отключен
