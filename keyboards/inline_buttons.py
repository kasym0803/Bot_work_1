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
    referenc_button = InlineKeyboardButton(
        "Referall menu",
        callback_data="referall"
    )
    link_button = InlineKeyboardButton(
        'Заказы в Habr',
        callback_data='link_button'
    )
    markup.add(ques_button, link_button)
    markup.add(profile_button)
    markup.add(referenc_button)
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


async def like_dislike_keyboard():
    markup = InlineKeyboardMarkup()
    user_form_like_button = InlineKeyboardButton(
        "Like",
        callback_data=f"user_form_like",
    )
    user_form_dislike_button = InlineKeyboardButton(
        "Dislike",
        callback_data=f"user_form_dislike",
    )
    markup.add(user_form_like_button)
    markup.add(user_form_dislike_button)
    return markup


async def reference_button():
    markup = InlineKeyboardMarkup()
    reference_link_button = InlineKeyboardButton(
        "reference link",
        callback_data='reference_link'
    )
    reference_list_button = InlineKeyboardButton(
        "reference list",
        callback_data='reference_list'
    )

    markup.add(reference_link_button)
    markup.add(reference_list_button)
    return markup
