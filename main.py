from highrise import BaseBot, Position
from highrise import SessionMetadata, User
from highrise import __main__
from asyncio import run as arun
from typing import Any, Dict, Union
from highrise import *
import asyncio
from highrise.models import*
from highrise import*
from asyncio import Task
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
        self.dilenme_active = False
        self.first_word = None
        self.third_word = None
  
    async def on_start(self, session_metadata: SessionMetadata) -> None:
        print("hi im alive?")
        self.highrise.tg.create_task(self.highrise.teleport(
            session_metadata.user_id, Position(16.0, 0.25, 13.5, "FrontLeft")))

    async def on_whisper(self, user: User, message: str) -> None:
        """On a received room whisper."""
        print(f"[WHISPER] {user.username} {message}")
        if message.startswith('/') and user.username in ["karainek"]:
            try:
                xxx = message[1:]
                await self.highrise.chat(xxx)
            except:
                print("error 3")
  
    async def on_emote(self, user: User, emote_id: str, receiver: User | None) -> None:
        """On a received emote."""
        print(f"{user.username} {emote_id}")
  

    async def on_tip(self, sender: User, receiver: User, tip: CurrencyItem | Item) -> None:
        tip_message = f"{sender.username} sent {tip.amount} golds to {receiver.username}"
        print(tip_message)


        self.first_word = tip_message.split()[0]
        

        words = tip_message.split()
        if len(words) >= 3:
            self.third_word = words[2]


        if receiver.username == "kelavana":
            if self.third_word == "1":
                response_message = f"بردن @{self.first_word}"
                await self.highrise.chat(response_message)
                await self.highrise.chat(f"یک طلا، زیر یک طلاست، خدا از تو راضی باشد 🙏 {self.first_word}")
            elif self.third_word == "5":
                response_message = f"بردن @{self.first_word}"
                await self.highrise.chat(response_message)
                await self.highrise.chat(f"تو به من 5 طلا دادی، خدا به تو 500 بده 🙏 {self.first_word}")
            elif self.third_word == "10":
                response_message = f"بردن @{self.first_word}"
                await self.highrise.chat(response_message)
                await self.highrise.chat(f"خدا از تو ده برابر راضی باشد 🙏 {self.first_word}")
            elif self.third_word == "50":
                response_message = f"بردن @{self.first_word}"
                await self.highrise.chat(response_message)
                await self.highrise.chat(f"خدا بخواهد تا دست زدی چیزت طلا شود 🙏 50 طلا برای من بسیار ارزشمند است 🥺{self.first_word}")
            elif self.third_word == "100":
                response_message = f"بردن @{self.first_word}"
                await self.highrise.chat(response_message)
                await self.highrise.chat(f"اوه خدایا، هر آرزویی داری برآورده شود، خدا از تو صد برابر راضی باشد 🙏 {self.first_word}")
            elif self.third_word == "500":
                response_message = f"بردن @{self.first_word}"
                await self.highrise.chat(response_message)
                await self.highrise.chat(f"تو یک انسان فوق‌العاده زیبا هستی. من عاشقتم... من را پیدا کن!! 🙏 {self.first_word}")
            elif self.third_word == "1000":
                response_message = f"بردن @{self.first_word}"
                await self.highrise.chat(response_message)
                await self.highrise.chat(f"هزار چیز چیزیست؟! {self.first_word}")
            elif self.third_word == "5000":
                response_message = f"بردن @{self.first_word}"
                await self.highrise.chat(response_message)
                await self.highrise.chat(f"به دلیل امکان‌پذیر نبودن، اینجا چیزی نمی‌نویسم... {self.first_word}")
            elif self.third_word == "10000":
                response_message = f"بردن @{self.first_word}"
                await self.highrise.chat(response_message)
                await self.highrise.chat(f"امکان‌پذیر نیست {self.first_word}")

              
    async def on_chat(self, user: User, message: str) -> None:

        if message.startswith("!cuzdan") and user.username in ["karainek", "maykilanderson"] or message.startswith("!cüzdan") and user.username in ["karainek", "maykilanderson"]:
            wallet = (await self.highrise.get_wallet()).content
            await self.highrise.chat(
                f"Benim {wallet[0].amount} {wallet[0].type}um var")

        if user.username.lower() == self.first_word:
            await self.highrise.react("heart", user.id)
      
        exclude_users = ["karainek", "inek.harun", "dilenenbot", "kelavana"]

        if message.lower().startswith("!beg") and user.username in ["karainek", "maykilanderson"]:
            if not self.dilenme_active:
                self.dilenme_active = True
                while self.dilenme_active:
                    room_data = (await self.highrise.get_room_users()).content
                    eligible_users = [u[0] for u in room_data if u[0].id != user.id and u[0].username not in exclude_users]

                    if not eligible_users:
                        await asyncio.sleep(10)
                    else:
                        selected_user = random.choice(eligible_users)
                        selected_user_position = [u[1] for u in room_data if u[0].id == selected_user.id][0]
                       
                        try:
                            nearby_position = Position(selected_user_position.x, selected_user_position.y, selected_user_position.z + 1.0)
                        except AttributeError:
                            print("Error: Could not calculate nearby_position due to missing attributes.")
                            pass

                        await self.highrise.walk_to(nearby_position)
                        await asyncio.sleep(3)

                        response_options = [
    f"آیا ممکن است یک کمی طلا به عنوان امانت زیبایی تو را بپردازم؟ 🙏؟ @{selected_user.username}",
    f"تو از طلا قابل قیمت‌تری، برای همین برای من یک ارزش داره. آیا یکم از طلاهات را به من بده میل داری؟ 🥺؟ @{selected_user.username}",
    f"سلام برادر، خواهر! اگر کمی طلا به من بدهی، به دعاگوی تو تبدیل می‌شوم 😢! @{selected_user.username}",
    f"اشتباه متوجه نشوید، فقط برای خوراک نون تقاضا دارم! یک طلا به من خیلی می‌شود؟ 😭! @{selected_user.username}",
    f"شما هر چیزی که به آن فکر می‌کنید را موفق می‌کنید، چون شما یک قدرت و عشق باورنکردنی دارید! این قدرت و عشق را با من به اشتراک بگذارید و یکمی از طلا برای من بفرستید لطفاً 👉🏾👈🏾؟ @{selected_user.username}",
    f"سریع باش و یکمی طلا به من بده، در غیر اینصورت شما را در این دنیا و دنیای دیگر راحت نمی‌کنم 🙂🙂! @{selected_user.username}",
    f"اگر در این اتاق خوشحال و خوشحال هستید، دلیل آن من هستم! سریع ثروت خود را با من به اشتراک بگذارید و یکمی طلا برای من بفرستید! @{selected_user.username}",
    f"سلام عشقم، آیا می‌توانید 1، 5، 10 طلا از دل خود برای من بفرستید؟ حتی اگر 1 طلا باشد هم کافی است 💅 💫؟ @{selected_user.username}",
    f"سلام، آیا فکر می‌کنی من زیبایی دارم؟ اگر بله باشد، با ارسال 5 طلا بازخورد بدهید، اگر نه با ارسال 10 طلا به بازخورد نقدی می‌پردازید 🙂. @{selected_user.username}",
    f"آیا این ثروت شما شوخی است؟ چه می‌گویند؟ هر چیزی را به اشتراک بگذارید، 5 طلایی دارید؟ عالی نیست؟ 🤗؟ @{selected_user.username}",
    f"خوشحالی برای گریه کردن است، من تبدیل به یک هنرمند تخصصی در انجام این هنر شده‌ام... اما آیا کسی ارزش من را می‌داند؟ خیر... @{selected_user.username}",
    f"یااااا از اینکه به من طلا می‌دهیم قبل ازاوانی از تو ممنونم! من تو را دوست دارم ❤️🤗. @{selected_user.username}",
    f"بسیار خوشبو هستی، آیا یکمی نذری به من بدهی؟ 💋 😘. @{selected_user.username}",
    f"دست‌ها بالا! این یک سرقت 🔫 است، همه چیز را از لباس زیر تا بالا به من می‌دهی حالا! طلاها را به سرعت بفرست 💰!! @{selected_user.username}",
    f"احترام به کار، حمایت از اتاق، طلا به من! @{selected_user.username}"
          ]
                        selected_response = random.choice(response_options)

                        await self.highrise.chat(selected_response)
                        await asyncio.sleep(30)


                    if not self.dilenme_active:
                        break
                else:
                    self.dilenme_active = False
        elif message.lower().startswith("!nobeg") and user.username in ["karainek", "maykilanderson"]:
            self.dilenme_active = False
            await self.highrise.chat("Dilenmekten yoruldum")
            end_position = Position(10.5, 0.0, 0.5)
            await self.highrise.walk_to(end_position)
        else:
            await asyncio.sleep(1)

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