# This Python file uses the following encoding: utf-8
import os

from aiogram.utils.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton


start_btn = InlineKeyboardButton('Да', callback_data='start_quiz')
dont_start_btn = InlineKeyboardButton('Нет', callback_data='dont_start_quiz')
quiz = InlineKeyboardMarkup().add(start_btn).add(dont_start_btn)

answerz = CallbackData('answer', 'vopros_id', 'user_answer')


vopros_1_text =  """<b>1. Выберите главную цель инвестирования.</b>\n\n<b> - A.</b> Я хочу сохранить ценность моих инвестиций и свести к минимуму риски потерь.\n\n<b> - B.</b> Мне важно чтобы инвестиции приносили текущий доход не в ущерб сохранности капитала.\n\n<b> - C.</b> Мне необходимо получать доход от инвестиций. Также я готов подвергнуть мой капитал небольшому риску, чтобы он рос со временем.\n\n<b> - D.</b> Для меня важнее нарастить капитал со временем, для этого я готов пойти на умеренный уровень риска, а также хотел бы получать текущий доход.\n\n<b> - E.</b> Моя цель — существенно увеличить стоимость своего капитала в будущем, для этого я готов пойти на значительные риски. Текущая доходность не является приоритетом."""

# ВОПРОС 1, ОТВЕТЫ
vopros_1_a = InlineKeyboardButton('A', callback_data=answerz.new(vopros_id=1, user_answer='A'))
vopros_1_b = InlineKeyboardButton('B', callback_data=answerz.new(vopros_id=1, user_answer='B'))
vopros_1_c = InlineKeyboardButton('C', callback_data=answerz.new(vopros_id=1, user_answer='C'))
vopros_1_d = InlineKeyboardButton('D', callback_data=answerz.new(vopros_id=1, user_answer='D'))
vopros_1_e = InlineKeyboardButton('E', callback_data=answerz.new(vopros_id=1, user_answer='E'))
vopros_1_btn = InlineKeyboardMarkup().add(vopros_1_a,vopros_1_b).add(vopros_1_c,vopros_1_d).add(vopros_1_e)


# ВОПРОС 2, ОТВЕТЫ
current_dir_path = os.path.dirname(__file__)
pic_2_file = "volatilnost.png"
pic_2_file_path = os.path.join(current_dir_path, pic_2_file)

vopros_2_text =  """<b>2. Волатильность – это колебание цены на актив. Чем выше волатильность инструмента, тем выше потенциал роста инвестиций на долгосрочном горизонте, при этом риски тоже растут. С какой волатильностью вам комфортно инвестировать?</b>\n\n<b> - A.</b> Как можно ниже. Я отдаю предпочтение активам со стабильной ценой, даже если это означает небольшую доходность.\n\n<b> - B.</b> Допускаю небольшую волатильность. Я готов к возможным потерям в стоимости, если мои инвестиции смогут от этого вырасти со временем.\n\n<b> - C.</b> Волатильность может быть больше, если мои инвестиции имеют значительный потенциал для роста с течением времени.\n\n<b> - D.</b> Я готов к высокой волатильности и значительным рискам в расчете получить максимальную прибыль от инвестиций."""

vopros_2_a = InlineKeyboardButton('A', callback_data=answerz.new(vopros_id=2, user_answer='A'))
vopros_2_b = InlineKeyboardButton('B', callback_data=answerz.new(vopros_id=2, user_answer='B'))
vopros_2_c = InlineKeyboardButton('C', callback_data=answerz.new(vopros_id=2, user_answer='C'))
vopros_2_d = InlineKeyboardButton('D', callback_data=answerz.new(vopros_id=2, user_answer='D'))
vopros_2_back = InlineKeyboardButton('Назад', callback_data='start_quiz')
vopros_2_btn = InlineKeyboardMarkup().add(vopros_2_a, vopros_2_b).add(vopros_2_c, vopros_2_d).add(vopros_2_back)
##################################################################

# ВОПРОС 3, ОТВЕТЫ
vopros_3_text =  """<b>3. Наиболее консервативные инвестиции могут давать доходность ниже инфляции. Это может привести к риску потери покупательной способности. Что из нижеперечисленного наиболее соответствует вашим инвестиционным целям?</b>\n\n<b> - A.</b> Мои инвестиции должны быть безопасными, даже если их доходность немного не успевает за инфляцией.\n\n<b> - B.</b> Я готов пойти на незначительный риск, чтобы мои инвестиции росли примерно на уровне инфляции.\n\n<b> - C.</b> Мои инвестиции должны расти немного быстрее инфляции, для этого я готов пойти на умеренные риски.\n\n<b> - D.</b> Мои инвестиции должны значительно обгонять уровень инфляции, для этого я готов пойти на существенные риски."""

vopros_3_a = InlineKeyboardButton('A', callback_data=answerz.new(vopros_id=3, user_answer='A'))
vopros_3_b = InlineKeyboardButton('B', callback_data=answerz.new(vopros_id=3, user_answer='B'))
vopros_3_c = InlineKeyboardButton('C', callback_data=answerz.new(vopros_id=3, user_answer='C'))
vopros_3_d = InlineKeyboardButton('D', callback_data=answerz.new(vopros_id=3, user_answer='D'))
vopros_3_back = InlineKeyboardButton('Назад', callback_data=answerz.new(vopros_id=1, user_answer='back'))
vopros_3_btn = InlineKeyboardMarkup().add(vopros_3_a, vopros_3_b).add(vopros_3_c, vopros_3_d).add(vopros_3_back)
################################################

# ВОПРОС 4, ОТВЕТЫ
vopros_4_text =  """<b>4. В зависимости от суммы принимаемого риска, стоимость инвестиций со временем будет колебаться. С каким общим процентом потерь за год вы пересмотрите свое отношение к риску?</b>"""

vopros_4_a = InlineKeyboardButton('A. До –5%', callback_data=answerz.new(vopros_id=4, user_answer='A'))
vopros_4_b = InlineKeyboardButton('B. От –5% до –10%', callback_data=answerz.new(vopros_id=4, user_answer='B'))
vopros_4_c = InlineKeyboardButton('C. От –10% до –15%', callback_data=answerz.new(vopros_id=4, user_answer='C'))
vopros_4_d = InlineKeyboardButton('D. От –15% до –25%', callback_data=answerz.new(vopros_id=4, user_answer='D'))
vopros_4_e = InlineKeyboardButton('E. –25% и более', callback_data=answerz.new(vopros_id=4, user_answer='E'))
vopros_4_back = InlineKeyboardButton('Назад', callback_data=answerz.new(vopros_id=2, user_answer='back'))
vopros_4_btn = InlineKeyboardMarkup().add(vopros_4_a, vopros_4_b).add(vopros_4_c, vopros_4_d).add(vopros_4_e).add(vopros_4_back)
################################################

# ВОПРОС 5, ОТВЕТЫ
vopros_5_text =  """<b>5. Вам предложили два вида инвестиций:</b>\n\n <b>- Инвестиции А.</b> Обеспечивают небольшую среднегодовую доходность 8% с минимальными рисками.\n\n <b>- Инвестиции В.</b> Обеспечивают среднегодовую доходность в размере 15%, но с возможностью в потерять 25% от инвестиций в один из годовых периодов.\n\nРаспределите свой капитал между этими двумя инвестициями.\n\n<b> - A.</b> 100% в инвестиции A и 0% в инвестиции B\n\n<b> - B.</b> 80% в инвестиции A и 20% в инвестиции B\n\n<b> - C.</b> 50% в инвестиции A и 50% в инвестиции B\n\n<b> - D.</b> 20% в инвестиции A и 80% в инвестиции B\n\n<b> - E.</b> 0% в инвестиции A и 100% в инвестиции B"""

pic_5_file = "vopros_5.png"
pic_5_file_path = os.path.join(current_dir_path, pic_5_file)

vopros_5_a = InlineKeyboardButton('A', callback_data=answerz.new(vopros_id=5, user_answer='A'))
vopros_5_b = InlineKeyboardButton('B', callback_data=answerz.new(vopros_id=5, user_answer='B'))
vopros_5_c = InlineKeyboardButton('C', callback_data=answerz.new(vopros_id=5, user_answer='C'))
vopros_5_d = InlineKeyboardButton('D', callback_data=answerz.new(vopros_id=5, user_answer='D'))
vopros_5_e = InlineKeyboardButton('E', callback_data=answerz.new(vopros_id=5, user_answer='E'))
vopros_5_back = InlineKeyboardButton('Назад', callback_data=answerz.new(vopros_id=3, user_answer='back'))
vopros_5_btn = InlineKeyboardMarkup().add(vopros_5_a, vopros_5_b).add(vopros_5_c, vopros_5_d).add(vopros_5_e).add(vopros_5_back)
################################################

# ВОПРОС 6, ОТВЕТЫ
vopros_6_text =  """<b>6. Если бы вы могли выбрать только один из пяти гипотетических портфелей, какой вариант вам подходит?</b>"""

pic_6_file = "vopros_6.png"
pic_6_file_path = os.path.join(current_dir_path, pic_6_file)

vopros_6_a = InlineKeyboardButton('A. Портфель A', callback_data=answerz.new(vopros_id=6, user_answer='A'))
vopros_6_b = InlineKeyboardButton('B. Портфель B', callback_data=answerz.new(vopros_id=6, user_answer='B'))
vopros_6_c = InlineKeyboardButton('C. Портфель С', callback_data=answerz.new(vopros_id=6, user_answer='C'))
vopros_6_d = InlineKeyboardButton('D. Портфель D', callback_data=answerz.new(vopros_id=6, user_answer='D'))
vopros_6_e = InlineKeyboardButton('E. Портфель E', callback_data=answerz.new(vopros_id=6, user_answer='E'))
vopros_6_back = InlineKeyboardButton('Назад', callback_data=answerz.new(vopros_id=4, user_answer='back'))
vopros_6_btn = InlineKeyboardMarkup().add(vopros_6_a, vopros_6_b).add(vopros_6_c, vopros_6_d).add(vopros_6_e).add(vopros_6_back)
################################################

# ВОПРОС 7, ОТВЕТЫ
vopros_7_text =  """<b>7. Как скоро вам потребуются весь ваш инвестиционный капитал или значительная его часть?</b>"""

vopros_7_a = InlineKeyboardButton('A. Короткий срок – от 0 до 3 лет', callback_data=answerz.new(vopros_id=7, user_answer='A'))
vopros_7_b = InlineKeyboardButton('B. Средний срок – от 3 до 8 лет', callback_data=answerz.new(vopros_id=7, user_answer='B'))
vopros_7_c = InlineKeyboardButton('C. Длинный срок – более 8 лет', callback_data=answerz.new(vopros_id=7, user_answer='C'))
vopros_7_back = InlineKeyboardButton('Назад', callback_data=answerz.new(vopros_id=5, user_answer='back'))
vopros_7_btn = InlineKeyboardMarkup().add(vopros_7_a).add(vopros_7_b).add(vopros_7_c).add(vopros_7_back)
#############################################################

# ВОПРОС 8, ОТВЕТЫ
vopros_8_text =  """<b>8. Ваши инвестиционные активы превышают сумму 50 миллионов рублей?</b>"""

vopros_8_a = InlineKeyboardButton('Да', callback_data=answerz.new(vopros_id=8, user_answer='Да'))
vopros_8_b = InlineKeyboardButton('Нет', callback_data=answerz.new(vopros_id=8, user_answer='Нет'))
vopros_8_back = InlineKeyboardButton('Назад', callback_data=answerz.new(vopros_id=6, user_answer='back'))
vopros_8_btn = InlineKeyboardMarkup().add(vopros_8_a, vopros_8_b).add(vopros_8_back)
#############################################################

# ВОПРОС 9, ОТВЕТЫ
vopros_9_text =  """<b>9. Сумма, которую вы инвестируете, составляет меньше 10% от ваших общих инвестиционных активов?</b>"""

vopros_9_a = InlineKeyboardButton('Да', callback_data=answerz.new(vopros_id=9, user_answer='Да'))
vopros_9_b = InlineKeyboardButton('Нет', callback_data=answerz.new(vopros_id=9, user_answer='Нет'))
vopros_9_back = InlineKeyboardButton('Назад', callback_data=answerz.new(vopros_id=8, user_answer='back'))
vopros_9_btn = InlineKeyboardMarkup().add(vopros_9_a, vopros_9_b).add(vopros_9_back)

vopros_9back_end = vopros_9_back = InlineKeyboardButton('Назад', callback_data=answerz.new(vopros_id=9, user_answer='back'))
vopros_9_btns_end = InlineKeyboardMarkup().add(vopros_9back_end)

voprosi = {
    1:vopros_1_text,
    2:vopros_2_text,
    3:vopros_3_text,
    4:vopros_4_text,
    5:vopros_5_text,
    6:vopros_6_text,
    7:vopros_7_text,
    8:vopros_8_text,
    9:vopros_9_text
}

answer_buttons = {
    1:vopros_1_btn,
    2:vopros_2_btn,
    3:vopros_3_btn,
    4:vopros_4_btn,
    5:vopros_5_btn,
    6:vopros_6_btn,
    7:vopros_7_btn,
    8:vopros_8_btn,
    9:vopros_9_btn
}

points_otvet_1 = {"A":1, "B":3, "C":5, "D":7, "E":9}
points_otvet_2 = {"A":1, "B":3, "C":7, "D":9}
points_otvet_3 = {"A":1, "B":3, "C":5, "D":9}
points_otvet_4 = {"A":1, "B":3, "C":5, "D":7, "E":9}
points_otvet_5 = {"A":1, "B":3, "C":5, "D":7, "E":9}
points_otvet_6 = {"A":1, "B":3, "C":5, "D":7, "E":9}



profiles = {
        "Консервативный": "<b>Консервативный</b>\n\n<b> - Акции 20%</b>\n<b> -  Облигации 55%</b>\n<b> - Деньги 25%</b>\n\nПодходит для инвесторов, которые преимущественно не склонны к риску.\n\nОсновное внимание направлено на стабильность портфеля и сохранность капитала с поправкой на инфляцию. Данная модель позволяет инвестору получать небольшую инвестиционную доходность за счет высоколиквидных инструментов с низким уровнем риска.\n\nТиповой портфель сильно смещен в сторону инвестиций в денежные средства и инвестиции с фиксированным доходом.",

        "Умеренно Консервативный": "<b>Умеренно-консервативный</b>\n\n<b> - Акции 40%</b>\n<b> -  Облигации 50%</b>\n<b> - Деньги 10%</b>\n\nПодходит для инвесторов, склонных к незначительному риску.\n\nОсновное внимание направлено на небольшой стабильный рост портфеля с низкой волатильностью и минимальными рисками потерь.\n\nТиповой портфель будет включать, прежде всего, денежные средства и инвестиции с фиксированным доходом с небольшой долей акций.",

        "Умеренный": "<b>Умеренный</b>\n\n<b> - Акции 60%</b>\n<b> -  Облигации 35%</b>\n<b> - Деньги 5%</b>\n\nПодходит для инвесторов, которые готовы принять умеренные риски.\n\nОсновное внимание направлено на баланс между стабильностью портфеля и ростом стоимости портфеля. Инвесторы, которые выбирают данную модель, готовы к определенной волатильности активов.\n\nТиповой портфель будет в основном сбалансирован между инвестициями с фиксированным доходом и акциями.",

        "Умеренно Агрессивный": "<b>Умеренно-агрессивный</b>\n\n<b> - Акции 70%</b>\n<b> -  Облигации 25%</b>\n<b> - Деньги 5%</b>\n\nПодходит для инвесторов, которые готовы принять средний уровень риска.\n\nСоотношение активов в портфеле позволяет получить значительный рост стоимости портфеля со временем. Инвесторы, использующие эту модель, должны быть готовы к повышенной волатильности своего портфеля.\n\nТиповой портфель включает в себя различные классы активов, основную часть из которых представляют акции.",

        "Агрессивный": "<b>Агрессивный</b>\n\n<b> - Акции 80%</b>\n<b> -  Облигации 15%</b>\n<b> - Деньги 5%</b>\n\nДля инвесторов, которые готовы пойти на значительный риск.\n\nОсновное внимание направлено на рост стоимости портфеля выше среднего на долгосрочном горизонте. В данной модели инвесторы готовы к высокой волатильности портфеля и значительным рискам в расчете получить максимальную прибыль от инвестиций.\n\nТиповой портфель включает различные классы активов, при этом сильно смещен в сторону акций."
}
