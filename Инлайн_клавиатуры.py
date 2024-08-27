from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

api = 'API BOT'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
button1 = KeyboardButton(text='Рассчитать')
button2 = KeyboardButton(text='Информация')
kb.add(button1)
kb.add(button2)

kb2 = InlineKeyboardMarkup()
button1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kb2.add(button1, button2)


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот для расчета калорий.', reply_markup=kb)


@dp.message_handler(text='Информация')
async def info(message):
    await message.answer('Информация о боте')


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=kb2)


@dp.callback_query_handler(text='formulas')
async def get_formula(call):
    await call.message.answer(f'Формулы расчёта:\n'
                              f'для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5\n'
                              f'для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161')


class UserStats(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    sex = State()


@dp.callback_query_handler(text='calories')
async def set_sex(call):
    await call.message.answer('Введите свой пол(м/ж):')
    await UserStats.sex.set()


@dp.message_handler(state=UserStats.sex)
async def set_age(message, state):
    if message.text == 'м' or message.text == 'ж':
        await state.update_data(sex=message.text)
        await message.answer('Введите свой возраст:')
        await UserStats.age.set()
    else:
        await message.answer('Отправьте м или ж.')
        await set_sex(message)


@dp.message_handler(state=UserStats.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserStats.growth.set()


@dp.message_handler(state=UserStats.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserStats.weight.set()


@dp.message_handler(state=UserStats.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    if data['sex'] == 'м':
        x = 5
    else:
        x = -161
    calories = 10 * float(data['weight']) + 6.25 * float(data['growth']) - 5 * float(data['age']) + x
    await message.answer(f'Ваша норма калорий: {calories} ккал.')
    await state.finish()


@dp.message_handler()
async def all_messages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
