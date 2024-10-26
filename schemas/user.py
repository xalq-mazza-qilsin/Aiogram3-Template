from pydantic import BaseModel

from .language import LanguageEnum


class User(BaseModel):
    telegram_id: int
    username: str | None = None
    full_name: str | None = None
    language: LanguageEnum = LanguageEnum.EN
