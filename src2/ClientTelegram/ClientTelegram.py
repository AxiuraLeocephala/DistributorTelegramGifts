from asyncio import Event

from pyrogram import Client

from src.settings import CONFIG_CLIENT_TELEGRAM

class ClientTelegram(Client):
    __instance: "ClientTelegram" = None
    __is_exist: bool = False
    config_client_telegram = CONFIG_CLIENT_TELEGRAM

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    
    def __del__(self):
        ClientTelegram.__instance = None
        ClientTelegram.__is_exist = False

    def __init__(self):
        if self.__is_exist:
            return
        self.__is_exist = True

        super().__init__(*self.config_client_telegram.values())

    async def start(self, client_is_ready_to_start: Event):
        await client_is_ready_to_start.wait()
