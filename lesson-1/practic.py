from aiogram import Bot, Dispatcher, executor, types
from myconfig import PRAC_TOKEN

bot = Bot(PRAC_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def echo(message: types.Message):
    if len(message.text.split()) > 2: #если больше 2 букв
        mess = message.text.capitalize() #начать с большой буквы каждое сообщение
        await message.answer(text=mess)


if __name__ == '__main__':
    executor.start_polling(dp)
