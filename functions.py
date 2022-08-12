from notifiers import get_notifier
from loguru import logger
import traceback
from aiogram import types

import content, bot_config
from models import Invest_profile_tgbot




# функция отправления сообщения в бот для уведомлений
telegram = get_notifier('telegram')
async def send_tg_notification(msg):
    for chat_id in bot_config.chad_ids.values():
        telegram.notify(message=f'<b>ПРОЕКТ:</b> Телеграм бот https://t.me/investor_profile_testing_bot\n\n{msg}', token=bot_config.tg_token_notifier, chat_id=chat_id, parse_mode='html')



# функция расчета результата
async def get_result(user_id, session, bot):
    try:
        otveti = session.query(Invest_profile_tgbot).filter(Invest_profile_tgbot.user_id==user_id).first()
        summ_1_to_6_vopros = content.points_otvet_1[otveti.otvet_1] + content.points_otvet_2[otveti.otvet_2] + content.points_otvet_3[otveti.otvet_3] + content.points_otvet_4[otveti.otvet_4] + content.points_otvet_5[otveti.otvet_5] + content.points_otvet_6[otveti.otvet_6]


        if summ_1_to_6_vopros <=15:   #Результаты до 15 балов включительно                  
            if otveti.otvet_7 == "A" or otveti.otvet_7 == "B":
                user_invest_profile = content.profiles['Консервативный']
                add_invest_profile =  Invest_profile_tgbot(user_id=user_id, invest_profile = user_invest_profile)                        
                session.merge(add_invest_profile)                                
                session.commit()

                await bot.send_message(user_id, f'Ваш Инвестиционный Профиль:\n\n{user_invest_profile}', reply_markup=types.ReplyKeyboardRemove())                               
                await bot.send_message(user_id, f'Чтобы пройти тест заново нажмите /start')

            elif otveti.otvet_7 == "C" and otveti.otvet_3 == "A":
                user_invest_profile = content.profiles['Консервативный']
                add_invest_profile =  Invest_profile_tgbot(user_id=user_id, invest_profile = user_invest_profile)                        
                session.merge(add_invest_profile)                                
                session.commit()

                await bot.send_message(user_id, f'Ваш Инвестиционный Профиль:\n\n{user_invest_profile}', reply_markup=types.ReplyKeyboardRemove())
                await bot.send_message(user_id, f'Чтобы пройти тест заново нажмите /start')

            elif otveti.otvet_7 == "C" and otveti.otvet_3 in ['B', 'C', 'D']:                        
                user_invest_profile = content.profiles['Умеренно Консервативный']
                add_invest_profile =  Invest_profile_tgbot(user_id=user_id, invest_profile = user_invest_profile)                        
                session.merge(add_invest_profile)                                
                session.commit()

                await bot.send_message(user_id, f'Ваш Инвестиционный Профиль:\n\n{user_invest_profile}', reply_markup=types.ReplyKeyboardRemove())
                await bot.send_message(user_id, f'Чтобы пройти тест заново нажмите /start')


            # Следующий блок ответов для подсчетов 16-25 балов
        elif 16 <= summ_1_to_6_vopros <= 25:
            if otveti.otvet_7 == "A" or otveti.otvet_7 == "B": 
                if otveti.otvet_1 == "A":
                    user_invest_profile = content.profiles['Консервативный']
                    add_invest_profile =  Invest_profile_tgbot(user_id=user_id, invest_profile = user_invest_profile)                        
                    session.merge(add_invest_profile)                                
                    session.commit()

                    await bot.send_message(user_id, f'Ваш Инвестиционный Профиль:\n\n{user_invest_profile}', reply_markup=types.ReplyKeyboardRemove())
                    await bot.send_message(user_id, f'Чтобы пройти тест заново нажмите /start')

                elif otveti.otvet_1 in ['B', 'C', 'D', 'E']:
                    user_invest_profile = content.profiles['Умеренно Консервативный']
                    add_invest_profile =  Invest_profile_tgbot(user_id=user_id, invest_profile = user_invest_profile)                        
                    session.merge(add_invest_profile)                                
                    session.commit()

                    await bot.send_message(user_id, f'Ваш Инвестиционный Профиль:\n\n{user_invest_profile}', reply_markup=types.ReplyKeyboardRemove())
                    await bot.send_message(user_id, f'Чтобы пройти тест заново нажмите /start')

            elif otveti.otvet_7 == "C": 
                if otveti.otvet_1 == "E":
                    user_invest_profile = content.profiles['Умеренный']
                    add_invest_profile =  Invest_profile_tgbot(user_id=user_id, invest_profile = user_invest_profile)                        
                    session.merge(add_invest_profile)                                
                    session.commit()

                    await bot.send_message(user_id, f'Ваш Инвестиционный Профиль:\n\n{user_invest_profile}', reply_markup=types.ReplyKeyboardRemove())
                    await bot.send_message(user_id, f'Чтобы пройти тест заново нажмите /start')

                elif otveti.otvet_1 in ['B', 'C', 'D', 'A']:
                    user_invest_profile = content.profiles['Умеренно Консервативный']
                    add_invest_profile =  Invest_profile_tgbot(user_id=user_id, invest_profile = user_invest_profile)                        
                    session.merge(add_invest_profile)                                
                    session.commit()

                    await bot.send_message(user_id, f'Ваш Инвестиционный Профиль:\n\n{user_invest_profile}', reply_markup=types.ReplyKeyboardRemove())
                    await bot.send_message(user_id, f'Чтобы пройти тест заново нажмите /start')

            # Следующий блок ответов для подсчетов 26-34 балов
        elif 26 <= summ_1_to_6_vopros <= 34:
            if otveti.otvet_7 == 'A': 
                if otveti.otvet_1 in ['A', 'B', 'C']:
                    user_invest_profile = content.profiles['Умеренно Консервативный']
                    add_invest_profile =  Invest_profile_tgbot(user_id=user_id, invest_profile = user_invest_profile)                        
                    session.merge(add_invest_profile)                                
                    session.commit()

                    await bot.send_message(user_id, f'Ваш Инвестиционный Профиль:\n\n{user_invest_profile}', reply_markup=types.ReplyKeyboardRemove())
                    await bot.send_message(user_id, f'Чтобы пройти тест заново нажмите /start')
                elif otveti.otvet_1 in ['D', 'E']:
                    user_invest_profile = content.profiles['Умеренный']
                    add_invest_profile =  Invest_profile_tgbot(user_id=user_id, invest_profile = user_invest_profile)                        
                    session.merge(add_invest_profile)                                
                    session.commit()

                    await bot.send_message(user_id, f'Ваш Инвестиционный Профиль:\n\n{user_invest_profile}', reply_markup=types.ReplyKeyboardRemove())
                    await bot.send_message(user_id, f'Чтобы пройти тест заново нажмите /start')

            elif otveti.otvet_7 == 'B': 
                if otveti.otvet_1 in ['A', 'B']:                            
                    user_invest_profile = content.profiles['Умеренно Консервативный']
                    add_invest_profile =  Invest_profile_tgbot(user_id=user_id, invest_profile = user_invest_profile)                        
                    session.merge(add_invest_profile)                                
                    session.commit()

                    await bot.send_message(user_id, f'Ваш Инвестиционный Профиль:\n\n{user_invest_profile}', reply_markup=types.ReplyKeyboardRemove())
                    await bot.send_message(user_id, f'Чтобы пройти тест заново нажмите /start')
                elif otveti.otvet_1 in ['C', 'D', 'E']:
                    user_invest_profile = content.profiles['Умеренный']
                    add_invest_profile =  Invest_profile_tgbot(user_id=user_id, invest_profile = user_invest_profile)                        
                    session.merge(add_invest_profile)                                
                    session.commit()

                    await bot.send_message(user_id, f'Ваш Инвестиционный Профиль:\n\n{user_invest_profile}', reply_markup=types.ReplyKeyboardRemove()) 
                    await bot.send_message(user_id, f'Чтобы пройти тест заново нажмите /start')

            elif otveti.otvet_7 == 'C': 
                if otveti.otvet_1 in ['A', 'B', 'C']:
                    user_invest_profile = content.profiles['Умеренный']
                    add_invest_profile =  Invest_profile_tgbot(user_id=user_id, invest_profile = user_invest_profile)                        
                    session.merge(add_invest_profile)                                
                    session.commit()

                    await bot.send_message(user_id, f'Ваш Инвестиционный Профиль:\n\n{user_invest_profile}', reply_markup=types.ReplyKeyboardRemove())
                    await bot.send_message(user_id, f'Чтобы пройти тест заново нажмите /start')
                elif otveti.otvet_1 in ['D', 'E']:
                    user_invest_profile = content.profiles['Умеренно Агрессивный']
                    add_invest_profile =  Invest_profile_tgbot(user_id=user_id, invest_profile = user_invest_profile)                        
                    session.merge(add_invest_profile)                                
                    session.commit()

                    await bot.send_message(user_id, f'Ваш Инвестиционный Профиль:\n\n{user_invest_profile}', reply_markup=types.ReplyKeyboardRemove())
                    await bot.send_message(user_id, f'Чтобы пройти тест заново нажмите /start')

            # Следующий блок ответов для подсчетов 35-44 балов
        elif 35 <= summ_1_to_6_vopros <= 44:
            if otveti.otvet_8 == 'Да': 
                if otveti.otvet_7 == 'A':
                    user_invest_profile = content.profiles['Умеренный']
                    add_invest_profile =  Invest_profile_tgbot(user_id=user_id, invest_profile = user_invest_profile)                        
                    session.merge(add_invest_profile)                                
                    session.commit()

                    await bot.send_message(user_id, f'Ваш Инвестиционный Профиль:\n\n{user_invest_profile}', reply_markup=types.ReplyKeyboardRemove())
                    await bot.send_message(user_id, f'Чтобы пройти тест заново нажмите /start')
                elif otveti.otvet_7 == 'B':
                    user_invest_profile = content.profiles['Умеренный']
                    add_invest_profile =  Invest_profile_tgbot(user_id=user_id, invest_profile = user_invest_profile)                        
                    session.merge(add_invest_profile)                                
                    session.commit()

                    await bot.send_message(user_id, f'Ваш Инвестиционный Профиль:\n\n{user_invest_profile}', reply_markup=types.ReplyKeyboardRemove())
                    await bot.send_message(user_id, f'Чтобы пройти тест заново нажмите /start')
                elif otveti.otvet_7 == 'C':
                    user_invest_profile = content.profiles['Агрессивный']
                    add_invest_profile = Invest_profile_tgbot(user_id=user_id, invest_profile = user_invest_profile)                        
                    session.merge(add_invest_profile)                                
                    session.commit()

                    await bot.send_message(user_id, f'Ваш Инвестиционный Профиль:\n\n{user_invest_profile}', reply_markup=types.ReplyKeyboardRemove()) 
                    await bot.send_message(user_id, f'Чтобы пройти тест заново нажмите /start')

            elif otveti.otvet_8 == 'Нет': 
                if otveti.otvet_7 == 'A':
                    user_invest_profile = content.profiles['Умеренный']
                    add_invest_profile = Invest_profile_tgbot(user_id=user_id, invest_profile = user_invest_profile)                        
                    session.merge(add_invest_profile)                                
                    session.commit()

                    await bot.send_message(user_id, f'Ваш Инвестиционный Профиль:\n\n{user_invest_profile}', reply_markup=types.ReplyKeyboardRemove())
                    await bot.send_message(user_id, f'Чтобы пройти тест заново нажмите /start')
                elif otveti.otvet_7 == 'B' and otveti.otvet_9 == 'Да':
                    user_invest_profile = content.profiles['Умеренно Агрессивный']
                    add_invest_profile = Invest_profile_tgbot(user_id=user_id, invest_profile = user_invest_profile)                        
                    session.merge(add_invest_profile)                                
                    session.commit()

                    await bot.send_message(user_id, f'Ваш Инвестиционный Профиль:\n\n{user_invest_profile}', reply_markup=types.ReplyKeyboardRemove())
                    await bot.send_message(user_id, f'Чтобы пройти тест заново нажмите /start')
                elif otveti.otvet_7 == 'B' and otveti.otvet_9 == 'Нет':
                    user_invest_profile = content.profiles['Умеренный']
                    add_invest_profile = Invest_profile_tgbot(user_id=user_id, invest_profile = user_invest_profile)                        
                    session.merge(add_invest_profile)                                
                    session.commit()

                    await bot.send_message(user_id, f'Ваш Инвестиционный Профиль:\n\n{user_invest_profile}', reply_markup=types.ReplyKeyboardRemove())
                    await bot.send_message(user_id, f'Чтобы пройти тест заново нажмите /start')
                elif otveti.otvet_7 == 'С' and otveti.otvet_9 == 'Да':
                    user_invest_profile = content.profiles['Агрессивный']
                    add_invest_profile = Invest_profile_tgbot(user_id=user_id, invest_profile = user_invest_profile)                        
                    session.merge(add_invest_profile)                                
                    session.commit()

                    await bot.send_message(user_id, f'Ваш Инвестиционный Профиль:\n\n{user_invest_profile}', reply_markup=types.ReplyKeyboardRemove())
                    await bot.send_message(user_id, f'Чтобы пройти тест заново нажмите /start')
                elif otveti.otvet_7 == 'С' and otveti.otvet_9 == 'Нет':
                    user_invest_profile = content.profiles['Умеренно Агрессивный']
                    add_invest_profile = Invest_profile_tgbot(user_id=user_id, invest_profile = user_invest_profile)                        
                    session.merge(add_invest_profile)                                
                    session.commit()

                    await bot.send_message(user_id, f'Ваш Инвестиционный Профиль:\n\n{user_invest_profile}', reply_markup=types.ReplyKeyboardRemove())
                    await bot.send_message(user_id, f'Чтобы пройти тест заново нажмите /start')

            # Следующий блок ответов для подсчетов 45-54 балов
        elif 45 <= summ_1_to_6_vopros <= 54:
            if otveti.otvet_7 == 'A':                             
                user_invest_profile = content.profiles['Умеренный']
                add_invest_profile = Invest_profile_tgbot(user_id=user_id, invest_profile = user_invest_profile)                        
                session.merge(add_invest_profile)                                
                session.commit()

                await bot.send_message(user_id, f'Ваш Инвестиционный Профиль:\n\n{user_invest_profile}', reply_markup=types.ReplyKeyboardRemove())
                await bot.send_message(user_id, f'Чтобы пройти тест заново нажмите /start')
            elif otveti.otvet_7 in ['B', 'C']:                             
                user_invest_profile = content.profiles['Агрессивный']
                add_invest_profile = Invest_profile_tgbot(user_id=user_id, invest_profile = user_invest_profile)                        
                session.merge(add_invest_profile)                                
                session.commit()

                await bot.send_message(user_id, f'Ваш Инвестиционный Профиль:\n\n{user_invest_profile}', reply_markup=types.ReplyKeyboardRemove())
                await bot.send_message(user_id, f'Чтобы пройти тест заново нажмите /start')
    except Exception as errory:
        logger.exception('Got exception', log_file="bot_log")
        error_tg_msg_raw = traceback.format_exc()

        # меняем скобки, тк библа для уведомлений ругается
        error_tg_msg_1 = error_tg_msg_raw.replace("<", "")
        error_tg_msg_clean = error_tg_msg_1.replace(">", "")
        # 
              
        finally_error_msg = f"""Ошибка в функции get_result.\n\nОписание:\n{error_tg_msg_clean}"""
        await send_tg_notification(finally_error_msg)
# конец фукнции расчета результата