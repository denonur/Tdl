from highrise import *
from highrise.models import *
from typing import Any, Literal, List
from datetime import datetime
from highrise import (
    BaseBot,
    ChatEvent,
    __main__,
    UserJoinedEvent,
    UserLeftEvent,
)
from highrise.models import (
    AnchorPosition,
    ChannelEvent,
    ChannelRequest,
    ChatEvent,
    ChatRequest,
    CurrencyItem,
    EmoteEvent,
    EmoteRequest,
    Error,
    FloorHitRequest,
    GetRoomUsersRequest,
    GetWalletRequest,
    IndicatorRequest,
    Item,
    Position,
    Reaction,
    ReactionEvent,
    ReactionRequest,
    SessionMetadata,
    TeleportRequest,
    TipReactionEvent,
    User,
    UserJoinedEvent,
    UserLeftEvent,
    MoveUserToRoomRequest,
    ModerateRoomRequest
)
from quattro import TaskGroup
from asyncio import run as arun
from asyncio import Queue
from typing import Any
import requests
import random
import asyncio
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
     
emote_mapping = {
    "angry": "emoji-angry",
    "1": "emoji-angry",
    "bow": "emote-bow",
    "2": "emote-bow",
    "casual": "idle-dance-casual",
    "3": "idle-dance-casual",
    "celebrate": "emoji-celebrate",
    "4": "emoji-celebrate",
    "charging": "emote-charging",
    "5": "emote-charging",
    "confused": "emote-confused",
    "6": "emote-confused",
    "cursing": "emoji-cursing",
    "7": "emoji-cursing",
    "curtsy": "emote-curtsy",
    "8": "emote-curtsy",
    "cutey": "emote-cutey",
    "9": "emote-cutey",
    "dotheworm": "emote-snake",
    "10": "emote-snake",
    "emotecute": "emote-cute",
    "11": "emote-cute",
    "energyball": "emote-energyball",
    "12": "emote-energyball",
    "enthused": "idle-enthusiastic",
    "13": "idle-enthusiastic",
    "fashion": "emote-fashionista",
    "14": "emote-fashionista",
    "flex": "emoji-flex",
    "15": "emoji-flex",
    "float": "emote-float",
    "16": "emote-float",
    "frog": "emote-frog",
    "17": "emote-frog",
    "gagging": "emoji-gagging",
    "18": "emoji-gagging",
    "gravity": "emote-gravity",
    "19": "emote-gravity",
    "greedy": "emote-greedy",
    "20": "emote-greedy",
    "hello": "emote-hello",
    "21": "emote-hello",
    "hot": "emote-hot",
    "22": "emote-hot",
    "icecream": "dance-icecream",
    "23": "dance-icecream",
    "kiss": "emote-kiss",
    "24": "emote-kiss",
    "kpop": "dance-blackpink",
    "25": "dance-blackpink",
    "laugh": "emote-laughing",
    "26": "emote-laughing",
    "lust": "emote-lust",
    "27": "emote-lust",
    "macarena": "dance-macarena",
    "28": "dance-macarena",
    "maniac": "emote-maniac",
    "29": "emote-maniac",
    "model": "emote-model",
    "30": "emote-model",
    "no": "emote-no",
    "31": "emote-no",
    "pose1": "emote-pose1",
    "32": "emote-pose1",
    "pose3": "emote-pose3",
    "33": "emote-pose3",
    "pose5": "emote-pose5",
    "34": "emote-pose5",
    "pose7": "emote-pose7",
    "35": "emote-pose7",
    "pose8": "emote-pose8",
    "36": "emote-pose8",
    "punk": "emote-punkguitar",
    "37": "emote-punkguitar",
    "russian": "dance-russian",
    "38": "dance-russian",
    "sad": "emote-sad",
    "39": "emote-sad",
    "sayso": "idle-dance-tiktok4",
    "40": "idle-dance-tiktok4",
    "shopping": "dance-shoppingcart",
    "41": "dance-shoppingcart",
    "shy": "emote-shy",
    "42": "emote-shy",
    "sit": "idle-loop-sitfloor",
    "43": "idle-loop-sitfloor",
    "snowangel": "emote-snowangel",
    "44": "emote-snowangel",
    "snowball": "emote-snowball",
    "45": "emote-snowball",
    "superpose": "emote-superpose",
    "46": "emote-superpose",
    "telekinesis": "emote-telekinesis",
    "47": "emote-telekinesis",
    "teleport": "emote-teleporting",
    "48": "emote-teleporting",
    "thumbs": "emoji-thumbsup",
    "49": "emoji-thumbsup",
    "tired": "emote-tired",
    "50": "emote-tired",
    "uwu": "idle-uwu",
    "51": "idle-uwu",
    "wave": "emote-wave",
    "52": "emote-wave",
    "weird": "dance-weird",
    "53": "dance-weird",
    "wrong": "dance-wrong",
    "54": "dance-wrong",
    "yes": "emote-yes",
    "55": "emote-yes",
    "zero": "emote-astronaut",
    "56": "emote-astronaut",
    "penny": "dance-pennywise",
    "57": "dance-pennywise",
    "zombie": "emote-zombierun",
    "58": "emote-zombierun",
    "fight": "emote-swordfight",
    "59": "emote-swordfight",
    "sing": "idle_singing",
    "60": "idle_singing",
    "savage": "dance-tiktok8",
    "61": "dance-tiktok8",
    "donot": "dance-tiktok2",
    "62": "dance-tiktok2",
    "shuffle": "dance-tiktok10",
    "63": "dance-tiktok10",
    "viral": "dance-tiktok9",
    "64": "dance-tiktok9",
    "penguin": "dance-pinguin",
    "65": "dance-pinguin",
    "rock": "idle-guitar",
    "66": "idle-guitar",
    "star": "emote-stargazer",
    "67": "emote-stargazer",
    "boxer": "emote-boxer",
    "68": "emote-boxer",
    "creepy": "dance-creepypuppet",
    "69": "dance-creepypuppet",
    "anime": "dance-anime",
    "70": "dance-anime",
    "ruh": "emote-creepycute",
    "71": "emote-creepycute",
    "kafasiz": "emote-headblowup",
    "72": "emote-headblowup",
    "bashful": "emote-shy2",
    "73": "emote-shy2",
    "party": "emote-celebrate",
    "74": "emote-celebrate",
    "pose10": "emote-pose10",
    "75": "emote-pose10",
    "skate": "emote-iceskating",
    "76": "emote-iceskating",
    "wild": "idle-wild",
    "77": "idle-wild",
    "nervous": "idle-nervous",
    "78": "idle-nervous",
    "timejump": "emote-timejump",
    "79": "emote-timejump",
    "toilet": "idle-toilet",
    "80": "idle-toilet",
    "jingle": "dance-jinglebell",
    "81": "dance-jinglebell",
    "hyped": "emote-hyped",
    "82": "emote-hyped",
    "sleigh": "emote-sleigh",
    "83": "emote-sleigh",
    "pose6": "emote-pose6",
    "84": "emote-pose6",
    "jump": "emote-jumpb",
    "85": "emote-jumpb",
    "kawai": "dance-kawai",
    "86": "dance-kawai",
    "touch": "dance-touch",
    "87": "dance-touch",
    "repose": "sit-relaxed",
    "88": "sit-relaxed",
    "step": "emote-celebrationstep",
    "89": "emote-celebrationstep",
    "ent": "idle-enthusiastic",    
    "kafasız": "emote-headblowup",
    "cik": "emote-shy2",
    "onur": "idle-wild"
}

class Bot(BaseBot):
    def __init__(self):
        super().__init__()
        self.target_room_id = "64e80327e64dcdf6d947c4aa"
        self.is_teleporting_dict = {}
        self.emote_looping = False
        self.user_emote_loops = {}
        self.following_user = None
        self.following_user_id = None
        self.kus = {}
        self.user_positions = {}  
        
    haricler = ["Atekinz"]
    dancs = ["emote-bow", "idle-dance-casual", "emoji-celebrate", "emote-charging", "emote-confused", "emoji-cursing", "emote-curtsy", "emote-cutey", "emote-snake", "emote-cute", "emote-energyball", "idle-enthusiastic", "emote-fashionista", "emoji-flex", "emote-float", "emote-frog", "emoji-gagging", "emote-gravity", "emote-greedy", "emote-hot", "dance-icecream", "dance-blackpink", "emote-laughing", "emote-lust", "emote-maniac", "emote-model", "dance-pennywise", "emote-pose1", "emote-pose3", "emote-pose5", "emote-pose7", "emote-pose8", "emote-punkguitar", "dance-russian", "idle-dance-tiktok4", "dance-shoppingcart", "emote-snowangel", "emote-snowball", "emote-superpose", "emote-swordfight", "emote-telekinesis", "emote-teleporting", "idle-uwu", "dance-weird", "dance-wrong", "emote-zombierun", "emote-astronaut", "dance-pennywise", "emote-zombierun", "emote-swordfight", "idle_singing", "dance-tiktok8", "dance-tiktok2", "dance-tiktok10", "dance-tiktok9", "dance-pinguin", "idle-guitar", "emote-stargazer", "emote-boxer", "dance-creepypuppet", "dance-anime", "emote-creepycute", "emote-headblowup", "emote-shy2", "emote-celebrate", "emote-pose10", "emote-iceskating", "idle-wild", "idle-nervous", "emote-timejump", "idle-toilet", "dance-jinglebell", "emote-hyped", "emote-sleigh", "emote-pose6", "emote-jumpb", "dance-kawai", "dance-touch", "emote-celebrationstep"]


    async def on_start(self, session_metadata: SessionMetadata) -> None:
        print("hi im alive?")
        self.highrise.tg.create_task(self.highrise.teleport(
            session_metadata.user_id, Position(17.00, 0.00,13.5, "FrontRight")))

  
    async def on_user_join(self, user: User, position: Position | AnchorPosition) -> None:

        if user.username == "Atekinz":
            response = f"My daddy joined room! @Atekinz 😙"
        elif user.username == "HimHoodie":
            response = f"Room owner joined room! @HimHoodie 😎"

        else:
            response = random.choice([f"Hi sir, welcome to HR School, @{user.username}!",
    f"Welcome School! I'm glad you joined us on this journey. Here every word can be the beginning of a new friendship, @{user.username}!",
    f"HELLO! Seeing you here is like the first sentence of a fairy tale. Hope you have a good time, welcome to our story, @{user.username}!",
    f"Hello dear traveler! The moments you spend here will turn into the best moments of your life. Hope you have a pleasant time, @{user.username}!",
    f"A warm welcome! I hope this room will be like a poem that touches the deepest points of our emotions. Welcome, @{user.username}!",
    f"Hello guys! Being in this room is like turning the pages of a literary work. Let's write unforgettable pages together, @{user.username}!",
    f"Welcome dear guests! In this room, let the words turn into a story woven with sincerity and friendship. Enjoy, @{user.username}!",
    f"HELLO! Being here is like turning the pages of a book. Every moment is a new discovery and a new beginning, @{user.username}!",
    f"We are very pleased to welcome you here! I hope this room is like a poem full of beauty. Welcome, @{user.username}!"])

        await self.highrise.chat(response)
        await self.highrise.send_whisper(user.id, "You can use emotes by typing numbers from 1 to 89.!")
        await self.highrise.send_emote("dance-floss")



    async def on_user_leave(self, user: User):
        if user.username == "Atekinz":
            farewell_message = "My daddy left 🥺😭 @Atekinz"
        else:
            if await self.is_user_allowed(user):
                farewell_message = f"Left @{user.username}!"
            else:
                farewell_message = f"@{user.username} Left!"

        user_id = user.id
        if user_id in self.user_emote_loops:
            await self.stop_emote_loop(user_id)

        if user_id in self.kus:
            self.kus[user_id] = False
      
        if self.following_user and self.following_user.id == user_id:
            await self.highrise.chat("I stopped following.")
            self.following_user = None
        await self.highrise.chat(farewell_message)

  
    async def on_chat(self, user: User, message: str) -> None:
        """On a received room-wide chat."""
      
        if message.lower().startswith("info") or message.lower().startswith("ınfo") :
            target_username = message.split("@")[-1].strip()  # Hedef kullanıcı adını al
            await self.userinfo(user, target_username)


        if message.startswith("+x") or message.startswith("-x"):
            try:
                adjustment = int(message[2:])
                axis = 'x' 

                if message.startswith("-x"):
                    adjustment *= -1 

                await self.adjust_position(user, adjustment, axis)

            except ValueError:
                print("Invalid adjustment value. Please use +x or -x followed by an integer.")

        elif message.startswith("+y") or message.startswith("-y"):
            try:
                adjustment = int(message[2:]) 
                axis = 'y'

                if message.startswith("-y"):
                    adjustment *= -1

                await self.adjust_position(user, adjustment, axis)

            except ValueError:
                print("Invalid adjustment value. Please use +y or -y followed by an integer.")

        elif message.startswith("+z") or message.startswith("-z"):
            try:
                adjustment = int(message[2:]) 
                axis = 'z'

                if message.startswith("-z"):
                    adjustment *= -1

                await self.adjust_position(user, adjustment, axis)

            except ValueError:
                print("Invalid adjustment value. Please use +z or -z followed by an integer.")
              
      
        allowed_commands = ["switch", "degis", "değiş"] 
        if any(message.lower().startswith(command) for command in allowed_commands) and await self.is_user_allowed(user):
            target_username = message.split("@")[-1].strip()

        
            if target_username not in self.haricler:
                await self.switch_users(user, target_username)
            else:
                print(f"{target_username} is in the exclusion list and won't be affected by the switch.")
      
        message_lower = message.lower()

        reactions_mapping = {
            "herkese el": "wave",
            "herkese parmak": "thumbs",
            "herkese kalp": "heart",
            "herkese alkis": "clap",
            "herkese alkış": "clap",
            "herkese goz": "wink",
            "herkese göz": "wink"
        }

        for reaction_name, reaction in reactions_mapping.items():
            if reaction_name in message_lower and await self.is_user_allowed(user):
                room_users = (await self.highrise.get_room_users()).content
                try:
                    for room_user, _ in room_users:
                        if str(room_user.id) != "656aa0bded43f73a721d284c":  # Exclude the bot itself
                            await self.highrise.react(reaction, room_user.id)
                except Exception as e:
                    print(f"An error occurred while sending all reactions: {e}")

      
        reactions_mapping = {
            "👋": "wave",
            "👍": "thumbs",
            "❤️": "heart",
            "👏": "clap",
            "😉": "wink",
        }

        unique_emojis = set(reactions_mapping.keys())

        for emoji in unique_emojis:
            count = message.count(emoji)
            if count > 0:
                await self.highrise.react(reactions_mapping[emoji], user.id)     
      
# TELPORTLAR TELEPORTLAR TELEPORT
      
      
        message = message.lower()

        teleport_locations = {
            "bosubos": Position(12.5, 0.5, 11.5),
            "bosubos": Position(0.5, 0.0, 0.5),
            "bosubos": Position(0.5, 0.0, 0.5),
            "bosubos": Position(random.randint(0, 40), random.randint(0, 40), random.randint(0, 40)),
            "bosubos": Position(random.randint(0, 40), random.randint(0, 40), random.randint(0, 40))
        }

        for location_name, position in teleport_locations.items():
            if message ==(location_name):
                try:
                    await self.teleport(user, position)
                except:
                    print("Teleportasyon sırasında hata oluştu")



        message = message.lower()

        teleport_locations = {
            "!bosuvos": Position(12.5, 0.5, 11.5),
            "!bosubod": Position(0.5, 0.0, 0.5),
            "!bosubos": Position(0.5, 0.0, 0.5),
            "!bosubos": Position(random.randint(0, 40), random.randint(0, 40), random.randint(0, 40)),
            "!bosubos": Position(random.randint(0, 40), random.randint(0, 40), random.randint(0, 40))
        }

        for location_name, position in teleport_locations.items():
            if message.startswith(location_name):
                target_username = message.split("@")[-1].strip().lower()

                try:
                    room_users = (await self.highrise.get_room_users()).content
                    target_user = next((u for u, _ in room_users if u.username.lower() == target_username), None)

                    if target_user and target_user.username.lower() not in self.haricler:
                        try:
                            await self.teleport(target_user, position)
                        except Exception as e:
                            print(f"An error occurred during teleportation: {e}")
                except Exception as e:
                    print(f"An error occurred while getting room users: {e}")
      
        if                          message.lower().startswith("gotur") or message.lower().startswith("götür"):
          target_username =         message.split("@")[-1].strip()
          await                     self.teleport_to_user(user, target_username)
        if await self.is_user_allowed(user) and message.lower().startswith("getir"):
            target_username = message.split("@")[-1].strip()
            if target_username not in self.haricler:
                await self.teleport_user_next_to(target_username, user)
        if message.lower().startswith("git") and await self.is_user_allowed(user):
            parts = message.split()
            if len(parts) == 2 and parts[1].startswith("@"):
                target_username = parts[1][1:]
                target_user = None

                room_users = (await self.highrise.get_room_users()).content
                for room_user, _ in room_users:
                    if room_user.username.lower() == target_username and room_user.username.lower() not in self.haricler:
                        target_user = room_user
                        break

                if target_user:
                    try:
                        kl = Position(random.randint(0, 40), random.randint(0, 40), random.randint(0, 40))
                        await self.teleport(target_user, kl)
                    except Exception as e:
                        print(f"An error occurred while teleporting: {e}")
                else:
                    print(f"Kullanıcı adı '{target_username}' odada bulunamadı.")

        if message.lower() == "full fldl" or message.lower() == "full flldv":
            if user.id not in self.kus:
                self.kus[user.id] = False

            if not self.kus[user.id]:
                self.kus[user.id] = True

                try:
                    while self.kus.get(user.id, False):
                        kl = Position(random.randint(0, 40), random.randint(0, 40), random.randint(0, 40))
                        await self.teleport(user, kl)

                        await asyncio.sleep(0.7)
                except Exception as e:
                    print(f"Teleport sırasında bir hata oluştu: {e}")

        if message.lower() == "dur" or message.lower() == "stop":
            if user.id in self.kus: 
                self.kus[user.id] = False

# MODERATOR KICK BAN VESAIRE 

        if message.lower().startswith("yallah") and await self.is_user_allowed(user):
            target_username = message.split("@")[-1].strip().lower()

            try:
                room_users = (await self.highrise.get_room_users()).content
                target_user = next((u for u, _ in room_users if u.username.lower() == target_username), None)

                if target_user and target_user.username.lower() != "Atekinz":
                    await self.move_user_to_target_room(target_user.id)
            except Exception as e:
                print(f"An error occurred while moving the user: {e}")
      
        if message == "-gay":
            await self.move_user_to_target_room(user.id)
        if message.lower() == "everyone gay" and await self.is_user_allowed(user):
            await self.move_users_to_target_room()
    

        if message.lower().startswith("ceza") and await self.is_user_allowed(user):
            target_username = message.split("@")[-1].strip().lower()

            if target_username not in self.haricler:
                room_users = (await self.highrise.get_room_users()).content
                target_user = next((u for u, _ in room_users if u.username.lower() == target_username), None)

                if target_user:
                    if target_user.id not in self.is_teleporting_dict:
                        self.is_teleporting_dict[target_user.id] = True

                        try:
                            while self.is_teleporting_dict.get(target_user.id, False):
                                kl = Position(random.randint(0, 30), random.randint(0, 0), random.randint(0, 30))
                                await self.teleport(target_user, kl)
                                await asyncio.sleep(1)
                        except Exception as e:
                            print(f"An error occurred while teleporting: {e}")

                        self.is_teleporting_dict.pop(target_user.id, None)
                        final_position = Position(17.0, 0.0, 13.5, "FrontRight")
                        await self.teleport(target_user, final_position)
                    else:
                        await self.highrise.chat(f"@{target_username} zaten cezalandırılıyor.")
                else:
                    await self.highrise.chat(f"@{target_username} odada değil?!")

        if message.lower().startswith("dur") and await self.is_user_allowed(user):
            target_username = message.split("@")[-1].strip().lower()

            room_users = (await self.highrise.get_room_users()).content
            target_user = next((u for u, _ in room_users if u.username.lower() == target_username), None)

            if target_user:
                self.is_teleporting_dict.pop(target_user.id, None)
                await self.highrise.chat(f"@{target_username} için cezalandırma işlemi durduruldu.")
            else:
                await self.highrise.chat(f"@{target_username} odada değil >.<")

        if message.lower() == "takip" and await self.is_user_allowed(user):
            if self.following_user is not None:
                await self.highrise.chat("Şu anda başka birini takip ediyorum, sıranızı bekleyin.")
            else:
                await self.follow(user)

        if message.lower() == "stay" and await self.is_user_allowed(user):
            if self.following_user is not None:
                await self.highrise.chat("Takip etmeyi bıraktım.")
                self.following_user = None
            else:
                await self.highrise.chat("Şu anda kimseyi takip etmiyorum.")
              
        if message.lower().startswith("kick") and await self.is_user_allowed(user):
            parts = message.split()
            if len(parts) != 2:
                await self.highrise.chat("Yanlış yazıyorsun 🙂.")
                return
            if "@" not in parts[1]:
                username = parts[1]
            else:
                username = parts[1][1:]

            room_users = (await self.highrise.get_room_users()).content
            for room_user, pos in room_users:
                if room_user.username.lower() == username.lower():
                    user_id = room_user.id
                    break

            if "user_id" not in locals():
                await self.highrise.chat("Bu kişi odada değil ki!?")
                return

            try:
                await self.highrise.moderate_room(user_id, "kick")
            except Exception as e:
                await self.highrise.chat(f"{e}")
                return

            await self.highrise.chat(f"@{username}, @{user.username} tarafından odadan kovuldu 🤭")

        message = message.strip().lower()
        user_id = user.id

        if message.startswith("full"):
            emote_name = message.replace("full", "").strip()

            if user_id in self.user_emote_loops and self.user_emote_loops[user_id] == emote_name:
                await self.stop_emote_loop(user_id)
            else:
                await self.start_emote_loop(user_id, emote_name)
        elif message == "stop" or message == "dur":
            if user_id in self.user_emote_loops:
                await self.stop_emote_loop(user_id)
              
        message = message.strip().lower()

        if "@" in message:
            parts = message.split("@")
            if len(parts) < 2:
                return

            emote_name = parts[0].strip()
            target_username = parts[1].strip()

            if emote_name in emote_mapping:
                response = await self.highrise.get_room_users()
                users = [content[0] for content in response.content]
                usernames = [user.username.lower() for user in users]

                if target_username not in usernames:
                    return

                user_id = next((u.id for u in users if u.username.lower() == target_username), None)
                if not user_id:
                    return

                await self.handle_emote_command(user.id, emote_name)
                await self.handle_emote_command(user_id, emote_name)

        for emote_name, emote_id in emote_mapping.items():
            if message.lower() == emote_name.lower():
                try:
                    await self.highrise.send_emote(emote_id, user.id)
                except:
                    print(f"Emote gönderilirken bir hata oluştu: {emote_name}")
      
        if message.lower().startswith("all ") and await self.is_user_allowed(user):
            emote_name = message.replace("all ", "").strip()
            if emote_name in emote_mapping:
                emote_to_send = emote_mapping[emote_name]
                room_users = (await self.highrise.get_room_users()).content
                for room_user, _ in room_users:
                    try:
                        await self.highrise.send_emote(emote_to_send, room_user.id)
                    except Exception as e:
                        error_message = f"Hata oluştu: {e}"
                        await self.highrise.send_whisper(user.id, error_message)
            else:
                await self.highrise.send_whisper(user.id, "Geçersiz emote adı: {}".format(emote_name))


        try:
            if message.lstrip().startswith(("cast")):
                response = await self.highrise.get_room_users()
                users = [content[0] for content in response.content]
                usernames = [user.username.lower() for user in users]
                parts = message[1:].split()
                args = parts[1:]

                if len(args) >= 1 and args[0][0] == "@" and args[0][1:].lower() in usernames:
                    user_id = next((u.id for u in users if u.username.lower() == args[0][1:].lower()), None)

                    if message.lower().startswith("cast"):
                        await self.highrise.send_emote("emote-telekinesis", user.id)
                        await self.highrise.send_emote("emote-gravity", user_id)
        except Exception as e:
            print(f"An error occurred: {e}")
          
        if message.startswith("dans") or message.startswith("dance"):
            try:
                emote_id = random.choice(self.dancs)
                await self.highrise.send_emote(emote_id, user.id)
            except:
                print("Dans emote gönderilirken bir hata oluştu.")

# DIGER KOMUTLAR WIE ASYNICO UND DING

    async def adjust_position(self, user: User, adjustment: int, axis: str) -> None:
        try:
            room_users = await self.highrise.get_room_users()

            user_position = None
            for user_obj, user_position in room_users.content:
                if user_obj.id == user.id:
                    break

            if user_position:
                if axis == 'x':
                    new_position = Position(user_position.x + adjustment, user_position.y, user_position.z, user_position.facing)
                elif axis == 'y':
                    new_position = Position(user_position.x, user_position.y + adjustment, user_position.z, user_position.facing)
                elif axis == 'z':
                    new_position = Position(user_position.x, user_position.y, user_position.z + adjustment, user_position.facing)
                else:
                    # Handle unsupported axis
                    print(f"Unsupported axis: {axis}")
                    return

                await self.teleport(user, new_position)

        except Exception as e:
            print(f"An error occurred during position adjustment: {e}")
  
    async def switch_users(self, user: User, target_username: str) -> None:
        try:
            room_users = await self.highrise.get_room_users()

            # Find maker's position
            maker_position = None
            for maker_user, maker_position in room_users.content:
                if maker_user.id == user.id:
                    break

            # Find target's position
            target_position = None
            for target_user, position in room_users.content:
                if target_user.username.lower() == target_username.lower():
                    target_position = position
                    break

            # Teleport maker to target's position with adjustment
            if maker_position and target_position:
                await self.teleport(user, Position(target_position.x + 0.0001, target_position.y, target_position.z, target_position.facing))

                # Teleport target to maker's position with adjustment
                await self.teleport(target_user, Position(maker_position.x + 0.0001, maker_position.y, maker_position.z, maker_position.facing))

        except Exception as e:
            print(f"An error occurred during user switch: {e}")
 
    async def on_reaction(self, user: User, reaction: str, receiver: User) -> None:
        # Check if the receiver is the bot by its id
        if str(receiver.id) == "656aa0bded43f73a721d284c":
            try:
                await self.highrise.react(reaction, user.id)
            except Exception as e:
                print(f"An error occurred while reacting: {e}")

    async def move_users_to_target_room(self):
        room_users = (await self.highrise.get_room_users()).content

        for room_user, _ in room_users:
                await self.highrise.move_user_to_room(room_user.id, self.target_room_id)
              
    async def move_user_to_target_room(self, user_id: str):
        await self.highrise.move_user_to_room(user_id, self.target_room_id)
  
    async def is_user_allowed(self, user: User) -> bool:
        user_privileges = await self.highrise.get_room_privilege(user.id)
        return user_privileges.moderator or user.username in ["Atekinz"]
  
    async def moderate_room(
        self,
        user_id: str,
        action: Literal["kick", "ban", "unban", "mute"],
        action_length: int | None = None,
    ) -> None:
        """Moderate a user in the room."""
  
    async def userinfo(self, user: User, target_username: str) -> None:
        user_info = await self.webapi.get_users(username=target_username, limit=1)

        if not user_info.users:
            await self.highrise.chat("Kullanıcı bulunamadı, lütfen geçerli bir kullanıcı belirtin")
            return

        user_id = user_info.users[0].user_id

        user_info = await self.webapi.get_user(user_id)

        number_of_followers = user_info.user.num_followers
        number_of_friends = user_info.user.num_friends
        country_code = user_info.user.country_code
        outfit = user_info.user.outfit
        bio = user_info.user.bio
        active_room = user_info.user.active_room
        crew = user_info.user.crew
        number_of_following = user_info.user.num_following
        joined_at = user_info.user.joined_at.strftime("%d/%m/%Y %H:%M:%S")

        joined_date = user_info.user.joined_at.date()
        today = datetime.now().date()
        days_played = (today - joined_date).days

        last_login = user_info.user.last_online_in.strftime("%d/%m/%Y %H:%M:%S") if user_info.user.last_online_in else "Son giriş bilgisi mevcut değil"

        await self.highrise.chat(f"""Kullanıcı adı: {target_username}\nTakipçi sayısı: {number_of_followers}\nArkadaş sayısı: {number_of_friends}\nOyuna ilk girdiği tarih: {joined_at}\nOyuna son girdiği tarih: {last_login}\nOyuna başladığından itibaren geçen gün sayısı: {days_played}""")

    async def follow(self, user: User, message: str = ""):
        self.following_user = user  
        while self.following_user == user:
            room_users = (await self.highrise.get_room_users()).content
            for room_user, position in room_users:
                if room_user.id == user.id:
                    user_position = position
                    break
            if user_position is not None and isinstance(user_position, Position):
                nearby_position = Position(user_position.x + 1.0, user_position.y, user_position.z)
                await self.highrise.walk_to(nearby_position)
            
            await asyncio.sleep(0.5)


    async def on_message(self, user_id: str, conversation_id: str, is_new_conversation: bool) -> None:
        response = await self.highrise.get_messages(conversation_id)
        if isinstance(response, GetMessagesRequest.GetMessagesResponse):
            message = response.messages[0].content
            print(message)

        if message.lower() == "liste":
            await self.highrise.send_message(conversation_id, "1. Angry\n2. Bow\n3. Casual\n4. Celebrate\n5. Charging\n6. Confused\n7. Cursing\n8. Curtsy\n9. Cutey\n10. Dotheworm\n11. Cute\n12. Energyball\n13. Enthused\n14. Fashion\n15. Flex\n16. Float\n17. Frog\n18. Gagging\n19. Gravity\n20. Greedy\n21. Hello\n22. Hot\n23. Icecream\n24. Kiss\n25. Kpop\n26. Laugh\n27. Lust\n28. Macarena\n29. Maniac\n30. Model\n31. No\n32. Pose1\n33. Pose3\n34. Pose5\n35. Pose7\n36. Pose8\n37. Punk\n38. Russian\n39. Sad\n40. Sayso\n41. Shopping\n42. Shy\n43. Sit\n44. Snowangel\n45. Snowball\n46. Superpose\n47. Telekinesis\n48. Teleport\n49. Thumbs\n50. Tired\n51. Uwu\n52. Wave\n53. Weird\n54. Wrong\n55. Yes\n56. Zero\n57. Penny\n58. Zombie\n59. Fight\n60. Sing\n61. Savage\n62. Donot\n63. Shuffle\n64. Viral\n65. Penguin\n66. Rock\n67. Star\n68. Boxer\n69. Creepy\n70. Anime\n71. Ruh\n72. Kafasız\n73. Bashful\n74. Party\n75. Pose10\n76. Skate\n77. Wild\n78. Nervous\n79. Timejump\n80. Toilet\n81. Jingle\n82. Hyped\n83. Sleigh\n84. Pose6\n85. Jump\n86. Kawai\n87. Touch\n88. Repose\n89. Step")

    async def on_tip(self, sender: User, receiver: User, tip: CurrencyItem | Item) -> None:
        message = f"{sender.username} tarafından {receiver.username} kişine {tip.amount} altın bağış yapıldı."
        await self.highrise.chat(message)

     
    async def handle_emote_command(self, user_id: str, emote_name: str) -> None:
        if emote_name in emote_mapping:
            emote_to_send = emote_mapping[emote_name]
            
            try:
                await self.highrise.send_emote(emote_to_send, user_id)
            except Exception as e:
                print(f"Error sending emote: {e}")

      
    async def teleport(self, user: User, position: Position):
        try:
            await self.highrise.teleport(user.id, position)
        except Exception as e:
            print(f"Caught Teleport Error: {e}")

    async def teleport_to_user(self, user: User, target_username: str) -> None:
        try:
            room_users = await self.highrise.get_room_users()
            for target, position in room_users.content:
                if target.username.lower() == target_username.lower():
                    z = position.z
                    new_z = z - 1
                    await self.teleport(user, Position(position.x, position.y, new_z, position.facing))
                    break
        except Exception as e:
            print(f"An error occurred while teleporting to {target_username}: {e}")

    async def teleport_user_next_to(self, target_username: str, requester_user: User) -> None:
        try:
            # Get the position of the requester_user
            room_users = await self.highrise.get_room_users()
            requester_position = None
            for user, position in room_users.content:
                if user.id == requester_user.id:
                    requester_position = position
                    break

            # Find the target user and their position
            for user, position in room_users.content:
                if user.username.lower() == target_username.lower():
                    z = requester_position.z
                    new_z = z + 1  # Example: Move +1 on the z-axis (upwards)
                    await self.teleport(user, Position(requester_position.x, requester_position.y, new_z, requester_position.facing))
                    break
        except Exception as e:
            print(f"An error occurred while teleporting {target_username} next to {requester_user.username}: {e}")
          
    async def on_whisper(self, user: User, message: str) -> None:
        """On a received room whisper."""
        if await self.is_user_allowed(user) and message.startswith(''):
            try:
                xxx = message[0:]
                await self.highrise.chat(xxx)
            except:
                print("error 3")
              
    async def start_emote_loop(self, user_id: str, emote_name: str) -> None:
        if emote_name in emote_mapping:
            self.user_emote_loops[user_id] = emote_name 
            emote_to_send = emote_mapping[emote_name]
            while self.user_emote_loops.get(user_id) == emote_name: 
                try:
                    await self.highrise.send_emote(emote_to_send, user_id)
                except Exception as e:
                    if "Target user not in room" in str(e):
                        print(f"{user_id} odada değil, emote gönderme durduruluyor.")
                        break 
                await asyncio.sleep(3.5) 

    async def stop_emote_loop(self, user_id: str) -> None:
        if user_id in self.user_emote_loops:
            self.user_emote_loops.pop(user_id)
  
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
  room_id = "64e80327e64dcdf6d947c4aa"
  bot_token = "b247c27820b5b0ee256df69def667fafe39c66bf2193cd6d23f344b996a89145"
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
        import traceback
        print("Caught an exception:")
        traceback.print_exc()
        time.sleep(1)
        continue


if __name__ == "__main__":
  WebServer().keep_alive()

  RunBot().run_loop()
