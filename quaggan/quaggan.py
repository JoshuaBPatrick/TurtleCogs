import os
import json
import discord
from discord.ext import commands
from __main__ import settings as bot_settings
from __main__ import send_cmd_help
from cogs.utils.dataIO import dataIO
import random
import urllib

SETTINGS = "data/quaggan/settings.json"

class Quaggan:
    """Cog to give the calling user a specified or otherwise random picture of a quaggan"""
    """All Quaggans sourced from the Guild Wars 2 Wiki and it's API's database of images"""
    
    def __init__(self, bot):
        self.bot = bot;
        self.settings = dataIO.load_json(SETTINGS)
    
    @commands.command(pass_context=True)
    async def quaggan(self, ctx, search):
        link = "https://api.guildwars2.com/v2/quaggans"
        f = urllib.urlopen(link)
        quagganList = f.read()
        await self.bot.say(quagganList)

def check_folders():
    folder = ("data/quaggan/")
    if not os.path.exists(folder):
        print("Creating quaggan folder...")
        os.makedirs(folder)
            
def check_files():
    if not os.path.isfile("data/quaggan/settings.json"):
        print("Creating empty settings.json...")
        dataIO.save_json("data/quaggan/settings.json", {})

def setup(bot):
    check_folders()
    check_files()
    bot.add_cog(Quaggan(bot))
    
