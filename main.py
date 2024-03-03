from highrise import BaseBot, Position
from highrise import SessionMetadata, User
from highrise import __main__
from asyncio import run as arun
from highrise import *
import asyncio
from highrise.models import*
from highrise import*
from flask import Flask
from threading import Thread
from highrise.__main__ import *
import time
import random
import asyncio
from highrise.models import (
    CurrencyItem,
    Item,
    SessionMetadata,
    User)


class Bot(BaseBot):
    def __init__(self):
        super().__init__()
  
    async def on_start(self, session_metadata: SessionMetadata) -> None:
        print("hi im alive?")
        self.highrise.tg.create_task(self.highrise.teleport(
            session_metadata.user_id, Position(16.0, 0.25, 13.5, "FrontLeft")))

    async def on_chat(self, user: User, message: str) -> None:  
      
        if message.startswith("!cuzdan") and user.username in ["karainek", "maykilanderson"] or message.startswith("!cüzdan") and user.username in ["karainek", "maykilanderson"]:
            wallet = (await self.highrise.get_wallet()).content
            await self.highrise.chat(
                f"Benim {wallet[0].amount} {wallet[0].type}um var")


    async def run(self, room_id, token) -> None:
        await __main__.main(self, room_id, token)
class WebServer():

  def __init__(self):
    self.app = Flask(__name__)

    @self.app.route('/')
    def index() -> str:
      return "Alive"

  def run(self) -> None:
    self.app.run(host='0.0.0.0', port=8080)

  def keep_alive(self):
    t = Thread(target=self.run)
    t.start()

web_server = WebServer()
app = web_server.app

    
class RunBot():
  room_id = "65bf7e2a71224cfff859496c"
  bot_token = "1acd8c655c489bba77030032951e9f733e3415df3bd09795924670cf514390ee"
  bot_file = "main"
  bot_class = "Bot"

  def __init__(self) -> None:
    self.definitions = [
        BotDefinition(
            getattr(import_module(self.bot_file), self.bot_class)(),
            self.room_id, self.bot_token)
    ]

  def run_loop(self) -> None:
    while True:
      try:
        arun(main(self.definitions)) 
      except Exception as e:
        print("Error: ", e)
        time.sleep(5)


if __name__ == "__main__":
  WebServer().keep_alive()

  RunBot().run_loop()