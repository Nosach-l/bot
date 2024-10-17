import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from decouple import config
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import random

# from db_handler.db_class import PostgresHandler

# pg_db = PostgresHandler(config('PG_LINK'))
scheduler = AsyncIOScheduler(timezone='Europe/Moscow')
admins = [int(admin_id) for admin_id in config('ADMINS').split(',')]

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

bot = Bot(token=config('TOKEN'), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage())
questions = {
    1: {'qst': 'Большой куш', 'answer': random.choice([
        "Резкий, как удар серпом по яйцам, жёсткий, как удар молотом — живой советский герб.",
        "Вытащи свой язык из моей жопы, Гари",
        "- Где?\n"
        "- В Лондоне?\n"
        "- В Лондоне!\n"
        "- В Лондоне!?\n"
        "- Да, Лондоне!\n"
        "Ну, это там где рыба, чипсы, чай, дрянная еда, отвратная погода,\n"
        "Мэри - ебать ее в сраку-Поппинс, Лондон!!!"])},
    2: {'qst': 'Сколько континентов на Земле?', 'answer': 'Семь'},
    3: {'qst': 'Самая длинная река в мире?', 'answer': 'Нил'},
    4: {'qst': 'Какой элемент обозначается символом "O"?', 'answer': 'Кислород'},
    5: {'qst': 'Как зовут главного героя книги "Гарри Поттер"?', 'answer': 'Гарри Поттер'},
    6: {'qst': 'Сколько цветов в радуге?', 'answer': 'Семь'},
    7: {'qst': 'Какая планета третья от Солнца?', 'answer': 'Земля'},
    8: {'qst': 'Кто написал "Войну и мир"?', 'answer': 'Лев Толстой'},
    9: {'qst': 'Что такое H2O?', 'answer': 'Вода'},
    10: {'qst': 'Какой океан самый большой?', 'answer': 'Тихий океан'},
}
