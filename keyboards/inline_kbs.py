from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


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
            text='На главную',
            callback_data='back_home'
        )
    )
    builder.adjust(1)
    return builder.as_markup()
