import os
import nextcord
from nextcord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TESTING_GUILD_ID = os.getenv("G_ID")
BOT_TOKEN = os.getenv("BOT_TOKEN")


intents = nextcord.Intents.all()
intents.members = True
intents.message_content = True


bot = commands.Bot(command_prefix='./', intents=intents)

@bot.event
async def on_ready():
    print(f"logged in as {bot.user}")

# cogs
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")

bot.run(BOT_TOKEN)