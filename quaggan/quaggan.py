import os
import json
import discord
from discord.ext import commands
from __main__ import settings as bot_settings
from __main__ import send_cmd_help
from cogs.utils.dataIO import dataIO
import random
import requests
import io
import aiohttp

SETTINGS = "data/quaggan/settings.json"

class Quaggan:
    """Cog to give the calling user a specified or otherwise random picture of a quaggan"""
    """All Quaggans sourced from the Guild Wars 2 Wiki and it's API's database of images"""

    def __init__(self, bot):
        self.bot = bot;
        self.settings = dataIO.load_json(SETTINGS)

    @commands.command(pass_context=True)
    async def quaggan(self, ctx, *quag):
        """Give a random quaggan"""
        link = "https://api.guildwars2.com/v2/quaggans"
        quagganList = eval(requests.get(link).text)
        if quag == ():
            qRand = quagganList[random.randint(0, len(quagganList))]
            selectQuaggan = "https://api.guildwars2.com/v2/quaggans/{}".format(qRand)
            link = selectQuaggan
            qImage = eval(requests.get(link).text)["url"]
            async with aiohttp.get(qImage) as image:
                await self.bot.upload(io.BytesIO(await image.read()), filename=qImage)
        else:
            quag = "".join(quag)
            selectQuaggan = "https://api.guildwars2.com/v2/quaggans/{}".format(quag)
            nLink = selectQuaggan
            qImage = eval(requests.get(nLink).text)["url"]
            async with aiohttp.get(qImage) as image:
                await self.bot.upload(io.BytesIO(await image.read()), filename=qImage)

    @commands.command(pass_context=True)
    async def quaggans(self, ctx):
        """Show all quaggans"""
        link = "https://api.guildwars2.com/v2/quaggans"
        quagganList = eval(requests.get(link).text)
        qString = ""
        for q in quagganList:
            qString += ("*" + q.lower() + "*, ")
        embed = discord.Embed(colour=0x3399FF, description="")
        embed.add_field(name="Quaggans", value=qString)
        await self.bot.send_message(ctx.message.author, embed=embed)

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
