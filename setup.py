import asyncio 

from src.main import telegram_client

async def setup_application() -> None:
    async with asyncio.TaskGroup() as task_group:
        task_run_telegram_client = task_group.create_task(telegram_client)

if __name__ == '__main__':
    asyncio.run(setup_application())