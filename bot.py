import logging
import wikipedia
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '1912624006:AAGbxo4NFiUEcKgK01Qe6XBafcZXCgeT4IE'
wikipedia.set_lang('uz')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Wkipedia Uz botiga Xush kelibsiz sizni qiziqtirgan sozni yozing: ")



@dp.message_handler()
async def sendWiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await  message.answer(respond)
    except:
        await message.answer("Bu mavzuga oid malumot topilmadi!!!")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)