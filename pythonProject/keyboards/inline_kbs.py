from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_inline_kb():
    inline_kb_list = [
        [InlineKeyboardButton(text="Генерировать пользователя", callback_data='get_person')],
        [InlineKeyboardButton(text="На главную", callback_data='back_home')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)


def create_qst_inline_kb(questions: dict) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for question_id, question_data in questions.items():
        builder.row(
            InlineKeyboardButton(
                text=question_data.get('qst'),
                callback_data=f'qst_{question_id}'
            )
        )
    builder.row(
        InlineKeyboardButton(
            text='На главную', callback_data='back_home'
        )
    )
    builder.adjust(1)
    return builder.as_markup()
