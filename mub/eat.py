import logging
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.filters import Text
from aiogram.utils import executor
from config import TOKEN_API

#логирование и инициализация
logging.basicConfig(level=logging.INFO)

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

#keyboard 
KEYBOARD = ReplyKeyboardMarkup(resize_keyboard=True)
BUTTONS = [
    KeyboardButton(text='Русская кухня'),
    KeyboardButton(text='Японская кухня'),
    KeyboardButton(text='Итальянская кухня')
]
KEYBOARD.add(*BUTTONS)

#commands

@dp.message_handler(commands=['start'])
async def command_start(message: Message):
    await message.reply("Добрый день! Что бы вы хотели заказать?", reply_markup=KEYBOARD)
    await message.delete()
    
@dp.message_handler(commands=['help'])    
async def command_help(message: Message):
    await message.answer('помощь')


#обработчики 

@dp.message_handler(Text(equals="Итальянская кухня"))
async def process_italian_food(message: Message):
    await message.answer("Вы выбрали Итальянскую кухню. Какое блюдо вы хотите заказать?")

@dp.message_handler(Text(equals="Японская кухня"))
async def process_japanese_food(message: Message):
    await message.answer("Вы выбрали Японскую кухню. Какое блюдо вы хотите заказать?")

@dp.message_handler(Text(equals="Русская кухня"))
async def process_russian_food(message: Message):
    await message.answer("Вы выбрали Русскую кухню. Какое блюдо вы хотите заказать?")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
       
    
  