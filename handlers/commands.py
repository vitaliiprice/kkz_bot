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
