import os
import logging
import asyncio
from gtts import gTTS
from twitchio.ext import commands
import pygame
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

OAUTH_TOKEN = os.getenv("OAUTH_TOKEN")
BOTNICK = os.getenv("BOTNICK")
CHANNEL = os.getenv("CHANNEL")
INTERVAL = 3

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(token=OAUTH_TOKEN, prefix="!", initial_channels=[CHANNEL])
        self.chat_message = None

    async def event_message(self, message):
        if len(message.content) <= 187  and len(message.content) > 0 and message.author.name.lower() not in ["Fossabot", "streamelements", "nightbot", "moobot"] and not "https://" in message.content: # and message.content.startswith("#"):
            self.chat_message = message.content
            self.author = message.author.name

async def read_chat():
    bot = Bot()
    asyncio.create_task(bot.start())
    lastmessage = None
    
    pygame.mixer.init()

    while True:
        await asyncio.sleep(INTERVAL)
        try:
            if bot.chat_message != lastmessage:
                filename = "voice.mp3"

                if os.path.exists(filename):
                    try:
                        os.remove(filename)
                    except PermissionError:
                        logging.warning(f"Cannot remove {filename} - file may still be in use")
                        continue

                voice = gTTS(text=bot.chat_message, lang="de")
                voice.save(filename)
                
                pygame.mixer.music.load(filename)
                pygame.mixer.music.play()

                while pygame.mixer.music.get_busy():
                    await asyncio.sleep(0.1)

                pygame.mixer.music.stop()

                pygame.mixer.quit()
                time.sleep(0.1)

                try:
                    os.remove(filename)
                    logging.info(f"{bot.author}: {filtered}")
                except Exception as e:
                    logging.error(f"Fehler beim Löschen der Datei {filename}: {e}")

                pygame.mixer.init()

                lastmessage = bot.chat_message

        except Exception as e:
            logging.error(f"Fehler: {e}")

if __name__ == "__main__":
    try:
        asyncio.run(read_chat())
    except KeyboardInterrupt:
        logging.info("Beendet")
    except Exception as e:
        logging.error(f"Fehler: {e}")