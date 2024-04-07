import os

from pydantic import StrictStr
from pydantic_settings import BaseSettings


class SiteSettings(BaseSettings):
    token: StrictStr = os.getenv("TOKEN", None)