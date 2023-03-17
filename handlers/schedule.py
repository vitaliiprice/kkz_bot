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