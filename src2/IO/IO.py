from asyncio import Event

from pyrogram import enums
from pyrogram.errors import BadRequest, SessionPasswordNeeded
from pyrogram.types import User

from src.ClientTelegram import ClientTelegram
from src.Data.TypeSentedCode import SENT_CODE_DESCRIPTIONS

class IO:
    __instance: "IO" = None
    __is_exist: bool = False

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    
    def __del__(self):
        IO.__instance = None
        IO.__is_exist = False

    def __init__(self):
        if self.__is_exist:
            return
        self.__is_exist = True

    async def start(self, client_telegram: ClientTelegram, client_is_ready_to_start: Event) -> None:
        print("Welcome. DistributorTelegramGifts is a program that allows you to " \
            "buy gifts on Telegram without taking a direct part in it.")
        
        await self.prepare_client_telegram_to_start(client_telegram)
        client_is_ready_to_start.set()
        self.start_io()

    async def prepare_client_telegram_to_start(self, client_telegram: ClientTelegram):
        while True:
            while True:
                if not client_telegram.config_client_telegram['phone_number']:
                    while True:
                        value = input('Enter phone number: ')
                        if value == "":
                            continue
                        
                        perform = (input(f'Is {value} correct? (y/n): ')).lower()
                        if perform == "y":
                            phone_number = value
                            client_telegram.config_client_telegram['phone_number'] = phone_number
                            break

                try:
                    sent_code = await client_telegram.send_code(value)
                except BadRequest as e:
                    print(e.MESSAGE)
                    continue
                else:
                    break

            print(f'The confirmation code has been sent via {SENT_CODE_DESCRIPTIONS[sent_code.type]}')

            while True:
                if not client_telegram.config_client_telegram['phone_code']:
                    while True:
                        value = input('Enter confirmation code')
                        if value == "":
                            continue

                        perform = (input(f'Is {value} correct? (y/n): ')).lower()
                        if perform == "y":
                            phone_code = value
                            client_telegram.config_client_telegram['phone_code'] = phone_code
                            break

                try:
                    signed_in = await client_telegram.sign_in(phone_number, sent_code.phone_code_hash, phone_code)
                except BadRequest as e:
                    print(e.MESSAGE)
                    continue
                except SessionPasswordNeeded as e:
                    print(e.MESSAGE)
                    
                    while True:
                        if not client_telegram.config_client_telegram['phone_code']:
                            value = input('Enter password: ')
                            if value == "":
                                continue

                            perform = (input(f'Is {value} correct? (y/n): ')).lower()
                            if perform == "y":
                                password = value
                                client_telegram.config_client_telegram['password'] = password
                                break
                        
                        try:
                            await client_telegram.check_password(password)
                            return
                        except BadRequest as e:
                            print(e.MESSAGE)
                else:
                    break

            if isinstance(signed_in, User):
                return
            else:
                print(f'the user with the number {phone_number} is not registered')
                continue

    def start_io(self):
        while True:
            value = input("> ")

            match value:
                case "help":
                    print("")
                case "stop":
                    self.handle_command_stop()

    def handle_command_stop(self):
        print("")