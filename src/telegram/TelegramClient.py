from typing import Union

from pyrogram import Client

class TelegramClient(Client):
    __instance: "TelegramClient" = None
    __is_exist: bool = False

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    
    def __del__(self):
        self.__instance = None
        self.__is_exist = False

    def __init__(self, api_id: Union[int, str], api_hash: str):
        if self.__is_exist:
            return 
        else:
            self.__is_exist = True

        super().__init__("client", api_id, api_hash)