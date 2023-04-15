from aiogram import Bot, Dispatcher, executor, types
from myconfig import PRAC_TOKEN
import time

bot = Bot(PRAC_TOKEN)
dp = Dispatcher(bot)
HELP_COMMAND = '''
<b>/start</b> - <em>запуск бота</em>
<b>/give</b> - <em>отправляет кота</em>
<b>/help</b> - <em>показывает все команды бота</em>
'''

async def start_up(_):
    print('bot started')

@dp.message_handler(commands=['help'])
async def helpa(message: types.Message):
    await message.reply(text=HELP_COMMAND, parse_mode='HTML')

@dp.message_handler(content_types=['sticker'])
async def sticker_id(message: types.Message):
    await message.answer(message.sticker.file_id)

# @dp.message_handler()
# async def count(message: types.Message):
#     await message.answer(text=message.text.count('📀'))
# @dp.message_handler(commands=['give'])
# async def give(message: types.Message):
#         await message.answer(text='смотри какие котики, прям как мы ❤️')
#         time.sleep(0.5)
#         await bot.send_sticker(chat_id=message.from_user.id, sticker='CAACAgQAAxkBAAEHtsZj6U34U_UsPPhRy2ub1IdDeauyugACphEAAqbxcR6IKKmyNX_aIC4E')


# @dp.message_handler()
# async def give(message: types.Message):
#     if message.text == '❤️':
#         await message.answer(text='🖤')
#     if message.text == 'a':
#         await message.answer(text='sa')

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=start_up)
