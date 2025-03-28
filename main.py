import logging
import asyncio
import os
import random
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()


logging.basicConfig(level=logging.INFO)

# Знаки зодиака
zodiacs = [
    "♈ Овен", "♉ Телец", "♊ Близнецы", "♋ Рак",
    "♌ Лев", "♍ Дева", "♎ Весы", "♏ Скорпион",
    "♐ Стрелец", "♑ Козерог", "♒ Водолей", "♓ Рыбы"
]

# Общий список гороскопов
common_horoscopes = [
    "Сегодня вас ждёт удача!",
    "Будьте осторожны в финансовых вопросах.",
    "Возможны неожиданные приятные встречи.",
    "Лучший день для новых начинаний!",
    "Слушайте свою интуицию – она вас не подведёт.",
    "Хороший день для отдыха и восстановления сил.",
    "Ваши старания вскоре принесут плоды.",
    "Не бойтесь брать на себя ответственность.",
    "Отличный момент для саморазвития и обучения.",
    "Сегодня вам стоит избегать споров и конфликтов.",
    "Вас ждёт приятный сюрприз!",
    "День подходит для романтики и общения с близкими.",
    "Будьте открыты к новым возможностям.",
    "Сегодня важно сохранять спокойствие и не торопиться.",
    "День принесёт неожиданные повороты судьбы."
]

# Создание клавиатуры
keyboard = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text=zodiac)] for zodiac in zodiacs],
    resize_keyboard=True
)

# Обработчик команды /start
@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Привет! Выбери свой знак зодиака, чтобы получить гороскоп:", reply_markup=keyboard)

# Обработчик выбора знака
@dp.message()
async def zodiac_selected(message: types.Message):
    sign = message.text.strip()
    if sign in zodiacs:
        prediction = random.choice(common_horoscopes)  # Выбираем случайный прогноз
        await message.answer(f"🔮 Гороскоп для {sign}:\n\n{prediction}")
    else:
        await message.answer("Пожалуйста, выбери знак зодиака из списка.")

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())