# This Python file uses the following encoding: utf-8
import os, datetime, typing, traceback

from aiogram import Bot, Dispatcher, executor, types
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from loguru import logger

import content, bot_config
from models import Invest_profile_tgbot
from functions import send_tg_notification, get_result


"""
Откуда взят тест: https://assetallocation.ru/merrill-edge-investor-profile/ 
"""

# Конфигурация логов
fmt = "[{time:YYYY-MM-DD HH:mm:ss}] | [{level}] | <{extra[log_file]}>: {name}:{function}:{line} - {message}"
logger.add("bot_log/bot_log.log", format=fmt, filter=lambda record: record["extra"]["log_file"] == "bot_log", backtrace=True, diagnose=False)
logger.bind(log_file="bot_log")





engine = create_engine(bot_config.bd_connection, pool_recycle=280)
Session = sessionmaker(bind=engine)
session = Session()
    
# Чат-бот
bot = Bot(token=bot_config.tg_token , parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


try:
    # Запуск тестировани и бота
    @dp.message_handler(commands=['start']) 
    async def send_welcome(message: types.Message):
        try:
            nickname = '@' + message.from_user.username
            add_nickname = Invest_profile_tgbot(user_id =message.from_user.id ,user_nickname=nickname, last_modified=datetime.datetime.now())
            session.merge(add_nickname)
            session.commit()
        except:
            add_first_name = Invest_profile_tgbot(user_id =message.from_user.id ,user_nickname=message.from_user.first_name, last_modified=datetime.datetime.now())
            session.merge(add_first_name)
            session.commit()
        msg = f"Здравствуйте, {message.from_user.first_name}.\nДля определения инвестиционного профиля, пожалуйста, ответьте на все вопросы. Тест поможет выявить Ваше отношение к риску, цели и задачи инвестирования.\n\nПосле прохождения теста Вы получите персональную рекомендацию по составлению инвестиционного плана и выбору стратегии."
        await message.reply(msg)
        msg2 = "Готовы начать тест?"      
        await message.answer(msg2, reply_markup=content.quiz)

    # Если готовы начать
    @dp.callback_query_handler(lambda c: c.data == 'start_quiz')
    async def start_quiz(callback_query: types.CallbackQuery):
        await bot.send_message(callback_query.from_user.id, content.voprosi[1], reply_markup=content.answer_buttons[1])   

    # Ловим ответы на вопросы и после ответа сразу отсылаем следующий вопрос, и так до 9 вопроса включительно
    @dp.callback_query_handler(content.answerz.filter(vopros_id=["1","2","3","4","5","6","7","8","9"]))
    async def get_answers(call: types.CallbackQuery, callback_data: dict):
        user_name = call.from_user.first_name
        user_nickname = call.from_user.username
        chat_id=call.message.chat.id
        try:
            vopros_id = callback_data['vopros_id']
            otvet = callback_data['user_answer']
            
            if int(vopros_id) <= 8:
                next_vopros = content.voprosi[int(vopros_id) + 1]
                answer = content.answer_buttons[int(vopros_id) + 1]
          
                if vopros_id == '1':                    
                    if otvet =='back':                        
                        with open(content.pic_2_file_path, 'rb') as photo2:                        
                            await bot.send_photo(chat_id=chat_id, photo=photo2, caption=next_vopros, reply_markup=answer)
                                                   
                    else:
                        add_otvet = Invest_profile_tgbot(user_id=call.from_user.id, otvet_1=otvet, last_modified=datetime.datetime.now())
                        session.merge(add_otvet)
                        session.commit()
                        with open(content.pic_2_file_path, 'rb') as photo2:
                            await bot.send_message(chat_id, f'Вопрос №{vopros_id}, ваш ответ: {otvet}')                        
                            await bot.send_photo(chat_id=chat_id, photo=photo2, caption=next_vopros,reply_markup=answer)                    
                elif vopros_id == '2':
                    if otvet =='back':
                        await bot.send_message(chat_id, next_vopros, reply_markup=answer)
                    else:
                        add_otvet = Invest_profile_tgbot(user_id=call.from_user.id, otvet_2=otvet, last_modified=datetime.datetime.now())
                        session.merge(add_otvet)
                        session.commit()
                        await bot.send_message(chat_id, f'Вопрос №{vopros_id}, ваш ответ: {otvet}')
                        await bot.send_message(chat_id, next_vopros, reply_markup=answer)
                elif vopros_id == '3':
                    if otvet =='back':
                        await bot.send_message(chat_id, next_vopros, reply_markup=answer)
                    else:
                        add_otvet = Invest_profile_tgbot(user_id=call.from_user.id, otvet_3=otvet, last_modified=datetime.datetime.now())
                        session.merge(add_otvet)
                        session.commit()
                        await bot.send_message(chat_id, f'Вопрос №{vopros_id}, ваш ответ: {otvet}')
                        await bot.send_message(chat_id, next_vopros, reply_markup=answer)
                elif vopros_id == '4':
                    if otvet =='back':
                        with open(content.pic_5_file_path, 'rb') as photo5:                        
                            await bot.send_photo(chat_id=chat_id, photo=photo5, caption='',reply_markup=answer)
                        await bot.send_message(chat_id, next_vopros, reply_markup=answer)
                    else:
                        add_otvet = Invest_profile_tgbot(user_id=call.from_user.id, otvet_4=otvet, last_modified=datetime.datetime.now())
                        session.merge(add_otvet)
                        session.commit()
                        with open(content.pic_5_file_path, 'rb') as photo5:
                            await bot.send_message(chat_id, f'Вопрос №{vopros_id}, ваш ответ: {otvet}')                        
                            await bot.send_photo(chat_id=chat_id, photo=photo5, caption=next_vopros,reply_markup=answer)                        
                elif vopros_id == '5':
                    if otvet =='back':
                        with open(content.pic_6_file_path, 'rb') as photo6:
                            await bot.send_photo(chat_id=chat_id, photo=photo6, caption=next_vopros,reply_markup=answer)
                    else:
                        add_otvet =  Invest_profile_tgbot(user_id=call.from_user.id, otvet_5 = otvet, last_modified=datetime.datetime.now())
                        session.merge(add_otvet)
                        session.commit()                        
                        with open(content.pic_6_file_path, 'rb') as photo6:
                            await bot.send_message(chat_id, f'Вопрос №{vopros_id}, ваш ответ: {otvet}')
                            await bot.send_photo(chat_id=chat_id, photo=photo6, caption=next_vopros,reply_markup=answer)
                elif vopros_id == '6':
                    if otvet =='back':
                        await bot.send_message(chat_id, next_vopros, reply_markup=answer)
                    else:
                        add_otvet = Invest_profile_tgbot(user_id=call.from_user.id, otvet_6=otvet, last_modified=datetime.datetime.now())
                        session.merge(add_otvet)
                        session.commit()
                        await bot.send_message(chat_id, f'Вопрос №{vopros_id}, ваш ответ: {otvet}')
                        await bot.send_message(chat_id, next_vopros, reply_markup=answer) 
                                     
                elif vopros_id == '7':
                    if otvet =='back':
                        await bot.send_message(chat_id, next_vopros, reply_markup=answer)
                    else:
                        add_otvet = Invest_profile_tgbot(user_id=call.from_user.id, otvet_7=otvet, last_modified=datetime.datetime.now())
                        session.merge(add_otvet)
                        session.commit()
                        await bot.send_message(chat_id, f'Вопрос №{vopros_id}, ваш ответ: {otvet}')
                        await bot.send_message(chat_id, next_vopros, reply_markup=answer)
                elif vopros_id == '8':
                    if otvet =='back':
                        await bot.send_message(chat_id, content.vopros_8_text, reply_markup=content.vopros_8_btn)
                    elif otvet == "Нет":
                        await bot.send_message(chat_id, f'Вопрос №{vopros_id}, ваш ответ: {otvet}')                        
                        await bot.send_message(chat_id, next_vopros, reply_markup=answer)                        
                        add_otvet =  Invest_profile_tgbot(user_id=call.from_user.id, otvet_8 = otvet, last_modified=datetime.datetime.now())                        
                        session.merge(add_otvet)                        
                        session.commit()                        
                    elif otvet == "Да":
                        await bot.send_message(chat_id, f'Вопрос №{vopros_id}, ваш ответ: {otvet}')            
                        add_otvet =  Invest_profile_tgbot(user_id=chat_id, otvet_8 = otvet, last_modified=datetime.datetime.now())                        
                        session.merge(add_otvet)                        
                        session.commit()                         
                        await bot.send_message(chat_id,'Спасибо за ваши ответы!\nСейчас пришлем результаты.')

                        # Считаем результаты
                        await get_result(user_id=chat_id, session=session, bot=bot)

    
            elif vopros_id == '9': #Считаем результаты тут и записываем в БД когда на 8 вопрос ответили "НЕТ"
                if otvet =='back':
                    await bot.send_message(chat_id, content.vopros_9_text, reply_markup=content.vopros_9_btn)
                else:                   
                    add_otvet = Invest_profile_tgbot(user_id=chat_id, otvet_9=otvet, last_modified=datetime.datetime.now())
                    session.merge(add_otvet)
                    session.commit()
                    await bot.send_message(chat_id, f'Вопрос №{vopros_id}, ваш ответ: {otvet}')
                    await bot.send_message(chat_id, 'Назад к 9 вопросу ', reply_markup=content.vopros_9_btns_end)

                    await bot.send_message(chat_id,'Спасибо за ваши ответы!\nСейчас пришлем результаты.')

                    # Считаем результаты
                    await get_result(user_id=chat_id, session=session, bot=bot) 

        # Ошибки во время ответов
        except Exception as errory:
            logger.exception(f'Ошибка: {errory}', log_file="bot_log")
            error_tg_msg_raw = traceback.format_exc()

            # меняем скобки, тк библа для уведомлений ругается
            error_tg_msg_1 = error_tg_msg_raw.replace("<", "")
            error_tg_msg_clean = error_tg_msg_1.replace(">", "")
            # 

            about_user = 'Имя: ' + user_name + '\nNickname: ' + '@' + str(user_nickname)      
            finally_error_msg = f"""Ошибка у пользователя:\n{about_user}\n\nОписание:\n{error_tg_msg_clean}"""
            await send_tg_notification(finally_error_msg)

            # Шлем уведомление об ошибке юзеру
            await bot.send_message(chat_id,'Возникла непредвиденная ошибка. Информация о ней уже ушла разработчикам.\nМы уведомим вас о её решении и вы сможете перепройти тест.')
                        

    # Если не хотят начать тест
    @dp.callback_query_handler(lambda c: c.data == 'dont_start_quiz')
    async def process_callback_button1(callback_query: types.CallbackQuery):
        try:
            await bot.answer_callback_query(callback_query.id)
            msg = "Жаль. Если передумаете, то вы всегда можете начать тест отправив команду /start в этот чат"
            await bot.send_message(callback_query.from_user.id, msg)
        except Exception as errory:
            logger.exception('Got exception',log_file="bot_log")


except Exception as errory:
        logger.exception('Got exception',log_file="bot_log")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)