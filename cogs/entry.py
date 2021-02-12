import templatebot
import discord
from discord.ext import commands
from discord.utils import find
from discord import Webhook, AsyncWebhookAdapter
import requests
import aiohttp
from os import environ as env
from dotenv import load_dotenv

load_dotenv(".env")

class Entry(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  

  @commands.command(name="verify")
  async def verify_(self, ctx, link):
   async with aiohttp.ClientSession() as session:
     hook = Webhook.from_url(env.get("HOOK"), adapter= AsyncWebhookAdapter(session)) 
     entries = requests.get(f"https://raw.githubusercontent.com/elfq/botjam/main/entries/{link}")

     if f"{ctx.author.id}" in entries.text:
       entry_role = find(lambda r: r.name == 'Entry Ticket', ctx.guild.roles)
       await ctx.author.add_roles(entry_role)
       await ctx.send("✅ Check your roles!")
       await hook.send(f"✅ Successfully verified `{ctx.author}`\n`{link}`\n<https://github.com/elfq/botjam/blob/main/entries/{link}>")
       
     if f"{ctx.author.id}" not in entries.text:
       await ctx.send(":x: You're not listed as an author for this file.")
  


def setup(bot):
  bot.add_cog(Entry(bot))