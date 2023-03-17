from telebot import telebot
import config

bot = telebot.TeleBot(config.token)

# В мене є така структура даних, чому код не працює?
Є папка Bot в якій є файли bot.py, config.py, create_bot.py
Змість файлу bot.py:
from create_bot import bot

bot.polling(none_stop=True, interval=0)
Змість файлу config.py:
import emoji

# Config

# Token
token = "5744786319:AAExxszjZLMA_-l1wVQiyEeLQL9papFxHyM"

# UA emoji coded
ua = "\U0001f1fa\U0001f1e6"

# Bones head (skull) череп emoji
skull = emoji.emojize(":skull_and_crossbones:")

# Fuck emoji
fuck = emoji.emojize(":middle_finger:")

# Bomb emoji
bomb = emoji.emojize(":bomb:")

# Russianwarship sticker
warship_sticker = "CAACAgIAAxkBAAEIKulkE5ZZpoIs0b7IxE_ahjaiaJp-lAACQRUAAuV36UkikVI6dDM5TC8E"

# Cry
cry_emoji = emoji.emojize(":cry:")

# List with words to "Donbass" message
bombs_list = ["бомбив", "бамбіл", "дамбив", "дамбіл", "домбив", "бомбил", "домбил"]
donbas_list = ["донбас", "бомбас", "бонбас", "бамбас"]
for word in list(donbas_list):
    donbas_list.append(word + "с")
    donbas_list.append(word + "с?")
    donbas_list.append(word + "?")

# List with words to russians warship message
russians_list = ["русский", "руский", "рускій", "русскій"]
military = ["военный", "военый", "воєний", "воєнний", "воений", "военний", "військовий"]
Зміст файлу create_bot.py:
from telebot import telebot
import config

bot = telebot.TeleBot(config.token)
Також в папці Bot є папка handlers з файлами commands.py, schedule.py, slogans.py
Зміст файлу commands.py:
from create_bot import bot

# /start command
@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(
        message, f"Вас вітає Поціновувач ПЛС!\n \
        <b>{message.from_user.first_name}</b> чим займемось сьогодні?", parse_mode='html')

# /help command
@bot.message_handler(commands=["help"])
def help(message):
    bot.reply_to(
        message, f"Я чатбот під назвою Поціновувач ПЛС, мене створив @Gorsun4ik, для захоплення світу, але поки я обмежений таким функціоналом:\n \
        Дійсно думали, що я викладу всі карти на стіл? Нііі, самі переписуйтесь і побачите що я вмію ")

# /developer command
@bot.message_handler(commands=["developer"])
bot.reply_to(
        message, f"Я поновелоний раб.\n мій власник @Gorsun4ik")
Зміст файлу schedule.py:
from datetime import datetime, strftime, now
from create_bot import bot

# Get day of week
today = datetime.datetime.now()
day_of_week = today.strftime("%A")

# Functions of seperate days
class SeperateDaysFunctions:

    # Tuesday
    def tuesday():
         for i in range(5):
            bot.reply_to(message,
                             f"<b>Розклад пар на вівторок:</b>\n \
                          {i}: 9:40-10:40 Диференціальні рівняння\n \
                          {i}: 10:50-11:50 Математичний аналіз\n \
                          {i}: 12:00-13:00 Технології(Основи програмування)\n \
                          {i}: 13:10-14:10 Алгоритми та структура даних\n \
                          {i}: 14:20-15:20 Історія: Україна і світ", parse_mode='html')

    # Wednsday
    def wednesday():
        for i in range(5):
                bot.reply_to(message,
                             f"<b>Розклад пар на середу:</b>\n \
                          {i}: 10:50-11:50 Географія, кабінет 413\n \
                          {i}: 12:00-13:00 Математи, кабінет 505\n \
                          {i}: 13:10-14:10 Алгоритми та структура даних, кабінет 201\n \
                          {i}: 14:20-15:20 Українська мова, кабінет 311\n \
                          {i}: 15:30-16:30 Українська література, кабінет 311",
                             parse_mode='html')

    # Thursday
    def thursday():
        for i in range(4):
                bot.reply_to(message,
                             f"<b>Розклад пар на четвер:</b>\n \
                          {i}: 9:40-10:40 Англійська, кабінет 420\n \
                          {i}: 10:50-11:50 Фіз-ра, спортзал\n \
                          {i}: 12:00-13:00 Фізика, кабінет 418\n \
                          {i}: 13:10-14:10 Математичний аналіз, кабінет 505", parse_mode='html')

    # Friday
    def friday():
        for i in range(3):
                bot.reply_to(message,
                             f"<b>Розклад пар на четвер:</b>\n \
                          {i}: 9:40-10:40 Диференціальні рівняння, кабінет 212\n \
                          {i}: 10:50-11:50 Технології(Основи програмування), кабінет 201\n \
                          {i}: 12:00-13:00 Технології(Основи програмування), кабінет 201", parse_mode='html')

# Today's schedule
class TodaySchedule:
    @bot.message_handler(func=lambda message: 'розклад' in message.text.lower())
    def schedule_message(message):

        # Вихідні
        if day_of_week == "Monday" \
                or day_of_week == "Saturday" \
                or day_of_week == "Sunday":
            bot.reply_to(
                message, f"<b>Сьогодні пар немає, можеш гуляти\nАбо напиши розклад <день тижня></b>", parse_mode='html')

        # Вівторок
        if day_of_week == "Tuesday":
           tuesday()

        # Середа
        if day_of_week == "Wednesday":
            wednesday()

        # Четвер
        if day_of_week == "Thursday":
            thursday()

        # П'ятниця
        if day_of_week == "Friday":
            friday()

# Seperate days schedule
class SeperateDaysSchedule:

    # Tuesday / Вівторок
    @bot.message_handler(func=lambda message: 'розклад вівторок' in message.text.lower())
    def schedule_message(message):
        tueday()
    
    # Wednesday / Середа
    @bot.message_handler(func=lambda message: 'розклад середа' in message.text.lower())
    def schedule_message(message):
        wednesday()
    
    # Thursday / Четвер
    @bot.message_handler(func=lambda message: 'розклад четвер' in message.text.lower())
    def schedule_message(message):
        thursday()
    
    # Friday / П'ятниця
    @bot.message_handler(func=lambda message: "розклад п'ятниця" in message.text.lower() or "розклад пятниця" in message.text.lower())
    def schedule_message(message):
        friday()
Зміст файлу slogans.py:
from create_bot import bot
from config import *

# Крим
@bot.message_handler(func=lambda message: 'крим' in message.text.lower())
def crimea_message(message):
    bot.reply_to(
        message, f"<b>Крим - це Україна{config.ua}</b>", parse_mode='html')

# Crimea
@bot.message_handler(func=lambda message: 'crimea' in message.text.lower())
def crimea_en_message(message):
    bot.reply_to(
        message, f"<b>Crimea - is Ukraine{config.ua}</b>", parse_mode='html')

# Йобана русня
@bot.message_handler(func=lambda message: 'йобана русня' in message.text.lower())
def fucking_russians_message(message):
    bot.reply_to(message, f"<b>Амінь!</b>", parse_mode='html')

# русні пизда
@bot.message_handler(func=lambda message: 'русні пизда' in message.text.lower())
def russians_were_fucked_message(message):
    bot.reply_to(message, "Воістину пизда!", parse_mode='html')

# шо там по русні?
@bot.message_handler(func=lambda message: 'шо там по русні' in message.text.lower() or
                     'шо по русні' in message.text.lower() or
                     'шо там по русні?' in message.text.lower() or
                     'шо по русні?' in message.text.lower())
def what_about_russians_message(message):
    bot.reply_to(message, "ₚусні пизда!", parse_mode='html')

# Пиши українською
@bot.message_handler(func=lambda message: 'крым' in message.text.lower() or
                     "крым?" in message.text.lower() or "украине" in message.text.lower() or
                     "украине!" in message.text.lower() or "нации" in message.text.lower() or
                     "нации!" in message.text.lower() or "нацие" in message.text.lower() or
                     "нацие!" in message.text.lower())
def type_ukrainian_message(message):
    bot.reply_to(message, f"<b>Пиши українською блять</b>", parse_mode='html')

# Какая разніца
@bot.message_handler(func=lambda message: 'какая разница' in message.text.lower()
                     or 'какая разница?' in message.text.lower()
                     or 'какая разніца' in message.text.lower()
                     or 'какая разніца?' in message.text.lower())
def what_is_the_different_message(message):
    bot.reply_to(message, f"<b>Велика. Можеш запитати в нього, але він й сам задається таким питанням @Armagedon_LoLWRF\n \
        Якщо все ж таки хочеш знайти відповідь - почитай історію.\n \
        Якщо коротко - причина по якій в Україні розмовляються російською - наслідок столітнього зросійщення нашого суспілсьтва.</b>", parse_mode='html')

# ПЛС
@bot.message_handler(func=lambda message: 'плс' in message.text.lower() or "pls" in message.text.lower())
def pls_message(message):
    bot.reply_to(message, f"<b>Слава ПЛС!\nНавіки Слава!</b>",
                 parse_mode='html')

# путін
@bot.message_handler(func=lambda message: 'путін' in message.text.lower() or "путин" in message.text.lower())
def putin_message(message):
    bot.reply_to(message, f"<b>путін - хуйло!\n \
        https://www.youtube.com/watch?v=447lXe1Y2tE&ab_channel=%D0%90%D0%BD%D0%BD%D0%B0%D0%A2.</b>", parse_mode='html')

# хто хуйло?
@bot.message_handler(func=lambda message: 'хто хуйло' in message.text.lower() or "хто хуйло?" in message.text.lower())
def huilo_message(message):
    bot.reply_to(
        message, f"<b>путін - хуйло!\nяк і вся русня - підараси</b>", parse_mode='html')

# Слава Україні!
@bot.message_handler(func=lambda message: 'слава україні' in message.text.lower()
                     or "слава україні" in message.text.lower())
def slava_ukraini_message(message):
    bot.reply_to(
        message, f"<b>Героям Слава!{config.ua}</b>", parse_mode='html')

# Тебе ображають?
@bot.message_handler(func=lambda message: 'тебе ображають' in message.text.lower() or
                     "тебе ображають" in message.text.lower()
                     or "тебе тут ображають" in message.text.lower()
                     or "тебе ображають?" in message.text.lower()
                     or "тебе тут ображають?" in message.text.lower())
def are_you_booling_message(message):
    bot.reply_to(message, f"<b>Так!</b>", parse_mode='html')

# слава раісі
@bot.message_handler(func=lambda message: 'слава россии' in message.text.lower()
                     or "слава росси" in message.text.lower()
                     or "слава росии" in message.text.lower()
                     or "слава россие" in message.text.lower()
                     or "слава рассие" in message.text.lower())
def slava_raisi_message(message):
    bot.reply_to(
        message, f"<b>Ти шо, йобу дав?\nКолядники вже в дорозі</b>", parse_mode='html')

# Хто такий морлок?
@bot.message_handler(func=lambda message: 'морлок' in message.text.lower()
                     or "morlok" in message.text.lower()
                     or "@Armagedon_LoLWRF" in message.text.lower()
                     or "@morlok" in message.text.lower())
def who_is_the_morlok_message(message):
    bot.reply_to(
        message, f"<b>А ви знали хто такий @Armagedon_LoLWRF ?\nЦе староста ПЛС!</b>", parse_mode='html')


# Йосип драний
@bot.message_handler(func=lambda message: 'йосип драний' in message.text.lower())
def yosup_dranii_message(message):
    bot.reply_to(message, f"це точно", parse_mode='html')

# Слава Нації!
@bot.message_handler(func=lambda message: 'слава нації!' in message.text.lower()
                     or "слава Слава нації" in message.text.lower())
def slava_natsii_message(message):
    bot.reply_to(
        message, f"<b>Смерть ворогам!{config.skull}</b>", parse_mode='html')

# Україна
@bot.message_handler(func=lambda message: 'україна' in message.text.lower()
                     or "україна?" in message.text.lower()
                     or "україна!" in message.text.lower())
def ukraina_ponad_use_message(message):
    bot.reply_to(
        message, f"<b>Україна - понад усе!{config.ua}</b>", parse_mode='html')

# Бандера
@bot.message_handler(func=lambda message: 'бандера' in message.text.lower()
                     or "бандера?" in message.text.lower()
                     or "бандера!" in message.text.lower())
def bandera_message(message):
    bot.reply_to(
        message, f"<b>Бандера - герой!{config.ua}</b>", parse_mode='html')

# Шухевич
@bot.message_handler(func=lambda message: 'Шухевич' in message.text.lower()
                     or "Шухевич?" in message.text.lower()
                     or "Шухевич!" in message.text.lower())
def suhevich_message(message):
    bot.reply_to(
        message, f"<b>Шухевич - герой!{config.ua}</b>", parse_mode='html')

# Glory to Ukraine!
@bot.message_handler(func=lambda message: "glory to ukraine!" in message.text.lower()
                     or "glory to ukraine" in message.text.lower()
                     or "glory ukraine" in message.text.lower()
                     or "glory ukraine!" in message.text.lower())
def glory_to_ukraine_message(message):
    bot.reply_to(
        message, f"<b>Glory to Heroes!{config.ua}</b>", parse_mode='html')

# Glory to nation!
@bot.message_handler(func=lambda message: 'nation' in message.text.lower()
                     or "nation?" in message.text.lower())
def glory_to_nation_message(message):
    bot.reply_to(
        message, f"<b>Death to enemies!{config.skull}</b>", parse_mode='html')

# Ukraine above All
@bot.message_handler(func=lambda message: 'ukraine' in message.text.lower()
                     or "ukraine!" in message.text.lower()
                     or "ukraine?" in message.text.lower())
def ukraine_above_all_message(message):
    bot.reply_to(
        message, f"<b>Ukraine - above all!{config.ua}</b>", parse_mode='html')

# Nerd
@bot.message_handler(func=lambda message: 'nerd' in message.text.lower()
    or 'nerd?' in message.text.lower()
    or 'ньорд' in message.text.lower()
    or 'нерд' in message.text.lower()
    or 'ботан' in message.text.lower()
    or 'розумний' in message.text.lower()
    or 'нёрд' in message.text.lower())
def nerd_message(message):
    bot.reply_to(message, "Cам ти ньорд", parse_mode='html')

# Donbass and russian's warship
@bot.message_handler()
def get_user_text(message):

     # Split input words and convert to set
    words = set(message.text.lower().split())

    # Донбас
    if len(words.intersection(config.bombs_list)) >= 1 and len(words.intersection(config.donbas_list)) >= 1:
        bot.reply_to(
            message, f"<b>Я дамбіл бамбас!{config.bomb}\nНу ще трохи @Gorsun4ik</b>", parse_mode='html')
    # Корабль
    if len(words.intersection(config.russians_list)) >= 1 and len(words.intersection(config.military)) >= 1:
        bot.reply_to(
            message, f"<b>Русский военный корабль - иди нахуй!{config.fuck}</b>", parse_mode='html')
        bot.send_sticker(message.chat.id, config.warship_sticker)

Що не так в цьому коді, чому він не працює?