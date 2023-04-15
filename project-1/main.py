from aiogram import Bot, Dispatcher, executor, types
from myconfig import PRAC_TOKEN
from data import HELP_TEXT, agents
from keyboards import menukeyboard
import random
from random import randint
 
bot = Bot(PRAC_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
        await bot.send_message(chat_id=message.from_user.id,text='Добро пожаловать в нашего бота. если вы не знакомы с функционалом бота - прошу ознакомиться командой /help')

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
       await bot.send_message(message.from_user.id, text=HELP_TEXT)

@dp.message_handler(commands=['description'])
async def description_command(message:types.Message):
       await bot.send_message(message.from_user.id, text='Данный бот сделан @woidead для личного пользования. Коммерческому пользованию не подлежит!! ')


@dp.message_handler(commands=['keyboard'])
async def replykeyboard(message:types.Message):
       await bot.send_message(message.from_user.id, text='Клавиатура снизу',reply_markup=menukeyboard)

@dp.message_handler(commands=['random_agent'])
async def random_agent(message: types.Message):
       random_index = random.choice(list(range(0, len(agents))))
       random_ag = list(agents.values())[random_index]
       await bot.send_photo(message.from_user.id, photo=random_ag, caption=f'тебе выпал {list(agents.keys())[random_index]}',has_spoiler=True,protect_content=True)


async def on_startup(_):
        print('go go go')

         
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
