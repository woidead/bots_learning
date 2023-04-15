from aiogram import Bot, Dispatcher, executor, types
from myconfig import PRAC_TOKEN

bot = Bot(PRAC_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def echo(message: types.Message):
        await message.answer(text=message.text)


async def on_startup(_):
        print('go go go')

         
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)
