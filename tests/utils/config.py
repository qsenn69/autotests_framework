import os
from dotenv import load_dotenv
import configparser
from pathlib import Path

load_dotenv()

class Config:
    BASE_URL = os.getenv("BASE_URL", "https://www.aviasales.ru/")
    USERNAME = os.getenv("USERNAME")
    PASSWORD = os.getenv("PASSWORD")
    BROWSER = os.getenv("BROWSER", "chromium")
    HEADLESS = os.getenv("HEADLESS", "True").lower() == "true"
    ELEMENT_SEARCH_TIMEOUT_S = int(os.getenv("ELEMENT_SEARCH_TIMEOUT_S", "10"))

    _locators_cache = None

    @classmethod
    def _load_locators(cls):
        if cls._locators_cache is None:
            config = configparser.ConfigParser()
            path = Path(__file__).parent.parent / "configs" / "locators.conf"
            if not path.exists():
                raise FileNotFoundError(f"locators.conf не найден: {path}")
            config.read(path, encoding="utf-8")
            cls._locators_cache = config
        return cls._locators_cache

    @classmethod
    def locator(cls, section: str, key: str) -> str:
        """
        Получить локатор из locators.conf
        Пример: Config.locator("header", "search_button")
        """
        return cls._load_locators()[section][key]