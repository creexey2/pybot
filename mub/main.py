import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.filters import Text
from aiogram.utils import executor

# установим уровень логирования
logging.basicConfig(level=logging.INFO)

# инициализируем бота и диспетчер
bot = Bot(token='5531833066:AAFn_cQtg28yhnqMND_GGbH1rAhF4hwp-tc')
dp = Dispatcher(bot)

# клавиатура для выбора кухни
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
buttons = [
    KeyboardButton(text="Итальянская кухня"),
    KeyboardButton(text="Японская кухня"),
    KeyboardButton(text="Русская кухня")
]
keyboard.add(*buttons)

# обработчик команды /start
@dp.message_handler(commands=['start'])
async def process_start_command(message: Message):
    await message.reply("Добрый день! Что бы вы хотели заказать?", reply_markup=keyboard)

# обработчик текстовых сообщений
@dp.message_handler(Text(equals="Итальянская кухня"))
async def process_italian_food(message: Message):
    await message.answer("Вы выбрали Итальянскую кухню. Какое блюдо вы хотите заказать?")

# обработчик текстовых сообщений
@dp.message_handler(Text(equals="Японская кухня"))
async def process_japanese_food(message: Message):
    await message.answer("Вы выбрали Японскую кухню. Какое блюдо вы хотите заказать?")

# обработчик текстовых сообщений
@dp.message_handler(Text(equals="Русская кухня"))
async def process_russian_food(message: Message):
    await message.answer("Вы выбрали Русскую кухню. Какое блюдо вы хотите заказать?")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)



    
    
    
    
#5531833066:AAFn_cQtg28yhnqMND_GGbH1rAhF4hwp-tc