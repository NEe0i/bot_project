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

# Создание клавиатуры с 12 знаками зодиака
zodiacs = [
    "♈ Овен", "♉ Телец", "♊ Близнецы", "♋ Рак",
    "♌ Лев", "♍ Дева", "♎ Весы", "♏ Скорпион",
    "♐ Стрелец", "♑ Козерог", "♒ Водолей", "♓ Рыбы"
]

# Возможные гороскопы
horoscopes = {
    "♈ Овен": ["Сегодня ваш день! Будьте смелее!", "Избегайте конфликтов, они могут испортить настроение."],
    "♉ Телец": ["Отличное время для новых начинаний!", "Будьте осторожны с финансами сегодня."],
    "♊ Близнецы": ["Не бойтесь проявить инициативу.", "Сегодня возможны неожиданные встречи."],
    "♋ Рак": ["Прислушайтесь к интуиции, она подскажет верное решение.", "Лучше отдохнуть и заняться собой."],
    "♌ Лев": ["Вы в центре внимания! Используйте это себе на пользу.", "Сегодня стоит избегать споров."],
    "♍ Дева": ["Все будет идти по плану, если проявите терпение.", "День удачен для творчества."],
    "♎ Весы": ["Хорошее время для принятия важных решений.", "Порадуйте себя чем-то приятным."],
    "♏ Скорпион": ["Возможны неожиданные повороты судьбы.", "Не торопитесь с выводами, анализируйте ситуацию."],
    "♐ Стрелец": ["Путешествия или новые впечатления принесут радость!", "Отличный день для общения и дружеских встреч."],
    "♑ Козерог": ["Сосредоточьтесь на работе, это принесет плоды.", "Сегодня лучше избегать рисков."],
    "♒ Водолей": ["Будьте открыты к новым возможностям.", "Интуиция поможет принять правильное решение."],
    "♓ Рыбы": ["День благоприятен для романтики и творчества.", "Сегодня важно заботиться о своем здоровье."]
}

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
    if sign in horoscopes:
        prediction = random.choice(horoscopes[sign])  # Берем случайный прогноз
        await message.answer(f"🔮 Гороскоп для {sign}:\n\n{prediction}")
    else:
        await message.answer("Пожалуйста, выбери знак зодиака из списка.")

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())