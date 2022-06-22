import discord
from discord.ext import commands
import datetime

client = commands.Bot(command_prefix = '!')
client.remove_command('help')

@client.event
async def on_ready():
    print('Bot is ready.')
    await client.change_presence(activity=discord.Game(name='Watching: !help'))

    with open('logs.txt', 'a') as f:
        # Write to logs.txt the date and time of the bot's startup.
        f.write(f'{client.user.name} has logged in at {datetime.datetime.now()}')
        f.close()

@client.command()
async def spotifyinfo(ctx, *, song):
    # Get the song's information from the Spotify API.
    song_info = await client.get_spotify_info(song)
    # If the song is not found, return an error message.
    if song_info is None:
        await ctx.send('Song not found.')
    # If the song is found, return the song's information.
    else:
        await ctx.send(f'Artist: {song_info["artist"]}\nSong: {song_info["song"]}\nAlbum: {song_info["album"]}\nURL: {song_info["url"]}')
    # If the song is not found, return an error message.
    if song_info is None:
        await ctx.send('Song not found.')
    # If the song is found, return the song's information.
    else:
        await ctx.send(f'Artist: {song_info["artist"]}\nSong: {song_info["song"]}\nAlbum: {song_info["album"]}\nURL: {song_info["url"]}')

client.run('OTYyNjcyOTU3ODY2NTE2NTEw.GhJBMV.rIcEPAxo1t8NQjCBI-n8XUUfYJHs6yYpXiuPCM')