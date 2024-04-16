import asyncio

import dotenv

from adapters.telegram_bot import main_bot

if __name__ == "__main__":
    dotenv.load_dotenv(".env")
    asyncio.run(main_bot())
