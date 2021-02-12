from templatebot import Bot
import discord
from discord import AllowedMentions, Activity, Game
from os import environ as env
from dotenv import load_dotenv

load_dotenv(".env")

bot = Bot(
    name="Bot Jam",
    command_prefix="!",
    allowed_mentions=AllowedMentions(
        everyone=False, roles=False, users=False, replied_user=True
    ),
    activity=Game("With new entries"),
)

bot.VERSION = "1.0.0"
bot.load_initial_cogs(
    "cogs.entry")

bot.run(env.get("TOKEN", None))
