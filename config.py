import emoji

# Config

# Token
token = "token"

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
