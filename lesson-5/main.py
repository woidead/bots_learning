from aiogram import Bot, Dispatcher, executor, types
from myconfig import PRAC_TOKEN

bot = Bot(PRAC_TOKEN)
dp = Dispatcher(bot)

async def on_start_up(_):
    print("бот успешно запущен") #при запуске будет писать что все работает на ура

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    a = message.from_user.first_name
    await message.answer(text=f'welcome {a}')

@dp.message_handler(commands=['stick'])
async def give_command(message: types.Message):
    await bot.send_sticker(message.from_user.id, sticker='CAACAgQAAxkBAAEHtsZj6U34U_UsPPhRy2ub1IdDeauyugACphEAAqbxcR6IKKmyNX_aIC4E')

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_start_up)
