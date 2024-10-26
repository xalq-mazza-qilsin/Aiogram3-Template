from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode
from aiogram.utils.i18n import I18n, FSMI18nMiddleware
from aiogram.fsm.storage.memory import MemoryStorage

from utils.db.postgres import Database
from data.config import BOT_TOKEN


db = Database()
bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

i18n = I18n(path="./locales", domain="messages")
I18n.set_current(i18n)
storage = MemoryStorage()
dispatcher = Dispatcher(storage=storage)
i18n_middleware = FSMI18nMiddleware(i18n=i18n)
i18n_middleware.setup(dispatcher)
