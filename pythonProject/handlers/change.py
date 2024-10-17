import asyncio

from aiogram import Router, F
from aiogram.filters import CommandStart, Command, CommandObject
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.utils.chat_action import ChatActionSender

from create_bot import questions, bot, admins
from keyboards.all_kb import main_kb, create_spec_kb, create_rat
from keyboards.inline_kbs import ease_link_kb, get_inline_kb, create_qst_inline_kb
from aiogram.types import CallbackQuery


start_router = Router()


@start_router.message(Command('test_edit_msg'))
async def cmd_start(message: Message, state: FSMContext):
    new_msg = await bot.copy_message(
        chat_id=message.from_user.id,
        from_chat_id=message.from_user.id,
        message_id=message.message_id
    )
    await message.delete()
    await bot.edit_message_text(
        text='<b>Отправляю сообщение!!!</b>',
        chat_id=message.from_user.id,
        message_id=new_msg.message_id
    )