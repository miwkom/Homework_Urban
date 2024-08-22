from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
import asyncio

api = 'API BOT'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.')
    await message.answer("Введите слово 'Calories' для начала вычисления вашей нормы калорий в день")


class UserStats(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    sex = State()


@dp.message_handler(text='Calories')
async def set_sex(message):
    await message.answer('Введите свой пол(м/ж):')
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
    calories = 10*float(data['weight'])+6.25*float(data['growth'])-5*float(data['age'])+x
    await message.answer(f'Ваша норма калорий: {calories} ккал.')
    await state.finish()


@dp.message_handler()
async def all_messages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
