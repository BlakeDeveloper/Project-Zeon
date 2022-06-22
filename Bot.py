import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix='ss.')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.command()
async def screenshot(ctx, *, website: str):
    import requests

    url = "https://v1.nocodeapi.com/belclap/screen/LefKfssFYTrSMTLV/screenshot?url={}".format(website)
    params = {"url": "<url>", "width": "1920", "height": "1080", "format": "png"}
    r = requests.get(url = url, params = params)
    await ctx.send(r.url)

client.run('OTYyNjcyOTU3ODY2NTE2NTEw.Gbu8u_.R2uRp-YMdI3msqIFolNuGgldSLKa0ecrLOt7hc')
