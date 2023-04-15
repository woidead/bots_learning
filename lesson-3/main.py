from aiogram import Bot, executor, Dispatcher, types
from myconfig import PRAC_TOKEN

bot = Bot(PRAC_TOKEN)
dp = Dispatcher(bot)

HELP_TEXT='''
/help - все команды
/start - начало
все вопросы к @woidead
'''

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.delete()
    await message.answer(text='спасибо за использование бота @woidead')

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply(text=HELP_TEXT)

if __name__ == '__main__':
    executor.start_polling(dp)