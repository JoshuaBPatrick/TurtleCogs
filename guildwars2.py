from cogs.utils.dataIO import dataIO
from __main__ import send_cmd_help
from __main__ import settings as bot_settings
import discord
from discord.ext import commands
import json
import os
import aiohttp

try:
    from bs4 import BeautifulSoup
    soupAvailable = True
except ImportError:
    soupAvailable = False

SETTINGS = "data/guildwars2/settings.json"

class GuildWars2:
    """Guild Wars 2 Data Search"""

    def __init__(self, bot):
        self.bot = bot
        self.settings = dataIO.load_json(SETTINGS)
        
    @commands.group(pass_context=True, aliases=["gw2"])
    async def guildwars2(self, ctx):
            if ctx.invoked_subcommand is None:
                await send_cmd_help(ctx)

    @guildwars2.command(pass_context=True)
    async def npc(self, ctx, *search):
        url = "https://wiki.guildwars2.com/wiki/{}".format(search)
        async with aiohttp.get(url) as response:
            soup = BeautifulSoup(await response.text(), "html.parser")
            sumInfo = soup.find_all("div", class_="infobox npc")
            
            npcTitle = sumInfo.find
            
            embed = discord.Embed(colour=0x009900, description=npcQuote)
            embed.add-field(name="Name", value=
        
def check_folders():
    if not os.path.exists("data/guildwars2"):
        print("Creating data/guildwars2 folder...")
        os.makedirs("data/guildwars2")

def check_files():
    f = "data/guildwars2/settings.json"
    if not dataIO.is_valid_json(f):
        print("Creating data/guildwars2/settings.json...")
        dataIO.save_json(f, {})

def setup(bot):
    if not soupAvailable:
        raise RuntimeError("You need to run \'pip3 install beautifulsoup4\' in command prompt.")
    else:
        check_folders()
        check_files()
        n = GuildWars2(bot)
        bot.add_cog(n)