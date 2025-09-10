import asyncio
from typing import Set

from src.ClientTelegram import client_telegram
from src.IO import io

async def main():
    set_tasks: Set[asyncio.Task] = set()
    client_is_ready_to_start: asyncio.Event = asyncio.Event()

    async with asyncio.TaskGroup() as group:
        task_io = group.create_task(io.start(client_telegram, client_is_ready_to_start))
        set_tasks.add(task_io)
        task_io.add_done_callback(set_tasks.discard)

        task_client_telegram = group.create_task(client_telegram.start(client_is_ready_to_start))
        set_tasks.add(task_client_telegram)
        task_client_telegram.add_done_callback(client_telegram.stop)
        task_client_telegram.add_done_callback(set_tasks.discard)