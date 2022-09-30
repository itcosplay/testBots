from aiogram import executor
from handlers import dp
import os
import django


def setup_django():
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "bot_backend.bot_backend.settings"
    )

    os.environ.update(
        {'DJANGO_ALLOW_ASYNC_UNSAFE': "true"}
    )

    django.setup()


if __name__ == '__main__':    
    setup_django()

    executor.start_polling(dp, skip_updates=True)