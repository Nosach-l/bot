import asyncio
from aiogram import Router, F
from aiogram.filters import CommandStart, Command, CommandObject
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.utils.chat_action import ChatActionSender
from create_bot import questions, bot, admins
from filters.is_admin import IsAdmin
from keyboards.all_kb import main_kb, create_spec_kb
from keyboards.inline_kbs import create_qst_inline_kb
from aiogram.types import CallbackQuery


start_router = Router()


@start_router.message(CommandStart())
async def cmd_start(message: Message, command: CommandObject):
    command_args: str = command.args
    if command_args:
        await message.answer(
            f'Запуск сообщения по команде /start используя фильтр CommandStart() с меткой <b>{command_args}</b>',
            reply_markup=main_kb(message.from_user.id))
    else:
        await message.answer(
            f'Запуск сообщения по команде /start используя фильтр CommandStart() без метки',
            reply_markup=main_kb(message.from_user.id))


@start_router.message(F.text == 'GEO')
async def cmd_start(message: Message):
    await message.answer('Поделись чем не жалко', reply_markup=create_spec_kb())


@start_router.message(F.text == 'Давай инлайн!')
async def get_inline_btn_link(message: Message):
    await message.answer('Вот тебе инлайн клавиатура со ссылками!', reply_markup=create_qst_inline_kb(questions))


@start_router.callback_query(F.data == 'back_home')
async def back_home(call: CallbackQuery):
    await call.message.answer('переход на главную', reply_markup=main_kb(call.from_user.id))
    await call.answer()


@start_router.message(Command('faq'))
async def cmd_start_2(message: Message):
    await message.answer('Сообщение с инлайн клавиатурой с вопросами',
                         reply_markup=create_qst_inline_kb(questions))


@start_router.callback_query(F.data.startswith('qst_'))
async def cmd_start(call: CallbackQuery):
    await call.answer()
    qst_id = int(call.data.replace('qst_', ''))
    qst_data = questions[qst_id]
    msg_text = f'Ответ на вопрос {qst_data.get("qst")}\n\n' \
               f'<b>{qst_data.get("answer")}</b>\n\n' \
               f'Выбери другой вопрос:'
    async with ChatActionSender(bot=bot, chat_id=call.from_user.id, action="typing"):
        await asyncio.sleep(1)
        await call.message.answer(msg_text, reply_markup=create_qst_inline_kb(questions))


@start_router.message(F.text.lower().contains('охотник'))
async def cmd_start(message: Message, state: FSMContext):
    # отправка обычного сообщения
    await message.answer('Я думаю, что ты тут про радугу рассказываешь')

    # то же действие, но через объект бота
    await bot.send_message(chat_id=message.from_user.id, text='Для меня это слишком просто')

    # ответ через цитату
    msg = await message.reply('Ну вот что за глупости!?')

    # ответ через цитату, через объект bot
    await bot.send_message(chat_id=message.from_user.id, text='Хотя, это забавно...',
                           reply_to_message_id=msg.message_id)

    await bot.forward_message(chat_id=message.from_user.id, from_chat_id=message.from_user.id, message_id=msg.message_id)

    data_task = {'user_id': message.from_user.id, 'full_name': message.from_user.full_name,
                 'username': message.from_user.username, 'message_id': message.message_id, 'date': message.date}
    print(data_task)


@start_router.message(Command('test_edit_msg'))
async def cmd_start(message: Message, state: FSMContext):
    # Бот делает отправку сообщения с сохранением объекта msg
    msg = await message.answer('Отправляю сообщение')

    # Достаем ID сообщения
    msg_id = msg.message_id

    # Имитируем набор текста 2 секунды и отправляе В коде оставлены комментарии.
    # Единственное, на что нужно обратить внимание, — строка:
    # м какое-то сообщение
    async with ChatActionSender(bot=bot, chat_id=message.from_user.id, action="typing"):
        await asyncio.sleep(2)
        await message.answer('Новое сообщение')

    # Делаем паузу ещё на 2 секунды
    await asyncio.sleep(2)

    # Изменяем текст сообщения, ID которого мы сохранили
    await bot.edit_message_text(text='<b>Отправляю сообщение!!!</b>', chat_id=message.from_user.id, message_id=msg_id)


"""@start_router.message(F.text.lower().contains('подписывайся'), IsAdmin(admins))
async def process_find_word(message: Message):
    await message.answer('О, админ, здарова! А тебе можно писать подписывайся.')


@start_router.message(F.text.lower().contains('подписывайся'))
async def process_find_word(message: Message):
    await message.answer('В твоем сообщении было найдено слово "подписывайся", а у нас такое писать запрещено!')"""
