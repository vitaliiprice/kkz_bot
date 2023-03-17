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
