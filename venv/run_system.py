import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
import aiogram.utils.markdown as md
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import State, StatesGroup
from database import cursor, db


logging.basicConfig(level=logging.INFO)
from API import api

bot = Bot(token=api)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

#admin_id = 800703982
admin_id = 0

def check_for_signup():
    column = "SELECT id_telegram FROM registrated_clients"
    cursor.execute(column)
    ids_list = cursor.fetchall()
    ids_int = []
    for tuple in ids_list:
        res = int(''.join(map(str, tuple)))
        ids_int.append(res)

    print(ids_int)
    return ids_int


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    id_p = message.from_user.id
    #print(id_p)

    ids = check_for_signup()

    markup_clients = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup_clients.add("Тіркелу📌")
    await bot.send_message(message.from_user.id,
                           """
                           Қайырлы күн🙂
Бұл Ibincina жеке клиникасына арналған бот🤖
Жалғастыру үшін сізге тіркелу керек📌
                           """,
                           reply_markup=markup_clients)

    for ID in ids:
        if id_p == admin_id:
            markup_admin = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
            markup_admin.add("Клиенттер👥", "Тексерілгендер📍")
            await bot.send_message(message.from_user.id,
                                   "Сіздің статусыңыз Админстратор",
                                   reply_markup=markup_admin)
            break

        elif id_p == ID:
            markup_signup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
            markup_signup.add("Қабылдауға жазылу📝", "Анықтама алу📃")
            await bot.send_message(message.from_user.id,
                                   "Сіз тіркелген аккаунтсыз👥",
                                   reply_markup=markup_signup)
            break
        elif id_p != ID:
            print(id_p)

            data_client_id = id_p
            markup_clients = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
            markup_clients.add("Тіркелу📌")
            await bot.send_message(message.from_user.id,
                                   """
                                   Қайырлы күн🙂
                                   Бұл Ibincina жеке клиникасына арналған бот🤖
                                   Жалғастыру үшін сізге тіркелу керек📌
                                   """,
                                   reply_markup=markup_clients)



from forma import Form
from database import db, cursor
from fetch import fetch

@dp.message_handler(content_types=['text'])
async def text_process(message: types.Message):
    from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
    public_m = message.text
    if public_m == "Тіркелу📌":
        from forma import Form
        # import statement
        await Form.surname_name.set()
        await bot.send_message(message.from_user.id,
                               "Толық аты-жөніңіз ... ?")

    elif public_m == "Қабылдауға жазылу📝":
        markup_doctor = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
        markup_doctor.add("Терапевт🧑🏻‍⚕", "ЛОР🧑🏻‍⚕", "Хирург🧑🏻‍⚕", "Окулист👩🏻‍⚕", "Педиатр👩🏻‍⚕",
                          "Невролог👩🏻‍⚕", "Артқа⬅️")
        await bot.send_message(message.from_user.id,
                               "Сіз тіркелген аккаунтсыз👥",
                               reply_markup=markup_doctor)

    elif public_m == "Терапевт🧑🏻‍⚕":
        time0900 = fetch(time0900='terapeft')
        time1000 = fetch(time1000='terapeft')
        time1100 = fetch(time1100='terapeft')
        time1200 = fetch(time1200='terapeft')
        time1340 = fetch(time1340='terapeft')
        time1440 = fetch(time1440='terapeft')
        time1540 = fetch(time1540='terapeft')
        time1640 = fetch(time1640='terapeft')
        time1740 = fetch(time1740='terapeft')


        if time0900 == 1:
            inline0900 = InlineKeyboardButton('09:00', callback_data='terapeft0900')
            inline9 = InlineKeyboardMarkup().add(inline0900)
            await bot.send_message(message.from_user.id,
                                   'Өзіңізге ыңғайлы уақытты таңдаңыз🙃',
                                   reply_markup=inline9)

        if time1000 == 1:
            inline1000 = InlineKeyboardButton('10:00', callback_data='terapeft1000')
            inline10 = InlineKeyboardMarkup().add(inline1000)

            await bot.send_message(message.from_user.id,
                                   'Өзіңізге ыңғайлы уақытты таңдаңыз🙃',
                                   reply_markup=inline10)

        if time1100 == 1:
            inline1100 = InlineKeyboardButton('11:00', callback_data='terapeft1100')
            inline11 = InlineKeyboardMarkup().add(inline1100)
            await bot.send_message(message.from_user.id,
                                   'Өзіңізге ыңғайлы уақытты таңдаңыз🙃',
                                   reply_markup=inline11)
        if time1200 == 1:
            inline1200 = InlineKeyboardButton('12:00', callback_data='terapeft1200')
            inline12 = InlineKeyboardMarkup().add(inline1200)
            await bot.send_message(message.from_user.id,
                                   'Өзіңізге ыңғайлы уақытты таңдаңыз🙃',
                                   reply_markup=inline12)

        if time1340 == 1:
            inline1340 = InlineKeyboardButton('13:40', callback_data='terapeft1340')
            inline13 = InlineKeyboardMarkup().add(inline1340)
            await bot.send_message(message.from_user.id,
                                   'Өзіңізге ыңғайлы уақытты таңдаңыз🙃',
                                   reply_markup=inline13)
        if time1440 == 1:
            inline1440 = InlineKeyboardButton('14:40', callback_data='terapeft1440')
            inline14 = InlineKeyboardMarkup().add(inline1440)
            await bot.send_message(message.from_user.id,
                                   'Өзіңізге ыңғайлы уақытты таңдаңыз🙃',
                                   reply_markup=inline14)

        if time1540 == 1:
            inline1540 = InlineKeyboardButton('15:40', callback_data='terapeft1540')
            inline15 = InlineKeyboardMarkup().add(inline1540)
            await bot.send_message(message.from_user.id,
                                   'Өзіңізге ыңғайлы уақытты таңдаңыз🙃',
                                   reply_markup=inline15)
        if time1640 == 1:
            inline1640 = InlineKeyboardButton('16:40', callback_data='terapeft1640')
            inline16 = InlineKeyboardMarkup().add(inline1640)
            await bot.send_message(message.from_user.id,
                                   'Өзіңізге ыңғайлы уақытты таңдаңыз🙃',
                                   reply_markup=inline16)
        if time1740 == 1:
            inline1740 = InlineKeyboardButton('17:40', callback_data='terapeft1740')
            inline17 = InlineKeyboardMarkup().add(inline1740)
            await bot.send_message(message.from_user.id,
                                   'Өзіңізге ыңғайлы уақытты таңдаңыз🙃',
                                   reply_markup=inline17)

    elif public_m == "ЛОР🧑🏻‍⚕":
        time0900 = fetch(time0900='lor')
        time1000 = fetch(time1000='lor')
        time1100 = fetch(time1100='lor')
        time1200 = fetch(time1200='lor')
        time1340 = fetch(time1340='lor')
        time1440 = fetch(time1440='lor')
        time1540 = fetch(time1540='lor')
        time1640 = fetch(time1640='lor')
        time1740 = fetch(time1740='lor')

        if time0900 == 1:
            inline0900 = InlineKeyboardButton('09:00', callback_data='lor0900')
            inline9 = InlineKeyboardMarkup().add(inline0900)
            await bot.send_message(message.from_user.id,
                                   'Өзіңізге ыңғайлы уақытты таңдаңыз🙃',
                                   reply_markup=inline9)

        if time1000 == 1:
            inline1000 = InlineKeyboardButton('10:00', callback_data='lor1000')
            inline10 = InlineKeyboardMarkup().add(inline1000)

            await bot.send_message(message.from_user.id,
                                   'Өзіңізге ыңғайлы уақытты таңдаңыз🙃',
                                   reply_markup=inline10)

        if time1100 == 1:
            inline1100 = InlineKeyboardButton('11:00', callback_data='lor1100')
            inline11 = InlineKeyboardMarkup().add(inline1100)
            await bot.send_message(message.from_user.id,
                                   'Өзіңізге ыңғайлы уақытты таңдаңыз🙃',
                                   reply_markup=inline11)
        if time1200 == 1:
            inline1200 = InlineKeyboardButton('12:00', callback_data='lor1200')
            inline12 = InlineKeyboardMarkup().add(inline1200)
            await bot.send_message(message.from_user.id,
                                   'Өзіңізге ыңғайлы уақытты таңдаңыз🙃',
                                   reply_markup=inline12)

        if time1340 == 1:
            inline1340 = InlineKeyboardButton('13:40', callback_data='lor1340')
            inline13 = InlineKeyboardMarkup().add(inline1340)
            await bot.send_message(message.from_user.id,
                                   'Өзіңізге ыңғайлы уақытты таңдаңыз🙃',
                                   reply_markup=inline13)
        if time1440 == 1:
            inline1440 = InlineKeyboardButton('14:40', callback_data='lor1440')
            inline14 = InlineKeyboardMarkup().add(inline1440)
            await bot.send_message(message.from_user.id,
                                   'Өзіңізге ыңғайлы уақытты таңдаңыз🙃',
                                   reply_markup=inline14)

        if time1540 == 1:
            inline1540 = InlineKeyboardButton('15:40', callback_data='lor1540')
            inline15 = InlineKeyboardMarkup().add(inline1540)
            await bot.send_message(message.from_user.id,
                                   'Өзіңізге ыңғайлы уақытты таңдаңыз🙃',
                                   reply_markup=inline15)
        if time1640 == 1:
            inline1640 = InlineKeyboardButton('16:40', callback_data='lor1640')
            inline16 = InlineKeyboardMarkup().add(inline1640)
            await bot.send_message(message.from_user.id,
                                   'Өзіңізге ыңғайлы уақытты таңдаңыз🙃',
                                   reply_markup=inline16)
        if time1740 == 1:
            inline1740 = InlineKeyboardButton('17:40', callback_data='lor1740')
            inline17 = InlineKeyboardMarkup().add(inline1740)
            await bot.send_message(message.from_user.id,
                                   'Өзіңізге ыңғайлы уақытты таңдаңыз🙃',
                                   reply_markup=inline17)
        else:
            await bot.send_message(message.from_user.id,
                                   'Өкінішке орай😐 бүгін дәрігер👨🏽‍⚕ бос емес, ертең көріңіз😉')

    elif public_m == "Хирург🧑🏻‍⚕":
        time0900 = fetch(time0900='hirurg')
        time1000 = fetch(time1000='hirurg')
        time1100 = fetch(time1100='hirurg')
        time1200 = fetch(time1200='hirurg')
        time1340 = fetch(time1340='hirurg')
        time1440 = fetch(time1440='hirurg')
        time1540 = fetch(time1540='hirurg')
        time1640 = fetch(time1640='hirurg')
        time1740 = fetch(time1740='hirurg')

        if time0900 == 1:
            inline0900 = InlineKeyboardButton('09:00', callback_data='hirurg0900')
            inline9 = InlineKeyboardMarkup().add(inline0900)
            await bot.send_message(message.from_user.id,
                                   'Өзіңізге ыңғайлы уақытты таңдаңыз🙃',
                                   reply_markup=inline9)

        if time1000 == 1:
            inline1000 = InlineKeyboardButton('10:00', callback_data='hirurg1000')
            inline10 = InlineKeyboardMarkup().add(inline1000)

            await bot.send_message(message.from_user.id,
                                   'Өзіңізге ыңғайлы уақытты таңдаңыз🙃',
                                   reply_markup=inline10)

        if time1100 == 1:
            inline1100 = InlineKeyboardButton('11:00', callback_data='hirurg1100')
            inline11 = InlineKeyboardMarkup().add(inline1100)
            await bot.send_message(message.from_user.id,
                                   'Өзіңізге ыңғайлы уақытты таңдаңыз🙃',
                                   reply_markup=inline11)
        if time1200 == 1:
            inline1200 = InlineKeyboardButton('12:00', callback_data='hirurg1200')
            inline12 = InlineKeyboardMarkup().add(inline1200)
            await bot.send_message(message.from_user.id,
                                   'Өзіңізге ыңғайлы уақытты таңдаңыз🙃',
                                   reply_markup=inline12)

        if time1340 == 1:
            inline1340 = InlineKeyboardButton('13:40', callback_data='hirurg1340')
            inline13 = InlineKeyboardMarkup().add(inline1340)
            await bot.send_message(message.from_user.id,
                                   'Өзіңізге ыңғайлы уақытты таңдаңыз🙃',
                                   reply_markup=inline13)
        if time1440 == 1:
            inline1440 = InlineKeyboardButton('14:40', callback_data='hirurg1440')
            inline14 = InlineKeyboardMarkup().add(inline1440)
            await bot.send_message(message.from_user.id,
                                   'Өзіңізге ыңғайлы уақытты таңдаңыз🙃',
                                   reply_markup=inline14)

        if time1540 == 1:
            inline1540 = InlineKeyboardButton('15:40', callback_data='hirurg1540')
            inline15 = InlineKeyboardMarkup().add(inline1540)
            await bot.send_message(message.from_user.id,
                                   'Өзіңізге ыңғайлы уақытты таңдаңыз🙃',
                                   reply_markup=inline15)
        if time1640 == 1:
            inline1640 = InlineKeyboardButton('16:40', callback_data='hirurg1640')
            inline16 = InlineKeyboardMarkup().add(inline1640)
            await bot.send_message(message.from_user.id,
                                   'Өзіңізге ыңғайлы уақытты таңдаңыз🙃',
                                   reply_markup=inline16)
        if time1740 == 1:
            inline1740 = InlineKeyboardButton('17:40', callback_data='hirurg1740')
            inline17 = InlineKeyboardMarkup().add(inline1740)
            await bot.send_message(message.from_user.id,
                                   'Өзіңізге ыңғайлы уақытты таңдаңыз🙃',
                                   reply_markup=inline17)
        else:
            await bot.send_message(message.from_user.id,
                                   'Өкінішке орай😐 бүгін дәрігер👨🏽‍⚕ бос емес, ертең көріңіз😉')

    elif public_m == "Окулист👩🏻‍⚕":
        time0900 = fetch(time0900='oculist')
        time1000 = fetch(time1000='oculist')
        time1100 = fetch(time1100='oculist')
        time1200 = fetch(time1200='oculist')
        time1340 = fetch(time1340='oculist')
        time1440 = fetch(time1440='oculist')
        time1540 = fetch(time1540='oculist')
        time1640 = fetch(time1640='oculist')
        time1740 = fetch(time1740='oculist')

        if time0900 == 1:
            inline0900 = InlineKeyboardButton('09:00', callback_data='oculist0900')
            inline9 = InlineKeyboardMarkup().add(inline0900)
            await bot.send_message(message.from_user.id,
                                   'Өзіңізге ыңғайлы уақытты таңдаңыз🙃',
                                   reply_markup=inline9)

        if time1000 == 1:
            inline1000 = InlineKeyboardButton('10:00', callback_data='oculist1000')
            inline10 = InlineKeyboardMarkup().add(inline1000)

            await bot.send_message(message.from_user.id,
                                   'Өзіңізге ыңғайлы уақытты таңдаңыз🙃',
                                   reply_markup=inline10)

        if time1100 == 1:
            inline1100 = InlineKeyboardButton('11:00', callback_data='oculist1100')
            inline11 = InlineKeyboardMarkup().add(inline1100)
            await bot.send_message(message.from_user.id,
                                   'Өзіңізге ыңғайлы уақытты таңдаңыз🙃',
                                   reply_markup=inline11)
        if time1200 == 1:
            inline1200 = InlineKeyboardButton('12:00', callback_data='oculist1200')
            inline12 = InlineKeyboardMarkup().add(inline1200)
            await bot.send_message(message.from_user.id,
                                   'Өзіңізге ыңғайлы уақытты таңдаңыз🙃',
                                   reply_markup=inline12)

        if time1340 == 1:
            inline1340 = InlineKeyboardButton('13:40', callback_data='oculist1340')
            inline13 = InlineKeyboardMarkup().add(inline1340)
            await bot.send_message(message.from_user.id,
                                   'Өзіңізге ыңғайлы уақытты таңдаңыз🙃',
                                   reply_markup=inline13)
        if time1440 == 1:
            inline1440 = InlineKeyboardButton('14:40', callback_data='oculist1440')
            inline14 = InlineKeyboardMarkup().add(inline1440)
            await bot.send_message(message.from_user.id,
                                   'Өзіңізге ыңғайлы уақытты таңдаңыз🙃',
                                   reply_markup=inline14)

        if time1540 == 1:
            inline1540 = InlineKeyboardButton('15:40', callback_data='oculist1540')
            inline15 = InlineKeyboardMarkup().add(inline1540)
            await bot.send_message(message.from_user.id,
                                   'Өзіңізге ыңғайлы уақытты таңдаңыз🙃',
                                   reply_markup=inline15)
        if time1640 == 1:
            inline1640 = InlineKeyboardButton('16:40', callback_data='oculist1640')
            inline16 = InlineKeyboardMarkup().add(inline1640)
            await bot.send_message(message.from_user.id,
                                   'Өзіңізге ыңғайлы уақытты таңдаңыз🙃',
                                   reply_markup=inline16)
        if time1740 == 1:
            inline1740 = InlineKeyboardButton('17:40', callback_data='oculist1740')
            inline17 = InlineKeyboardMarkup().add(inline1740)
            await bot.send_message(message.from_user.id,
                                   'Өзіңізге ыңғайлы уақытты таңдаңыз🙃',
                                   reply_markup=inline17)
        else:
            await bot.send_message(message.from_user.id,
                                   'Өкінішке орай😐 бүгін дәрігер👨🏽‍⚕ бос емес, ертең көріңіз😉')

    elif public_m == "Педиатр👩🏻‍⚕":
        time0900 = fetch(time0900='pediatr')
        time1000 = fetch(time1000='pediatr')
        time1100 = fetch(time1100='pediatr')
        time1200 = fetch(time1200='pediatr')
        time1340 = fetch(time1340='pediatr')
        time1440 = fetch(time1440='pediatr')
        time1540 = fetch(time1540='pediatr')
        time1640 = fetch(time1640='pediatr')
        time1740 = fetch(time1740='pediatr')

        if time0900 == 1:
            inline0900 = InlineKeyboardButton('09:00', callback_data='pediatr0900')
            inline9 = InlineKeyboardMarkup().add(inline0900)
            await bot.send_message(message.from_user.id,
                                   'Өзіңізге ыңғайлы уақытты таңдаңыз🙃',
                                   reply_markup=inline9)

        if time1000 == 1:
            inline1000 = InlineKeyboardButton('10:00', callback_data='pediatr1000')
            inline10 = InlineKeyboardMarkup().add(inline1000)

            await bot.send_message(message.from_user.id,
                                   'Өзіңізге ыңғайлы уақытты таңдаңыз🙃',
                                   reply_markup=inline10)

        if time1100 == 1:
            inline1100 = InlineKeyboardButton('11:00', callback_data='pediatr1100')
            inline11 = InlineKeyboardMarkup().add(inline1100)
            await bot.send_message(message.from_user.id,
                                   'Өзіңізге ыңғайлы уақытты таңдаңыз🙃',
                                   reply_markup=inline11)
        if time1200 == 1:
            inline1200 = InlineKeyboardButton('12:00', callback_data='pediatr1200')
            inline12 = InlineKeyboardMarkup().add(inline1200)
            await bot.send_message(message.from_user.id,
                                   'Өзіңізге ыңғайлы уақытты таңдаңыз🙃',
                                   reply_markup=inline12)

        if time1340 == 1:
            inline1340 = InlineKeyboardButton('13:40', callback_data='pediatr1340')
            inline13 = InlineKeyboardMarkup().add(inline1340)
            await bot.send_message(message.from_user.id,
                                   'Өзіңізге ыңғайлы уақытты таңдаңыз🙃',
                                   reply_markup=inline13)
        if time1440 == 1:
            inline1440 = InlineKeyboardButton('14:40', callback_data='pediatr1440')
            inline14 = InlineKeyboardMarkup().add(inline1440)
            await bot.send_message(message.from_user.id,
                                   'Өзіңізге ыңғайлы уақытты таңдаңыз🙃',
                                   reply_markup=inline14)

        if time1540 == 1:
            inline1540 = InlineKeyboardButton('15:40', callback_data='pediatr1540')
            inline15 = InlineKeyboardMarkup().add(inline1540)
            await bot.send_message(message.from_user.id,
                                   'Өзіңізге ыңғайлы уақытты таңдаңыз🙃',
                                   reply_markup=inline15)
        if time1640 == 1:
            inline1640 = InlineKeyboardButton('16:40', callback_data='pediatr1640')
            inline16 = InlineKeyboardMarkup().add(inline1640)
            await bot.send_message(message.from_user.id,
                                   'Өзіңізге ыңғайлы уақытты таңдаңыз🙃',
                                   reply_markup=inline16)
        if time1740 == 1:
            inline1740 = InlineKeyboardButton('17:40', callback_data='pediatr1740')
            inline17 = InlineKeyboardMarkup().add(inline1740)
            await bot.send_message(message.from_user.id,
                                   'Өзіңізге ыңғайлы уақытты таңдаңыз🙃',
                                   reply_markup=inline17)
        else:
            await bot.send_message(message.from_user.id,
                                   'Өкінішке орай😐 бүгін дәрігер👨🏽‍⚕ бос емес, ертең көріңіз😉')

    elif public_m == "Невролог👩🏻‍⚕":
        time0900 = fetch(time0900='nevrolog')
        time1000 = fetch(time1000='nevrolog')
        time1100 = fetch(time1100='nevrolog')
        time1200 = fetch(time1200='nevrolog')
        time1340 = fetch(time1340='nevrolog')
        time1440 = fetch(time1440='nevrolog')
        time1540 = fetch(time1540='nevrolog')
        time1640 = fetch(time1640='nevrolog')
        time1740 = fetch(time1740='nevrolog')

        if time0900 == 1:
            inline0900 = InlineKeyboardButton('09:00', callback_data='nevrolog0900')
            inline9 = InlineKeyboardMarkup().add(inline0900)
            await bot.send_message(message.from_user.id,
                                   'Өзіңізге ыңғайлы уақытты таңдаңыз🙃',
                                   reply_markup=inline9)

        if time1000 == 1:
            inline1000 = InlineKeyboardButton('10:00', callback_data='nevrolog1000')
            inline10 = InlineKeyboardMarkup().add(inline1000)

            await bot.send_message(message.from_user.id,
                                   'Өзіңізге ыңғайлы уақытты таңдаңыз🙃',
                                   reply_markup=inline10)

        if time1100 == 1:
            inline1100 = InlineKeyboardButton('11:00', callback_data='nevrolog1100')
            inline11 = InlineKeyboardMarkup().add(inline1100)
            await bot.send_message(message.from_user.id,
                                   'Өзіңізге ыңғайлы уақытты таңдаңыз🙃',
                                   reply_markup=inline11)
        if time1200 == 1:
            inline1200 = InlineKeyboardButton('12:00', callback_data='nevrolog1200')
            inline12 = InlineKeyboardMarkup().add(inline1200)
            await bot.send_message(message.from_user.id,
                                   'Өзіңізге ыңғайлы уақытты таңдаңыз🙃',
                                   reply_markup=inline12)

        if time1340 == 1:
            inline1340 = InlineKeyboardButton('13:40', callback_data='nevrolog1340')
            inline13 = InlineKeyboardMarkup().add(inline1340)
            await bot.send_message(message.from_user.id,
                                   'Өзіңізге ыңғайлы уақытты таңдаңыз🙃',
                                   reply_markup=inline13)
        if time1440 == 1:
            inline1440 = InlineKeyboardButton('14:40', callback_data='nevrolog1440')
            inline14 = InlineKeyboardMarkup().add(inline1440)
            await bot.send_message(message.from_user.id,
                                   'Өзіңізге ыңғайлы уақытты таңдаңыз🙃',
                                   reply_markup=inline14)

        if time1540 == 1:
            inline1540 = InlineKeyboardButton('15:40', callback_data='nevrolog1540')
            inline15 = InlineKeyboardMarkup().add(inline1540)
            await bot.send_message(message.from_user.id,
                                   'Өзіңізге ыңғайлы уақытты таңдаңыз🙃',
                                   reply_markup=inline15)
        if time1640 == 1:
            inline1640 = InlineKeyboardButton('16:40', callback_data='nevrolog1640')
            inline16 = InlineKeyboardMarkup().add(inline1640)
            await bot.send_message(message.from_user.id,
                                   'Өзіңізге ыңғайлы уақытты таңдаңыз🙃',
                                   reply_markup=inline16)
        if time1740 == 1:
            inline1740 = InlineKeyboardButton('17:40', callback_data='nevrolog1740')
            inline17 = InlineKeyboardMarkup().add(inline1740)
            await bot.send_message(message.from_user.id,
                                   'Өзіңізге ыңғайлы уақытты таңдаңыз🙃',
                                   reply_markup=inline17)
        else:
            await bot.send_message(message.from_user.id,
                                   'Өкінішке орай😐 бүгін дәрігер👨🏽‍⚕ бос емес, ертең көріңіз😉')


    elif public_m == "Анықтама алу📃":
        from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

        inline_sport = InlineKeyboardButton('Спорт секция🏃🏻', callback_data='sport')
        inline_086 = InlineKeyboardButton('Форма 0-86📃', callback_data='forma086')
        inline_job = InlineKeyboardButton('Жұмысқа💼', callback_data='job')
        inline_spavka = InlineKeyboardMarkup(row_width=2).add(inline_sport,
                                                              inline_086,
                                                              inline_job)
        await bot.send_message(message.from_user.id,
                               text='Қандай анықтама📃?',
                               reply_markup=inline_spavka)

    elif public_m == "Артқа⬅️":
        markup_signup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
        markup_signup.add("Қабылдауға жазылу📝", "Анықтама алу📃")
        await bot.send_message(message.from_user.id,
                               "Бастапқы мәзір",
                               reply_markup=markup_signup)


    elif public_m == "Клиенттер👥":
        from make_excell import make_excell_file
        name_ = "clients_who_regis"
        table_name_ = "registrated_clients"
        make_excell_file(name_, table_name_)
        name_file = open('{}.xlsx'.format(name_), 'rb').read()

        await bot.send_document(message.from_user.id, name_file)

    elif public_m == "Тексерілгендер📍":
        from make_excell import make_excell_file
        name_ = "clients_who_check_analyze"
        table_name_ = "analyze_results"
        make_excell_file(name_, table_name_)
        name_file = open('{}.xlsx'.format(name_), 'rb').read()

        await bot.send_document(message.from_user.id, name_file)

    else:
        markup_signup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
        markup_signup.add("Қабылдауға жазылу📝", "Анықтама алу📃")
        await bot.send_message(message.from_user.id,
                               "Сіз тіркелген аккаунтсыз👥",
                               reply_markup=markup_signup)


from forma import Form
@dp.message_handler(state='*', commands='Бас тарту🙌🏻')
@dp.message_handler(Text(equals='Бас тарту🙌🏻', ignore_case=True), state='*')
async def cancell_handler(message: types.Message, state: FSMContext):
    """
    :param message: Бастартылды
    :param state: Тоқтату
    :return: finish

    """

    current_state = await state.get_state()
    if current_state is None:
        return

    logging.info('Бас тарту!')
    await state.finish()
    await message.reply('Бастартылды.', reply_markup=types.ReplyKeyboardMarkup())


@dp.message_handler(state=Form.surname_name)
async def full_name(message: types.Message, state: FSMContext):
    """
    Толық аты-жөн ...
    """

    await Form.next()
    global data_client_id
    global surname
    async with state.proxy() as data:
        data['surname_name'] = message.text
        surname = data['surname_name']

    markup_cancel = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup_cancel.add("Бас тарту🙌🏻")
    client_id = message.from_user.id
    data_client_id = client_id
    await bot.send_message(message.from_user.id,
                           "Жасыңыз?(Тек қана санмен жазыңыз!)",
                           reply_markup=markup_cancel)




@dp.message_handler(lambda message: not message.text.isdigit(), state=Form.age)
async def procces_age_invalid(message: types.Message):
    """
    Сан болмаса!
    """
    return await message.reply("Сандармен жазу керек.\nЖасыңыз?")


@dp.message_handler(lambda message: message.text.isdigit(), state=Form.age)
async def procces_age(message: types.Message, state: FSMContext):
    await Form.next()
    await state.update_data(age=int(message.text))
    global ages
    async with state.proxy() as data:
        data['age'] = int(message.text)
        ages = data['age']

    markup_sex = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup_sex.add("Ер🤵🏽", "Әйел👩🏻‍💼")
    markup_sex.add("Бас тарту🙌🏻")

    await message.reply("Жынысыңыз👥?",
                        reply_markup=markup_sex)


@dp.message_handler(lambda message: message.text not in ["Ер🤵🏽", "Әйел👩🏻‍💼"], state=Form.gender)
async def procces_gender_invalid(message: types.Message):
    return await message.reply("Дұрыс жынысыңызды белгілеңіз!")


@dp.message_handler(lambda message: message.text in ["Ер🤵🏽", "Әйел👩🏻‍💼"], state=Form.gender)
async def procces_gender(message: types.Message, state: FSMContext):
    await Form.next()
    global Gender
    async  with state.proxy() as data:
        data['gender'] = message.text
        Gender = data['gender']
    markup_blood = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup_blood.add("I", "II", "III", "IV")
    markup_blood.add("Бас тарту🙌🏻")
    await message.reply("Қан тобыңыз?",
                        reply_markup=markup_blood)


@dp.message_handler(lambda message: message.text not in ["I", "II", "III", "IV"], state=Form.which_blood)
async def procces_blood_invalid(message: types.Message):
    return await message.reply("Қан тобын дұрыстап белгілеңіз!")


@dp.message_handler(state=Form.which_blood)
async def procces_blood(message: types.Message, state: FSMContext):
    await Form.next()
    global WHICH_BLOOD
    async  with state.proxy() as data:
        data['which_blood'] = message.text
        WHICH_BLOOD = data['which_blood']

    markup_number = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup_number.add("Бас тарту🙌🏻")
    await message.reply("Телефон номеріңіз?",
                        reply_markup=markup_number)


@dp.message_handler(lambda message: not message.text.isdigit(), state=Form.tele_number)
async def failed(message: types.Message):
    return message.reply("Телефон номерді сандармен жазыңыз!")


@dp.message_handler(lambda message: message.text.isdigit(), state=Form.tele_number)
async def procces_blood_type(message: types.Message, state: FSMContext):
    await state.update_data(tele_number=int(message.text))
    global number
    async with state.proxy() as data:
        data['tele_number'] = message.text
        number = data['tele_number']

    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    from database import db, cursor
    cursor.execute("""
                                   INSERT INTO registrated_clients(
                                                    id_telegram,
                                                    first_last_name,
                                                    age,
                                                    gender,
                                                    blood_type,
                                                    number,
                                                    proverka  
                                   ) VALUES(?,?,?,?,?,?,?) """, (str(data_client_id), str(surname),
                                                                 str(ages), str(Gender),
                                                                 str(WHICH_BLOOD), str(number),
                                                                 "false"))
    db.commit()

    await bot.send_message(
        message.chat.id,
        md.text(
            md.text('Сіз тіркелдіңіз📍,', md.bold(data['surname_name'])),
            md.text('Жасыңыз:', md.code(data['age'])),
            md.text('Жынысыңыз👥:', data['gender']),
            md.text('Қан тобы', data['which_blood']),
            md.text('Телефон номеріңіз', data['tele_number']),
            sep='\n',
        ),
        reply_markup=markup,
        parse_mode=ParseMode.MARKDOWN
    )

    await state.finish()

from forma import spravka_sport, spravka_086, spravka_job
@dp.message_handler(lambda message: not message.text.isdigit(), state=spravka_sport.inn)
async def failed_inn(message: types.Message):
    return message.reply("ЖСН-ді сандармен жазыңыз!")


@dp.message_handler(lambda message: message.text.isdigit(), state=spravka_sport.inn)
async def procces_waiting(message: types.Message, state: FSMContext):
    await spravka_sport.next()
    await state.update_data(inn=int(message.text))
    global inn_
    async with state.proxy() as data:
        data['inn'] = message.text
        inn_ = data['inn']

    markup_bron = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup_bron.add("Иә⏩", "Бас тарту🙌🏻")
    await message.reply("Анықтама алу📃",
                        reply_markup=markup_bron)

@dp.message_handler(state=spravka_sport.yes)
async def process_yes(message: types.Message, state: FSMContext):
    id_cl = message.from_user.id
    async  with state.proxy() as data:
        data['yes'] = message.text

    cursor.execute("""
                   INSERT INTO sport_spravka(
                                                    inn,
                                                    t 
                                   ) VALUES(?, ?) """, (str(inn_), 0)
                   )
    db.commit()
    markup_signup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup_signup.add("Қабылдауға жазылу📝", "Анықтама алу📃")
    await bot.send_message(message.from_user.id,
                           'Анықтама алуға өтінішіңіз қабылданды📃👍🏻,кері байланысты күтіңіз📞',
                           reply_markup=markup_signup)
    await state.finish()

#########################################################################################
@dp.message_handler(lambda message: not message.text.isdigit(), state=spravka_086.inn)
async def failed_inn(message: types.Message):
    return message.reply("ЖСН-ді сандармен жазыңыз!")


@dp.message_handler(lambda message: message.text.isdigit(), state=spravka_086.inn)
async def procces_sp(message: types.Message, state: FSMContext):
    await spravka_086.next()
    await state.update_data(inn=int(message.text))
    global inn_
    async  with state.proxy() as data:
        data['inn'] = message.text
        inn_ = data['inn']

    markup_bron = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup_bron.add("Иә⏩", "Бас тарту🙌🏻")
    await message.reply("Анықтама алу📃",
                        reply_markup=markup_bron)


@dp.message_handler(state=spravka_086.yes)
async def process_yes(message: types.Message, state: FSMContext):
    id_cl = message.from_user.id
    async  with state.proxy() as data:
        data['yes'] = message.text

    cursor.execute("""
                   INSERT INTO sport_086(
                                                    inn,
                                                    t 
                                   ) VALUES(?, ?) """, (str(inn_), 0)
                   )
    db.commit()

    markup_signup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup_signup.add("Қабылдауға жазылу📝", "Анықтама алу📃")
    await bot.send_message(message.from_user.id,
                           'Анықтама алуға өтінішіңіз қабылданды📃👍🏻,кері байланысты күтіңіз📞',
                           reply_markup=markup_signup)
    await state.finish()
#######################################################################################
@dp.message_handler(lambda message: not message.text.isdigit(), state=spravka_job.inn)
async def failed_inn(message: types.Message):
    return message.reply("ЖСН-ді сандармен жазыңыз!")


@dp.message_handler(lambda message: message.text.isdigit(), state=spravka_job.inn)
async def procces_sp(message: types.Message, state: FSMContext):
    await spravka_job.next()
    await state.update_data(inn=int(message.text))
    global inn_
    async  with state.proxy() as data:
        data['inn'] = message.text
        inn_ = data['inn']

    markup_bron = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup_bron.add("Иә⏩", "Бас тарту🙌🏻")
    await message.reply("Анықтама алу📃",
                        reply_markup=markup_bron)


@dp.message_handler(state=spravka_job.yes)
async def process_yes(message: types.Message, state: FSMContext):
    id_cl = message.from_user.id
    async  with state.proxy() as data:
        data['yes'] = message.text

    cursor.execute("""
                   INSERT INTO sport_job(
                                                    inn,
                                                    t 
                                   ) VALUES(?, ?) """, (str(inn_), 0)
                   )
    db.commit()

    markup_signup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup_signup.add("Қабылдауға жазылу📝", "Анықтама алу📃")
    await bot.send_message(message.from_user.id,
                           'Анықтама алуға өтінішіңіз қабылданды📃👍🏻,кері байланысты күтіңіз📞',
                           reply_markup=markup_signup)
    await state.finish()


@dp.callback_query_handler(text='terapeft0900')
@dp.callback_query_handler(text='terapeft1000')
@dp.callback_query_handler(text='terapeft1100')
@dp.callback_query_handler(text='terapeft1200')
@dp.callback_query_handler(text='terapeft1340')
@dp.callback_query_handler(text='terapeft1440')
@dp.callback_query_handler(text='terapeft1540')
@dp.callback_query_handler(text='terapeft1640')
@dp.callback_query_handler(text='terapeft1740')

@dp.callback_query_handler(text='lor0900')
@dp.callback_query_handler(text='lor1000')
@dp.callback_query_handler(text='lor1100')
@dp.callback_query_handler(text='lor1200')
@dp.callback_query_handler(text='lor1340')
@dp.callback_query_handler(text='lor1440')
@dp.callback_query_handler(text='lor1540')
@dp.callback_query_handler(text='lor1640')
@dp.callback_query_handler(text='lor1740')

@dp.callback_query_handler(text='hirurg0900')
@dp.callback_query_handler(text='hirurg1000')
@dp.callback_query_handler(text='hirurg1100')
@dp.callback_query_handler(text='hirurg1200')
@dp.callback_query_handler(text='hirurg1340')
@dp.callback_query_handler(text='hirurg1440')
@dp.callback_query_handler(text='hirurg1540')
@dp.callback_query_handler(text='hirurg1640')
@dp.callback_query_handler(text='hirurg1740')

@dp.callback_query_handler(text='oculist0900')
@dp.callback_query_handler(text='oculist1000')
@dp.callback_query_handler(text='oculist1100')
@dp.callback_query_handler(text='oculist1200')
@dp.callback_query_handler(text='oculist1340')
@dp.callback_query_handler(text='oculist1440')
@dp.callback_query_handler(text='oculist1540')
@dp.callback_query_handler(text='oculist1640')
@dp.callback_query_handler(text='oculist1740')

@dp.callback_query_handler(text='pediatr0900')
@dp.callback_query_handler(text='pediatr1000')
@dp.callback_query_handler(text='pediatr1100')
@dp.callback_query_handler(text='pediatr1200')
@dp.callback_query_handler(text='pediatr1340')
@dp.callback_query_handler(text='pediatr1440')
@dp.callback_query_handler(text='pediatr1540')
@dp.callback_query_handler(text='pediatr1640')
@dp.callback_query_handler(text='pediatr1740')

@dp.callback_query_handler(text='nevrolog0900')
@dp.callback_query_handler(text='nevrolog1000')
@dp.callback_query_handler(text='nevrolog1100')
@dp.callback_query_handler(text='nevrolog1200')
@dp.callback_query_handler(text='nevrolog1340')
@dp.callback_query_handler(text='nevrolog1440')
@dp.callback_query_handler(text='nevrolog1540')
@dp.callback_query_handler(text='nevrolog1640')
@dp.callback_query_handler(text='nevrolog1740')

@dp.callback_query_handler(text='sport')
@dp.callback_query_handler(text='forma086')
@dp.callback_query_handler(text='job')
async def callback_procces(query: types.CallbackQuery):
    answer_data = query.data
    global times
    if answer_data == 'sport':
        from forma import spravka_sport
        await spravka_sport.inn.set()
        await bot.send_message(query.from_user.id, text="ЖСН енгізіңіз ...")

    elif answer_data == 'forma086':
        from forma import spravka_086
        await spravka_086.inn.set()
        await bot.send_message(query.from_user.id, text="ЖСН енгізіңіз ...")

    elif answer_data == 'job':
        from forma import spravka_job
        await spravka_job.inn.set()
        await bot.send_message(query.from_user.id, text="ЖСН енгізіңіз ...")

    elif answer_data == 'terapeft0900':
        id = query.from_user.id
        #print(id)
        t = '09:00'
        cu = "SELECT first_last_name FROM registrated_clients WHERE id_telegram = ?"
        cursor.execute(cu, (id,))
        c = cursor.fetchone()
        fio = ''
        for i in c:
            #print(i)
            fio = i
        insert_data = """
                      INSERT INTO waiting(
                               id_telegram,
                               inn,
                               type_doctor,
                               time,
                               t) VALUES(?,?,?,?,?)
                      """
        cursor.execute(insert_data, (str(id), str(fio), "terapeft", str(t), 0,))
        update_data = """
                      UPDATE terapeft set time0900 = ?
                      """
        cursor.execute(update_data, (0,))
        db.commit()
        await bot.send_message(query.from_user.id, 'Сіз таңдалған уақытқа жазылдыңыз🙃, кешікпей келіңіз😉, қабылдау уақыты 40 минут⏱')

    elif answer_data == 'terapeft1000':
        t = '10:00'
        id = query.from_user.id
        #print(id)
        cu = "SELECT first_last_name FROM registrated_clients WHERE id_telegram = ?"
        cursor.execute(cu, (id,))
        c = cursor.fetchone()
        fio = ''
        for i in c:
            #print(i)
            fio = i
        insert_data = """
                              INSERT INTO waiting(
                                       id_telegram,
                                       inn,
                                       type_doctor,
                                       time,
                                       t) VALUES(?,?,?,?,?)
                              """
        cursor.execute(insert_data, (str(id), str(fio), "terapeft", str(t), 0,))
        update_data = """
                              UPDATE terapeft set time1000 = ?
                              """
        cursor.execute(update_data, (0,))
        db.commit()
        await bot.send_message(query.from_user.id,
                               'Сіз таңдалған уақытқа жазылдыңыз🙃, кешікпей келіңіз😉, қабылдау уақыты 40 минут⏱')

    elif answer_data == 'terapeft1100':
        t = '11:00'
        id = query.from_user.id
        #print(id)
        cu = "SELECT first_last_name FROM registrated_clients WHERE id_telegram = ?"
        cursor.execute(cu, (id,))
        c = cursor.fetchone()
        fio = ''
        for i in c:
            #print(i)
            fio = i
        insert_data = """
                                      INSERT INTO waiting(
                                               id_telegram,
                                               inn,
                                               type_doctor,
                                               time,
                                               t) VALUES(?,?,?,?,?)
                                      """
        cursor.execute(insert_data, (str(id), str(fio), "terapeft", str(t), 0,))
        update_data = """
                                      UPDATE terapeft set time1100 = ?
                                      """
        cursor.execute(update_data, (0,))
        db.commit()
        await bot.send_message(query.from_user.id,
                               'Сіз таңдалған уақытқа жазылдыңыз🙃, кешікпей келіңіз😉, қабылдау уақыты 40 минут⏱')

    elif answer_data == 'terapeft1200':
        t = '12:00'
        id = query.from_user.id
        #print(id)
        cu = "SELECT first_last_name FROM registrated_clients WHERE id_telegram = ?"
        cursor.execute(cu, (id,))
        c = cursor.fetchone()
        fio = ''
        for i in c:
            #print(i)
            fio = i
        insert_data = """
                                              INSERT INTO waiting(
                                                       id_telegram,
                                                       inn,
                                                       type_doctor,
                                                       time,
                                                       t) VALUES(?,?,?,?,?)
                                              """
        cursor.execute(insert_data, (str(id), str(fio), "terapeft", str(t), 0,))
        update_data = """
                                              UPDATE terapeft set time1200 = ?
                                              """
        cursor.execute(update_data, (0,))
        db.commit()
        await bot.send_message(query.from_user.id,
                               'Сіз таңдалған уақытқа жазылдыңыз🙃, кешікпей келіңіз😉, қабылдау уақыты 40 минут⏱')

    elif answer_data == 'terapeft1340':
        t = '13:40'
        id = query.from_user.id
        #print(id)
        cu = "SELECT first_last_name FROM registrated_clients WHERE id_telegram = ?"
        cursor.execute(cu, (id,))
        c = cursor.fetchone()
        fio = ''
        for i in c:
            #print(i)
            fio = i
        insert_data = """
                                                      INSERT INTO waiting(
                                                               id_telegram,
                                                               inn,
                                                               type_doctor,
                                                               time,
                                                               t) VALUES(?,?,?,?,?)
                                                      """
        cursor.execute(insert_data, (str(id), str(fio), "terapeft", str(t), 0,))
        update_data = """
                                                      UPDATE terapeft set time1340 = ?
                                                      """
        cursor.execute(update_data, (0,))
        db.commit()
        await bot.send_message(query.from_user.id,
                               'Сіз таңдалған уақытқа жазылдыңыз🙃, кешікпей келіңіз😉, қабылдау уақыты 40 минут⏱')

    elif answer_data == 'terapeft1440':

        t = '14:40'
        id = query.from_user.id
        #print(id)
        cu = "SELECT first_last_name FROM registrated_clients WHERE id_telegram = ?"
        cursor.execute(cu, (id,))
        c = cursor.fetchone()
        fio = ''
        for i in c:
            #print(i)
            fio = i
        insert_data = """
                                                              INSERT INTO waiting(
                                                                       id_telegram,
                                                                       inn,
                                                                       type_doctor,
                                                                       time,
                                                                       t) VALUES(?,?,?,?,?)
                                                              """
        cursor.execute(insert_data, (str(id), str(fio), "terapeft", str(t), 0,))
        update_data = """
                                                              UPDATE terapeft set time1440 = ?
                                                              """
        cursor.execute(update_data, (0,))
        db.commit()
        await bot.send_message(query.from_user.id,
                               'Сіз таңдалған уақытқа жазылдыңыз🙃, кешікпей келіңіз😉, қабылдау уақыты 40 минут⏱')

    elif answer_data == 'terapeft1540':

        t = '15:40'
        id = query.from_user.id
        #print(id)
        cu = "SELECT first_last_name FROM registrated_clients WHERE id_telegram = ?"
        cursor.execute(cu, (id,))
        c = cursor.fetchone()
        fio = ''
        for i in c:
            #print(i)
            fio = i
        insert_data = """
                                                                      INSERT INTO waiting(
                                                                               id_telegram,
                                                                               inn,
                                                                               type_doctor,
                                                                               time,
                                                                               t) VALUES(?,?,?,?,?)
                                                                      """
        cursor.execute(insert_data, (str(id), str(fio), "terapeft", str(t), 0,))
        update_data = """
                                                                      UPDATE terapeft set time1540 = ?
                                                                      """
        cursor.execute(update_data, (0,))
        db.commit()
        await bot.send_message(query.from_user.id,
                               'Сіз таңдалған уақытқа жазылдыңыз🙃, кешікпей келіңіз😉, қабылдау уақыты 40 минут⏱')

    elif answer_data == 'terapeft1640':

        t = '16:40'
        id = query.from_user.id
        #print(id)
        cu = "SELECT first_last_name FROM registrated_clients WHERE id_telegram = ?"
        cursor.execute(cu, (id,))
        c = cursor.fetchone()
        fio = ''
        for i in c:
            #print(i)
            fio = i
        insert_data = """
                                                                              INSERT INTO waiting(
                                                                                       id_telegram,
                                                                                       inn,
                                                                                       type_doctor,
                                                                                       time,
                                                                                       t) VALUES(?,?,?,?,?)
                                                                              """
        cursor.execute(insert_data, (str(id), str(fio), "terapeft", str(t), 0,))
        update_data = """
                                                                              UPDATE terapeft set time1640 = ?
                                                                              """
        cursor.execute(update_data, (0,))
        db.commit()
        await bot.send_message(query.from_user.id,
                               'Сіз таңдалған уақытқа жазылдыңыз🙃, кешікпей келіңіз😉, қабылдау уақыты 40 минут⏱')

    elif answer_data == 'terapeft1740':

        t = '17:40'
        id = query.from_user.id
        #print(id)
        cu = "SELECT first_last_name FROM registrated_clients WHERE id_telegram = ?"
        cursor.execute(cu, (id,))
        c = cursor.fetchone()
        fio = ''
        for i in c:
            #print(i)
            fio = i
        insert_data = """
                                                                                      INSERT INTO waiting(
                                                                                               id_telegram,
                                                                                               inn,
                                                                                               type_doctor,
                                                                                               time,
                                                                                               t) VALUES(?,?,?,?,?)
                                                                                      """
        cursor.execute(insert_data, (str(id), str(fio), "terapeft", str(t), 0,))
        update_data = """
                                                                                      UPDATE terapeft set time1740 = ?
                                                                                      """
        cursor.execute(update_data, (0,))
        db.commit()
        await bot.send_message(query.from_user.id,
                               'Сіз таңдалған уақытқа жазылдыңыз🙃, кешікпей келіңіз😉, қабылдау уақыты 40 минут⏱')

    #####################
    elif answer_data == 'lor0900':
        id = query.from_user.id
        #print(id)
        t = '09:00'
        cu = "SELECT first_last_name FROM registrated_clients WHERE id_telegram = ?"
        cursor.execute(cu, (id,))
        c = cursor.fetchone()
        fio = ''
        for i in c:
            #print(i)
            fio = i
        insert_data = """
                      INSERT INTO waiting(
                               id_telegram,
                               inn,
                               type_doctor,
                               time,
                               t) VALUES(?,?,?,?,?)
                      """
        cursor.execute(insert_data, (str(id), str(fio), "lor", str(t), 0,))
        update_data = """
                      UPDATE lor set time0900 = ?
                      """
        cursor.execute(update_data, (0,))
        db.commit()
        await bot.send_message(query.from_user.id, 'Сіз таңдалған уақытқа жазылдыңыз🙃, кешікпей келіңіз😉, қабылдау уақыты 40 минут⏱')

    elif answer_data == 'lor1000':
        t = '10:00'
        id = query.from_user.id
        #print(id)
        cu = "SELECT first_last_name FROM registrated_clients WHERE id_telegram = ?"
        cursor.execute(cu, (id,))
        c = cursor.fetchone()
        fio = ''
        for i in c:
            #print(i)
            fio = i
        insert_data = """
                              INSERT INTO waiting(
                                       id_telegram,
                                       inn,
                                       type_doctor,
                                       time,
                                       t) VALUES(?,?,?,?,?)
                              """
        cursor.execute(insert_data, (str(id), str(fio), "lor", str(t), 0,))
        update_data = """
                              UPDATE lor set time1000 = ?
                              """
        cursor.execute(update_data, (0,))
        db.commit()
        await bot.send_message(query.from_user.id,
                               'Сіз таңдалған уақытқа жазылдыңыз🙃, кешікпей келіңіз😉, қабылдау уақыты 40 минут⏱')

    elif answer_data == 'lor1100':
        t = '11:00'
        id = query.from_user.id
        #print(id)
        cu = "SELECT first_last_name FROM registrated_clients WHERE id_telegram = ?"
        cursor.execute(cu, (id,))
        c = cursor.fetchone()
        fio = ''
        for i in c:
            #print(i)
            fio = i
        insert_data = """
                                      INSERT INTO waiting(
                                               id_telegram,
                                               inn,
                                               type_doctor,
                                               time,
                                               t) VALUES(?,?,?,?,?)
                                      """
        cursor.execute(insert_data, (str(id), str(fio), "lor", str(t), 0,))
        update_data = """
                                      UPDATE lor set time1100 = ?
                                      """
        cursor.execute(update_data, (0,))
        db.commit()
        await bot.send_message(query.from_user.id,
                               'Сіз таңдалған уақытқа жазылдыңыз🙃, кешікпей келіңіз😉, қабылдау уақыты 40 минут⏱')

    elif answer_data == 'lor1200':
        t = '12:00'
        id = query.from_user.id
        #print(id)
        cu = "SELECT first_last_name FROM registrated_clients WHERE id_telegram = ?"
        cursor.execute(cu, (id,))
        c = cursor.fetchone()
        fio = ''
        for i in c:
            #print(i)
            fio = i
        insert_data = """
                                              INSERT INTO waiting(
                                                       id_telegram,
                                                       inn,
                                                       type_doctor,
                                                       time,
                                                       t) VALUES(?,?,?,?,?)
                                              """
        cursor.execute(insert_data, (str(id), str(fio), "lor", str(t), 0,))
        update_data = """
                                              UPDATE lor set time1200 = ?
                                              """
        cursor.execute(update_data, (0,))
        db.commit()
        await bot.send_message(query.from_user.id,
                               'Сіз таңдалған уақытқа жазылдыңыз🙃, кешікпей келіңіз😉, қабылдау уақыты 40 минут⏱')

    elif answer_data == 'lor1340':
        t = '13:40'
        id = query.from_user.id
        #print(id)
        cu = "SELECT first_last_name FROM registrated_clients WHERE id_telegram = ?"
        cursor.execute(cu, (id,))
        c = cursor.fetchone()
        fio = ''
        for i in c:
            #print(i)
            fio = i
        insert_data = """
                                                      INSERT INTO waiting(
                                                               id_telegram,
                                                               inn,
                                                               type_doctor,
                                                               time,
                                                               t) VALUES(?,?,?,?,?)
                                                      """
        cursor.execute(insert_data, (str(id), str(fio), "lor", str(t), 0,))
        update_data = """
                                                      UPDATE lor set time1340 = ?
                                                      """
        cursor.execute(update_data, (0,))
        db.commit()
        await bot.send_message(query.from_user.id,
                               'Сіз таңдалған уақытқа жазылдыңыз🙃, кешікпей келіңіз😉, қабылдау уақыты 40 минут⏱')

    elif answer_data == 'lor1440':

        t = '14:40'
        id = query.from_user.id
        #print(id)
        cu = "SELECT first_last_name FROM registrated_clients WHERE id_telegram = ?"
        cursor.execute(cu, (id,))
        c = cursor.fetchone()
        fio = ''
        for i in c:
            #print(i)
            fio = i
        insert_data = """
                                                              INSERT INTO waiting(
                                                                       id_telegram,
                                                                       inn,
                                                                       type_doctor,
                                                                       time,
                                                                       t) VALUES(?,?,?,?,?)
                                                              """
        cursor.execute(insert_data, (str(id), str(fio), "lor", str(t), 0,))
        update_data = """
                                                              UPDATE lor set time1440 = ?
                                                              """
        cursor.execute(update_data, (0,))
        db.commit()
        await bot.send_message(query.from_user.id,
                               'Сіз таңдалған уақытқа жазылдыңыз🙃, кешікпей келіңіз😉, қабылдау уақыты 40 минут⏱')

    elif answer_data == 'lor1540':

        t = '15:40'
        id = query.from_user.id
        #print(id)
        cu = "SELECT first_last_name FROM registrated_clients WHERE id_telegram = ?"
        cursor.execute(cu, (id,))
        c = cursor.fetchone()
        fio = ''
        for i in c:
            #print(i)
            fio = i
        insert_data = """
                                                                      INSERT INTO waiting(
                                                                               id_telegram,
                                                                               inn,
                                                                               type_doctor,
                                                                               time,
                                                                               t) VALUES(?,?,?,?,?)
                                                                      """
        cursor.execute(insert_data, (str(id), str(fio), "lor", str(t), 0,))
        update_data = """
                                                                      UPDATE lor set time1540 = ?
                                                                      """
        cursor.execute(update_data, (0,))
        db.commit()
        await bot.send_message(query.from_user.id,
                               'Сіз таңдалған уақытқа жазылдыңыз🙃, кешікпей келіңіз😉, қабылдау уақыты 40 минут⏱')

    elif answer_data == 'lor1640':

        t = '16:40'
        id = query.from_user.id
        #print(id)
        cu = "SELECT first_last_name FROM registrated_clients WHERE id_telegram = ?"
        cursor.execute(cu, (id,))
        c = cursor.fetchone()
        fio = ''
        for i in c:
            #print(i)
            fio = i
        insert_data = """
                                                                              INSERT INTO waiting(
                                                                                       id_telegram,
                                                                                       inn,
                                                                                       type_doctor,
                                                                                       time,
                                                                                       t) VALUES(?,?,?,?,?)
                                                                              """
        cursor.execute(insert_data, (str(id), str(fio), "lor", str(t), 0,))
        update_data = """
                                                                              UPDATE lor set time1640 = ?
                                                                              """
        cursor.execute(update_data, (0,))
        db.commit()
        await bot.send_message(query.from_user.id,
                               'Сіз таңдалған уақытқа жазылдыңыз🙃, кешікпей келіңіз😉, қабылдау уақыты 40 минут⏱')

    elif answer_data == 'lor1740':

        t = '17:40'
        id = query.from_user.id
        #print(id)
        cu = "SELECT first_last_name FROM registrated_clients WHERE id_telegram = ?"
        cursor.execute(cu, (id,))
        c = cursor.fetchone()
        fio = ''
        for i in c:
            #print(i)
            fio = i
        insert_data = """
                                                                                      INSERT INTO waiting(
                                                                                               id_telegram,
                                                                                               inn,
                                                                                               type_doctor,
                                                                                               time,
                                                                                               t) VALUES(?,?,?,?,?)
                                                                                      """
        cursor.execute(insert_data, (str(id), str(fio), "lor", str(t), 0,))
        update_data = """
                                                                                      UPDATE lor set time1740 = ?
                                                                                      """
        cursor.execute(update_data, (0,))
        db.commit()
        await bot.send_message(query.from_user.id,
                               'Сіз таңдалған уақытқа жазылдыңыз🙃, кешікпей келіңіз😉, қабылдау уақыты 40 минут⏱')

    #############################
    elif answer_data == 'hirurg0900':
        id = query.from_user.id
        #print(id)
        t = '09:00'
        cu = "SELECT first_last_name FROM registrated_clients WHERE id_telegram = ?"
        cursor.execute(cu, (id,))
        c = cursor.fetchone()
        fio = ''
        for i in c:
            #print(i)
            fio = i
        insert_data = """
                      INSERT INTO waiting(
                               id_telegram,
                               inn,
                               type_doctor,
                               time,
                               t) VALUES(?,?,?,?,?)
                      """
        cursor.execute(insert_data, (str(id), str(fio), "hirurg", str(t), 0,))
        update_data = """
                      UPDATE hirurg set time0900 = ?
                      """
        cursor.execute(update_data, (0,))
        db.commit()
        await bot.send_message(query.from_user.id, 'Сіз таңдалған уақытқа жазылдыңыз🙃, кешікпей келіңіз😉, қабылдау уақыты 40 минут⏱')

    elif answer_data == 'hirurg1000':
        t = '10:00'
        id = query.from_user.id
        #print(id)
        cu = "SELECT first_last_name FROM registrated_clients WHERE id_telegram = ?"
        cursor.execute(cu, (id,))
        c = cursor.fetchone()
        fio = ''
        for i in c:
            #print(i)
            fio = i
        insert_data = """
                              INSERT INTO waiting(
                                       id_telegram,
                                       inn,
                                       type_doctor,
                                       time,
                                       t) VALUES(?,?,?,?,?)
                              """
        cursor.execute(insert_data, (str(id), str(fio), "hirurg", str(t), 0,))
        update_data = """
                              UPDATE hirurg set time1000 = ?
                              """
        cursor.execute(update_data, (0,))
        db.commit()
        await bot.send_message(query.from_user.id,
                               'Сіз таңдалған уақытқа жазылдыңыз🙃, кешікпей келіңіз😉, қабылдау уақыты 40 минут⏱')

    elif answer_data == 'hirurg1100':
        t = '11:00'
        id = query.from_user.id
        #print(id)
        cu = "SELECT first_last_name FROM registrated_clients WHERE id_telegram = ?"
        cursor.execute(cu, (id,))
        c = cursor.fetchone()
        fio = ''
        for i in c:
            #print(i)
            fio = i
        insert_data = """
                                      INSERT INTO waiting(
                                               id_telegram,
                                               inn,
                                               type_doctor,
                                               time,
                                               t) VALUES(?,?,?,?,?)
                                      """
        cursor.execute(insert_data, (str(id), str(fio), "hirurg", str(t), 0,))
        update_data = """
                                      UPDATE hirurg set time1100 = ?
                                      """
        cursor.execute(update_data, (0,))
        db.commit()
        await bot.send_message(query.from_user.id,
                               'Сіз таңдалған уақытқа жазылдыңыз🙃, кешікпей келіңіз😉, қабылдау уақыты 40 минут⏱')

    elif answer_data == 'hirurg1200':
        t = '12:00'
        id = query.from_user.id
        #print(id)
        cu = "SELECT first_last_name FROM registrated_clients WHERE id_telegram = ?"
        cursor.execute(cu, (id,))
        c = cursor.fetchone()
        fio = ''
        for i in c:
            #print(i)
            fio = i
        insert_data = """
                                              INSERT INTO waiting(
                                                       id_telegram,
                                                       inn,
                                                       type_doctor,
                                                       time,
                                                       t) VALUES(?,?,?,?,?)
                                              """
        cursor.execute(insert_data, (str(id), str(fio), "hirurg", str(t), 0,))
        update_data = """
                                              UPDATE hirurg set time1200 = ?
                                              """
        cursor.execute(update_data, (0,))
        db.commit()
        await bot.send_message(query.from_user.id,
                               'Сіз таңдалған уақытқа жазылдыңыз🙃, кешікпей келіңіз😉, қабылдау уақыты 40 минут⏱')

    elif answer_data == 'hirurg1340':
        t = '13:40'
        id = query.from_user.id
        #print(id)
        cu = "SELECT first_last_name FROM registrated_clients WHERE id_telegram = ?"
        cursor.execute(cu, (id,))
        c = cursor.fetchone()
        fio = ''
        for i in c:
            #print(i)
            fio = i
        insert_data = """
                                                      INSERT INTO waiting(
                                                               id_telegram,
                                                               inn,
                                                               type_doctor,
                                                               time,
                                                               t) VALUES(?,?,?,?,?)
                                                      """
        cursor.execute(insert_data, (str(id), str(fio), "hirurg", str(t), 0,))
        update_data = """
                                                      UPDATE hirurg set time1340 = ?
                                                      """
        cursor.execute(update_data, (0,))
        db.commit()
        await bot.send_message(query.from_user.id,
                               'Сіз таңдалған уақытқа жазылдыңыз🙃, кешікпей келіңіз😉, қабылдау уақыты 40 минут⏱')

    elif answer_data == 'hirurg1440':

        t = '14:40'
        id = query.from_user.id
        #print(id)
        cu = "SELECT first_last_name FROM registrated_clients WHERE id_telegram = ?"
        cursor.execute(cu, (id,))
        c = cursor.fetchone()
        fio = ''
        for i in c:
            #print(i)
            fio = i
        insert_data = """
                                                              INSERT INTO waiting(
                                                                       id_telegram,
                                                                       inn,
                                                                       type_doctor,
                                                                       time,
                                                                       t) VALUES(?,?,?,?,?)
                                                              """
        cursor.execute(insert_data, (str(id), str(fio), "hirurg", str(t), 0,))
        update_data = """
                                                              UPDATE hirurg set time1440 = ?
                                                              """
        cursor.execute(update_data, (0,))
        db.commit()
        await bot.send_message(query.from_user.id,
                               'Сіз таңдалған уақытқа жазылдыңыз🙃, кешікпей келіңіз😉, қабылдау уақыты 40 минут⏱')

    elif answer_data == 'hirurg1540':

        t = '15:40'
        id = query.from_user.id
        #print(id)
        cu = "SELECT first_last_name FROM registrated_clients WHERE id_telegram = ?"
        cursor.execute(cu, (id,))
        c = cursor.fetchone()
        fio = ''
        for i in c:
            #print(i)
            fio = i
        insert_data = """
                                                                      INSERT INTO waiting(
                                                                               id_telegram,
                                                                               inn,
                                                                               type_doctor,
                                                                               time,
                                                                               t) VALUES(?,?,?,?,?)
                                                                      """
        cursor.execute(insert_data, (str(id), str(fio), "hirurg", str(t), 0,))
        update_data = """
                                                                      UPDATE hirurg set time1540 = ?
                                                                      """
        cursor.execute(update_data, (0,))
        db.commit()
        await bot.send_message(query.from_user.id,
                               'Сіз таңдалған уақытқа жазылдыңыз🙃, кешікпей келіңіз😉, қабылдау уақыты 40 минут⏱')

    elif answer_data == 'hirurg1640':

        t = '16:40'
        id = query.from_user.id
        #print(id)
        cu = "SELECT first_last_name FROM registrated_clients WHERE id_telegram = ?"
        cursor.execute(cu, (id,))
        c = cursor.fetchone()
        fio = ''
        for i in c:
            #print(i)
            fio = i
        insert_data = """
                                                                              INSERT INTO waiting(
                                                                                       id_telegram,
                                                                                       inn,
                                                                                       type_doctor,
                                                                                       time,
                                                                                       t) VALUES(?,?,?,?,?)
                                                                              """
        cursor.execute(insert_data, (str(id), str(fio), "hirurg", str(t), 0,))
        update_data = """
                                                                              UPDATE hirurg set time1640 = ?
                                                                              """
        cursor.execute(update_data, (0,))
        db.commit()
        await bot.send_message(query.from_user.id,
                               'Сіз таңдалған уақытқа жазылдыңыз🙃, кешікпей келіңіз😉, қабылдау уақыты 40 минут⏱')

    elif answer_data == 'hirurg1740':

        t = '17:40'
        id = query.from_user.id
        #print(id)
        cu = "SELECT first_last_name FROM registrated_clients WHERE id_telegram = ?"
        cursor.execute(cu, (id,))
        c = cursor.fetchone()
        fio = ''
        for i in c:
            #print(i)
            fio = i
        insert_data = """
                                                                                      INSERT INTO waiting(
                                                                                               id_telegram,
                                                                                               inn,
                                                                                               type_doctor,
                                                                                               time,
                                                                                               t) VALUES(?,?,?,?,?)
                                                                                      """
        cursor.execute(insert_data, (str(id), str(fio), "hirurg", str(t), 0,))
        update_data = """
                                                                                      UPDATE hirurg set time1740 = ?
                                                                                      """
        cursor.execute(update_data, (0,))
        db.commit()
        await bot.send_message(query.from_user.id,
                               'Сіз таңдалған уақытқа жазылдыңыз🙃, кешікпей келіңіз😉, қабылдау уақыты 40 минут⏱')

    #############################
    elif answer_data == 'oculist0900':
        id = query.from_user.id
        #print(id)
        t = '09:00'
        cu = "SELECT first_last_name FROM registrated_clients WHERE id_telegram = ?"
        cursor.execute(cu, (id,))
        c = cursor.fetchone()
        fio = ''
        for i in c:
            #print(i)
            fio = i
        insert_data = """
                      INSERT INTO waiting(
                               id_telegram,
                               inn,
                               type_doctor,
                               time,
                               t) VALUES(?,?,?,?,?)
                      """
        cursor.execute(insert_data, (str(id), str(fio), "oculist", str(t), 0,))
        update_data = """
                      UPDATE oculist set time0900 = ?
                      """
        cursor.execute(update_data, (0,))
        db.commit()
        await bot.send_message(query.from_user.id, 'Сіз таңдалған уақытқа жазылдыңыз🙃, кешікпей келіңіз😉, қабылдау уақыты 40 минут⏱')

    elif answer_data == 'oculist1000':
        t = '10:00'
        id = query.from_user.id
        #print(id)
        cu = "SELECT first_last_name FROM registrated_clients WHERE id_telegram = ?"
        cursor.execute(cu, (id,))
        c = cursor.fetchone()
        fio = ''
        for i in c:
            #print(i)
            fio = i
        insert_data = """
                              INSERT INTO waiting(
                                       id_telegram,
                                       inn,
                                       type_doctor,
                                       time,
                                       t) VALUES(?,?,?,?,?)
                              """
        cursor.execute(insert_data, (str(id), str(fio), "oculist", str(t), 0,))
        update_data = """
                              UPDATE oculist set time1000 = ?
                              """
        cursor.execute(update_data, (0,))
        db.commit()
        await bot.send_message(query.from_user.id,
                               'Сіз таңдалған уақытқа жазылдыңыз🙃, кешікпей келіңіз😉, қабылдау уақыты 40 минут⏱')

    elif answer_data == 'oculist1100':
        t = '11:00'
        id = query.from_user.id
        #print(id)
        cu = "SELECT first_last_name FROM registrated_clients WHERE id_telegram = ?"
        cursor.execute(cu, (id,))
        c = cursor.fetchone()
        fio = ''
        for i in c:
            #print(i)
            fio = i
        insert_data = """
                                      INSERT INTO waiting(
                                               id_telegram,
                                               inn,
                                               type_doctor,
                                               time,
                                               t) VALUES(?,?,?,?,?)
                                      """
        cursor.execute(insert_data, (str(id), str(fio), "oculist", str(t), 0,))
        update_data = """
                                      UPDATE oculist set time1100 = ?
                                      """
        cursor.execute(update_data, (0,))
        db.commit()
        await bot.send_message(query.from_user.id,
                               'Сіз таңдалған уақытқа жазылдыңыз🙃, кешікпей келіңіз😉, қабылдау уақыты 40 минут⏱')

    elif answer_data == 'oculist1200':
        t = '12:00'
        id = query.from_user.id
        #print(id)
        cu = "SELECT first_last_name FROM registrated_clients WHERE id_telegram = ?"
        cursor.execute(cu, (id,))
        c = cursor.fetchone()
        fio = ''
        for i in c:
            #print(i)
            fio = i
        insert_data = """
                                              INSERT INTO waiting(
                                                       id_telegram,
                                                       inn,
                                                       type_doctor,
                                                       time,
                                                       t) VALUES(?,?,?,?,?)
                                              """
        cursor.execute(insert_data, (str(id), str(fio), "oculist", str(t), 0,))
        update_data = """
                                              UPDATE oculist set time1200 = ?
                                              """
        cursor.execute(update_data, (0,))
        db.commit()
        await bot.send_message(query.from_user.id,
                               'Сіз таңдалған уақытқа жазылдыңыз🙃, кешікпей келіңіз😉, қабылдау уақыты 40 минут⏱')

    elif answer_data == 'oculist1340':
        t = '13:40'
        id = query.from_user.id
        #print(id)
        cu = "SELECT first_last_name FROM registrated_clients WHERE id_telegram = ?"
        cursor.execute(cu, (id,))
        c = cursor.fetchone()
        fio = ''
        for i in c:
            #print(i)
            fio = i
        insert_data = """
                                                      INSERT INTO waiting(
                                                               id_telegram,
                                                               inn,
                                                               type_doctor,
                                                               time,
                                                               t) VALUES(?,?,?,?,?)
                                                      """
        cursor.execute(insert_data, (str(id), str(fio), "oculist", str(t), 0,))
        update_data = """
                                                      UPDATE oculist set time1340 = ?
                                                      """
        cursor.execute(update_data, (0,))
        db.commit()
        await bot.send_message(query.from_user.id,
                               'Сіз таңдалған уақытқа жазылдыңыз🙃, кешікпей келіңіз😉, қабылдау уақыты 40 минут⏱')

    elif answer_data == 'oculist1440':

        t = '14:40'
        id = query.from_user.id
        #print(id)
        cu = "SELECT first_last_name FROM registrated_clients WHERE id_telegram = ?"
        cursor.execute(cu, (id,))
        c = cursor.fetchone()
        fio = ''
        for i in c:
            #print(i)
            fio = i
        insert_data = """
                                                              INSERT INTO waiting(
                                                                       id_telegram,
                                                                       inn,
                                                                       type_doctor,
                                                                       time,
                                                                       t) VALUES(?,?,?,?,?)
                                                              """
        cursor.execute(insert_data, (str(id), str(fio), "oculist", str(t), 0,))
        update_data = """
                                                              UPDATE oculist set time1440 = ?
                                                              """
        cursor.execute(update_data, (0,))
        db.commit()
        await bot.send_message(query.from_user.id,
                               'Сіз таңдалған уақытқа жазылдыңыз🙃, кешікпей келіңіз😉, қабылдау уақыты 40 минут⏱')

    elif answer_data == 'oculist1540':

        t = '15:40'
        id = query.from_user.id
        #print(id)
        cu = "SELECT first_last_name FROM registrated_clients WHERE id_telegram = ?"
        cursor.execute(cu, (id,))
        c = cursor.fetchone()
        fio = ''
        for i in c:
            #print(i)
            fio = i
        insert_data = """
                                                                      INSERT INTO waiting(
                                                                               id_telegram,
                                                                               inn,
                                                                               type_doctor,
                                                                               time,
                                                                               t) VALUES(?,?,?,?,?)
                                                                      """
        cursor.execute(insert_data, (str(id), str(fio), "oculist", str(t), 0,))
        update_data = """
                                                                      UPDATE oculist set time1540 = ?
                                                                      """
        cursor.execute(update_data, (0,))
        db.commit()
        await bot.send_message(query.from_user.id,
                               'Сіз таңдалған уақытқа жазылдыңыз🙃, кешікпей келіңіз😉, қабылдау уақыты 40 минут⏱')

    elif answer_data == 'oculist1640':

        t = '16:40'
        id = query.from_user.id
        #print(id)
        cu = "SELECT first_last_name FROM registrated_clients WHERE id_telegram = ?"
        cursor.execute(cu, (id,))
        c = cursor.fetchone()
        fio = ''
        for i in c:
            #print(i)
            fio = i
        insert_data = """
                                                                              INSERT INTO waiting(
                                                                                       id_telegram,
                                                                                       inn,
                                                                                       type_doctor,
                                                                                       time,
                                                                                       t) VALUES(?,?,?,?,?)
                                                                              """
        cursor.execute(insert_data, (str(id), str(fio), "oculist", str(t), 0,))
        update_data = """
                                                                              UPDATE oculist set time1640 = ?
                                                                              """
        cursor.execute(update_data, (0,))
        db.commit()
        await bot.send_message(query.from_user.id,
                               'Сіз таңдалған уақытқа жазылдыңыз🙃, кешікпей келіңіз😉, қабылдау уақыты 40 минут⏱')

    elif answer_data == 'oculist1740':

        t = '17:40'
        id = query.from_user.id
        #print(id)
        cu = "SELECT first_last_name FROM registrated_clients WHERE id_telegram = ?"
        cursor.execute(cu, (id,))
        c = cursor.fetchone()
        fio = ''
        for i in c:
            #print(i)
            fio = i
        insert_data = """
                                                                                      INSERT INTO waiting(
                                                                                               id_telegram,
                                                                                               inn,
                                                                                               type_doctor,
                                                                                               time,
                                                                                               t) VALUES(?,?,?,?,?)
                                                                                      """
        cursor.execute(insert_data, (str(id), str(fio), "oculist", str(t), 0,))
        update_data = """
                                                                                      UPDATE oculist set time1740 = ?
                                                                                      """
        cursor.execute(update_data, (0,))
        db.commit()
        await bot.send_message(query.from_user.id,
                               'Сіз таңдалған уақытқа жазылдыңыз🙃, кешікпей келіңіз😉, қабылдау уақыты 40 минут⏱')

    #############################

    elif answer_data == 'pediatr0900':
        id = query.from_user.id
        #print(id)
        t = '09:00'
        cu = "SELECT first_last_name FROM registrated_clients WHERE id_telegram = ?"
        cursor.execute(cu, (id,))
        c = cursor.fetchone()
        fio = ''
        for i in c:
            #print(i)
            fio = i
        insert_data = """
                      INSERT INTO waiting(
                               id_telegram,
                               inn,
                               type_doctor,
                               time,
                               t) VALUES(?,?,?,?,?)
                      """
        cursor.execute(insert_data, (str(id), str(fio), "pediatr", str(t), 0,))
        update_data = """
                      UPDATE pediatr set time0900 = ?
                      """
        cursor.execute(update_data, (0,))
        db.commit()
        await bot.send_message(query.from_user.id, 'Сіз таңдалған уақытқа жазылдыңыз🙃, кешікпей келіңіз😉, қабылдау уақыты 40 минут⏱')

    elif answer_data == 'pediatr1000':
        t = '10:00'
        id = query.from_user.id
        #print(id)
        cu = "SELECT first_last_name FROM registrated_clients WHERE id_telegram = ?"
        cursor.execute(cu, (id,))
        c = cursor.fetchone()
        fio = ''
        for i in c:
            #print(i)
            fio = i
        insert_data = """
                              INSERT INTO waiting(
                                       id_telegram,
                                       inn,
                                       type_doctor,
                                       time,
                                       t) VALUES(?,?,?,?,?)
                              """
        cursor.execute(insert_data, (str(id), str(fio), "pediatr", str(t), 0,))
        update_data = """
                              UPDATE pediatr set time1000 = ?
                              """
        cursor.execute(update_data, (0,))
        db.commit()
        await bot.send_message(query.from_user.id,
                               'Сіз таңдалған уақытқа жазылдыңыз🙃, кешікпей келіңіз😉, қабылдау уақыты 40 минут⏱')

    elif answer_data == 'pediatr1100':
        t = '11:00'
        id = query.from_user.id
        #print(id)
        cu = "SELECT first_last_name FROM registrated_clients WHERE id_telegram = ?"
        cursor.execute(cu, (id,))
        c = cursor.fetchone()
        fio = ''
        for i in c:
            #print(i)
            fio = i
        insert_data = """
                                      INSERT INTO waiting(
                                               id_telegram,
                                               inn,
                                               type_doctor,
                                               time,
                                               t) VALUES(?,?,?,?,?)
                                      """
        cursor.execute(insert_data, (str(id), str(fio), "pediatr", str(t), 0,))
        update_data = """
                                      UPDATE pediatr set time1100 = ?
                                      """
        cursor.execute(update_data, (0,))
        db.commit()
        await bot.send_message(query.from_user.id,
                               'Сіз таңдалған уақытқа жазылдыңыз🙃, кешікпей келіңіз😉, қабылдау уақыты 40 минут⏱')

    elif answer_data == 'pediatr1200':
        t = '12:00'
        id = query.from_user.id
        #print(id)
        cu = "SELECT first_last_name FROM registrated_clients WHERE id_telegram = ?"
        cursor.execute(cu, (id,))
        c = cursor.fetchone()
        fio = ''
        for i in c:
            #print(i)
            fio = i
        insert_data = """
                                              INSERT INTO waiting(
                                                       id_telegram,
                                                       inn,
                                                       type_doctor,
                                                       time,
                                                       t) VALUES(?,?,?,?,?)
                                              """
        cursor.execute(insert_data, (str(id), str(fio), "pediatr", str(t), 0,))
        update_data = """
                                              UPDATE pediatr set time1200 = ?
                                              """
        cursor.execute(update_data, (0,))
        db.commit()
        await bot.send_message(query.from_user.id,
                               'Сіз таңдалған уақытқа жазылдыңыз🙃, кешікпей келіңіз😉, қабылдау уақыты 40 минут⏱')

    elif answer_data == 'pediatr1340':
        t = '13:40'
        id = query.from_user.id
        #print(id)
        cu = "SELECT first_last_name FROM registrated_clients WHERE id_telegram = ?"
        cursor.execute(cu, (id,))
        c = cursor.fetchone()
        fio = ''
        for i in c:
            #print(i)
            fio = i
        insert_data = """
                                                      INSERT INTO waiting(
                                                               id_telegram,
                                                               inn,
                                                               type_doctor,
                                                               time,
                                                               t) VALUES(?,?,?,?,?)
                                                      """
        cursor.execute(insert_data, (str(id), str(fio), "pediatr", str(t), 0,))
        update_data = """
                                                      UPDATE pediatr set time1340 = ?
                                                      """
        cursor.execute(update_data, (0,))
        db.commit()
        await bot.send_message(query.from_user.id,
                               'Сіз таңдалған уақытқа жазылдыңыз🙃, кешікпей келіңіз😉, қабылдау уақыты 40 минут⏱')

    elif answer_data == 'pediatr1440':

        t = '14:40'
        id = query.from_user.id
        #print(id)
        cu = "SELECT first_last_name FROM registrated_clients WHERE id_telegram = ?"
        cursor.execute(cu, (id,))
        c = cursor.fetchone()
        fio = ''
        for i in c:
            #print(i)
            fio = i
        insert_data = """
                                                              INSERT INTO waiting(
                                                                       id_telegram,
                                                                       inn,
                                                                       type_doctor,
                                                                       time,
                                                                       t) VALUES(?,?,?,?,?)
                                                              """
        cursor.execute(insert_data, (str(id), str(fio), "pediatr", str(t), 0,))
        update_data = """
                                                              UPDATE pediatr set time1440 = ?
                                                              """
        cursor.execute(update_data, (0,))
        db.commit()
        await bot.send_message(query.from_user.id,
                               'Сіз таңдалған уақытқа жазылдыңыз🙃, кешікпей келіңіз😉, қабылдау уақыты 40 минут⏱')

    elif answer_data == 'pediatr1540':

        t = '15:40'
        id = query.from_user.id
        #print(id)
        cu = "SELECT first_last_name FROM registrated_clients WHERE id_telegram = ?"
        cursor.execute(cu, (id,))
        c = cursor.fetchone()
        fio = ''
        for i in c:
            #print(i)
            fio = i
        insert_data = """
                                                                      INSERT INTO waiting(
                                                                               id_telegram,
                                                                               inn,
                                                                               type_doctor,
                                                                               time,
                                                                               t) VALUES(?,?,?,?,?)
                                                                      """
        cursor.execute(insert_data, (str(id), str(fio), "pediatr", str(t), 0,))
        update_data = """
                                                                      UPDATE pediatr set time1540 = ?
                                                                      """
        cursor.execute(update_data, (0,))
        db.commit()
        await bot.send_message(query.from_user.id,
                               'Сіз таңдалған уақытқа жазылдыңыз🙃, кешікпей келіңіз😉, қабылдау уақыты 40 минут⏱')

    elif answer_data == 'pediatr1640':

        t = '16:40'
        id = query.from_user.id
        #print(id)
        cu = "SELECT first_last_name FROM registrated_clients WHERE id_telegram = ?"
        cursor.execute(cu, (id,))
        c = cursor.fetchone()
        fio = ''
        for i in c:
            #print(i)
            fio = i
        insert_data = """
                                                                              INSERT INTO waiting(
                                                                                       id_telegram,
                                                                                       inn,
                                                                                       type_doctor,
                                                                                       time,
                                                                                       t) VALUES(?,?,?,?,?)
                                                                              """
        cursor.execute(insert_data, (str(id), str(fio), "pediatr", str(t), 0,))
        update_data = """
                                                                              UPDATE pediatr set time1640 = ?
                                                                              """
        cursor.execute(update_data, (0,))
        db.commit()
        await bot.send_message(query.from_user.id,
                               'Сіз таңдалған уақытқа жазылдыңыз🙃, кешікпей келіңіз😉, қабылдау уақыты 40 минут⏱')

    elif answer_data == 'pediatr1740':

        t = '17:40'
        id = query.from_user.id
        #print(id)
        cu = "SELECT first_last_name FROM registrated_clients WHERE id_telegram = ?"
        cursor.execute(cu, (id,))
        c = cursor.fetchone()
        fio = ''
        for i in c:
            #print(i)
            fio = i
        insert_data = """
                                                                                      INSERT INTO waiting(
                                                                                               id_telegram,
                                                                                               inn,
                                                                                               type_doctor,
                                                                                               time,
                                                                                               t) VALUES(?,?,?,?,?)
                                                                                      """
        cursor.execute(insert_data, (str(id), str(fio), "pediatr", str(t), 0,))
        update_data = """
                                                                                      UPDATE pediatr set time1740 = ?
                                                                                      """
        cursor.execute(update_data, (0,))
        db.commit()
        await bot.send_message(query.from_user.id,
                               'Сіз таңдалған уақытқа жазылдыңыз🙃, кешікпей келіңіз😉, қабылдау уақыты 40 минут⏱')

    #############################

    elif answer_data == 'nevrolog0900':
        id = query.from_user.id
        #print(id)
        t = '09:00'
        cu = "SELECT first_last_name FROM registrated_clients WHERE id_telegram = ?"
        cursor.execute(cu, (id,))
        c = cursor.fetchone()
        fio = ''
        for i in c:
            print(i)
            fio = i
        insert_data = """
                      INSERT INTO waiting(
                               id_telegram,
                               inn,
                               type_doctor,
                               time,
                               t) VALUES(?,?,?,?,?)
                      """
        cursor.execute(insert_data, (str(id), str(fio), "nevrolog", str(t), 0,))
        update_data = """
                      UPDATE nevrolog set time0900 = ?
                      """
        cursor.execute(update_data, (0,))
        db.commit()
        await bot.send_message(query.from_user.id, 'Сіз таңдалған уақытқа жазылдыңыз🙃, кешікпей келіңіз😉, қабылдау уақыты 40 минут⏱')

    elif answer_data == 'nevrolog1000':
        t = '10:00'
        id = query.from_user.id
        #print(id)
        cu = "SELECT first_last_name FROM registrated_clients WHERE id_telegram = ?"
        cursor.execute(cu, (id,))
        c = cursor.fetchone()
        fio = ''
        for i in c:
            print(i)
            fio = i
        insert_data = """
                              INSERT INTO waiting(
                                       id_telegram,
                                       inn,
                                       type_doctor,
                                       time,
                                       t) VALUES(?,?,?,?,?)
                              """
        cursor.execute(insert_data, (str(id), str(fio), "nevrolog", str(t), 0,))
        update_data = """
                              UPDATE nevrolog set time1000 = ?
                              """
        cursor.execute(update_data, (0,))
        db.commit()
        await bot.send_message(query.from_user.id,
                               'Сіз таңдалған уақытқа жазылдыңыз🙃, кешікпей келіңіз😉, қабылдау уақыты 40 минут⏱')

    elif answer_data == 'nevrolog1100':
        t = '11:00'
        id = query.from_user.id
        #print(id)
        cu = "SELECT first_last_name FROM registrated_clients WHERE id_telegram = ?"
        cursor.execute(cu, (id,))
        c = cursor.fetchone()
        fio = ''
        for i in c:
            print(i)
            fio = i
        insert_data = """
                                      INSERT INTO waiting(
                                               id_telegram,
                                               inn,
                                               type_doctor,
                                               time,
                                               t) VALUES(?,?,?,?,?)
                                      """
        cursor.execute(insert_data, (str(id), str(fio), "nevrolog", str(t), 0,))
        update_data = """
                                      UPDATE nevrolog set time1100 = ?
                                      """
        cursor.execute(update_data, (0,))
        db.commit()
        await bot.send_message(query.from_user.id,
                               'Сіз таңдалған уақытқа жазылдыңыз🙃, кешікпей келіңіз😉, қабылдау уақыты 40 минут⏱')

    elif answer_data == 'nevrolog1200':
        t = '12:00'
        id = query.from_user.id
        #print(id)
        cu = "SELECT first_last_name FROM registrated_clients WHERE id_telegram = ?"
        cursor.execute(cu, (id,))
        c = cursor.fetchone()
        fio = ''
        for i in c:
            #print(i)
            fio = i
        insert_data = """
                                              INSERT INTO waiting(
                                                       id_telegram,
                                                       inn,
                                                       type_doctor,
                                                       time,
                                                       t) VALUES(?,?,?,?,?)
                                              """
        cursor.execute(insert_data, (str(id), str(fio), "nevrolog", str(t), 0,))
        update_data = """
                                              UPDATE nevrolog set time1200 = ?
                                              """
        cursor.execute(update_data, (0,))
        db.commit()
        await bot.send_message(query.from_user.id,
                               'Сіз таңдалған уақытқа жазылдыңыз🙃, кешікпей келіңіз😉, қабылдау уақыты 40 минут⏱')

    elif answer_data == 'nevrolog1340':
        t = '13:40'
        id = query.from_user.id
        #print(id)
        cu = "SELECT first_last_name FROM registrated_clients WHERE id_telegram = ?"
        cursor.execute(cu, (id,))
        c = cursor.fetchone()
        fio = ''
        for i in c:
            #print(i)
            fio = i
        insert_data = """
                                                      INSERT INTO waiting(
                                                               id_telegram,
                                                               inn,
                                                               type_doctor,
                                                               time,
                                                               t) VALUES(?,?,?,?,?)
                                                      """
        cursor.execute(insert_data, (str(id), str(fio), "nevrolog", str(t), 0,))
        update_data = """
                                                      UPDATE nevrolog set time1340 = ?
                                                      """
        cursor.execute(update_data, (0,))
        db.commit()
        await bot.send_message(query.from_user.id,
                               'Сіз таңдалған уақытқа жазылдыңыз🙃, кешікпей келіңіз😉, қабылдау уақыты 40 минут⏱')

    elif answer_data == 'nevrolog1440':

        t = '14:40'
        id = query.from_user.id
        #print(id)
        cu = "SELECT first_last_name FROM registrated_clients WHERE id_telegram = ?"
        cursor.execute(cu, (id,))
        c = cursor.fetchone()
        fio = ''
        for i in c:
            #print(i)
            fio = i
        insert_data = """
                                                              INSERT INTO waiting(
                                                                       id_telegram,
                                                                       inn,
                                                                       type_doctor,
                                                                       time,
                                                                       t) VALUES(?,?,?,?,?)
                                                              """
        cursor.execute(insert_data, (str(id), str(fio), "nevrolog", str(t), 0,))
        update_data = """
                                                              UPDATE nevrolog set time1440 = ?
                                                              """
        cursor.execute(update_data, (0,))
        db.commit()
        await bot.send_message(query.from_user.id,
                               'Сіз таңдалған уақытқа жазылдыңыз🙃, кешікпей келіңіз😉, қабылдау уақыты 40 минут⏱')

    elif answer_data == 'nevrolog1540':

        t = '15:40'
        id = query.from_user.id
        #print(id)
        cu = "SELECT first_last_name FROM registrated_clients WHERE id_telegram = ?"
        cursor.execute(cu, (id,))
        c = cursor.fetchone()
        fio = ''
        for i in c:
            #print(i)
            fio = i
        insert_data = """
                                                                      INSERT INTO waiting(
                                                                               id_telegram,
                                                                               inn,
                                                                               type_doctor,
                                                                               time,
                                                                               t) VALUES(?,?,?,?,?)
                                                                      """
        cursor.execute(insert_data, (str(id), str(fio), "nevrolog", str(t), 0,))
        update_data = """
                                                                      UPDATE nevrolog set time1540 = ?
                                                                      """
        cursor.execute(update_data, (0,))
        db.commit()
        await bot.send_message(query.from_user.id,
                               'Сіз таңдалған уақытқа жазылдыңыз🙃, кешікпей келіңіз😉, қабылдау уақыты 40 минут⏱')

    elif answer_data == 'nevrolog1640':

        t = '16:40'
        id = query.from_user.id
        #print(id)
        cu = "SELECT first_last_name FROM registrated_clients WHERE id_telegram = ?"
        cursor.execute(cu, (id,))
        c = cursor.fetchone()
        fio = ''
        for i in c:
            #print(i)
            fio = i
        insert_data = """
                                                                              INSERT INTO waiting(
                                                                                       id_telegram,
                                                                                       inn,
                                                                                       type_doctor,
                                                                                       time,
                                                                                       t) VALUES(?,?,?,?,?)
                                                                              """
        cursor.execute(insert_data, (str(id), str(fio), "nevrolog", str(t), 0,))
        update_data = """
                                                                              UPDATE nevrolog set time1640 = ?
                                                                              """
        cursor.execute(update_data, (0,))
        db.commit()
        await bot.send_message(query.from_user.id,
                               'Сіз таңдалған уақытқа жазылдыңыз🙃, кешікпей келіңіз😉, қабылдау уақыты 40 минут⏱')

    elif answer_data == 'nevrolog1740':

        t = '17:40'
        id = query.from_user.id
        #print(id)
        cu = "SELECT first_last_name FROM registrated_clients WHERE id_telegram = ?"
        cursor.execute(cu, (id,))
        c = cursor.fetchone()
        fio = ''
        for i in c:
            #print(i)
            fio = i
        insert_data = """
                                                                                      INSERT INTO waiting(
                                                                                               id_telegram,
                                                                                               inn,
                                                                                               type_doctor,
                                                                                               time,
                                                                                               t) VALUES(?,?,?,?,?)
                                                                                      """
        cursor.execute(insert_data, (str(id), str(fio), "nevrolog", str(t), 0,))
        update_data = """
                                                                                      UPDATE nevrolog set time1740 = ?
                                                                                      """
        cursor.execute(update_data, (0,))
        db.commit()
        await bot.send_message(query.from_user.id,
                               'Сіз таңдалған уақытқа жазылдыңыз🙃, кешікпей келіңіз😉, қабылдау уақыты 40 минут⏱')

    #############################

if __name__ == "__main__":
    '''
    Запуск
    '''

    executor.start_polling(dp, skip_updates=True)
    check_for_signup()
