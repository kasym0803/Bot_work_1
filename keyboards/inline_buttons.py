from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def start_keyboard():
    markup = InlineKeyboardMarkup()
    ques_button = InlineKeyboardButton(
        "Start Questionnaire",
        callback_data="start_questionnaire"
    )
    profile_button = InlineKeyboardButton(
        "view profile",
        callback_data="random_profiles"
    )
    markup.add(ques_button)
    markup.add(profile_button)
    return markup


async def questionnaire_one_keyboard():
    markup = InlineKeyboardMarkup()
    yes_button = InlineKeyboardButton(
        "Yes",
        callback_data="hungry_yes"
    )
    no_button = InlineKeyboardButton(
        "No",
        callback_data="hungry_no"
    )
    markup.add(yes_button)
    markup.add(no_button)
    return markup


async def admin_keyboard():
    markup = InlineKeyboardMarkup()
    admin_user_list_button = InlineKeyboardButton(
        "User_list",
        callback_data="admin_user_list"
    )
    markup.add(admin_user_list_button)
    return markup


async def like_dislike_keyboard(owner_tg_id):
    markup = InlineKeyboardMarkup()
    user_form_like_button = InlineKeyboardButton(
        "Like",
        callback_data=f"user_form_like{owner_tg_id}",
    )
    user_form_dislike_button = InlineKeyboardButton(
        "Dislike",
        callback_data=f"random_profile"
    )
    markup.add(user_form_like_button)
    markup.add(user_form_dislike_button)
    return markup


