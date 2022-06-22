import json
from tkinter import N
import discord
from discord.ext import commands

client = commands.Bot(command_prefix = 't.')

@commands.has_permissions(kick_members = True)
@client.command()
async def warn(ctx, member: discord.Member, *, reason = "No reason specified."):    
    embed = discord.Embed(title = "Moderation system notification", color = 0x00ff00)
    embed.add_field(name = "Action", value = "Warned")
    embed.add_field(name = "User", value = f"{member.mention}")
    embed.add_field(name = "Reason", value = reason)
    embed.add_field(name = "Moderator", value = f"{ctx.author.mention}")
    await ctx.send(embed = embed)

    with open('warnings.json', 'w') as f:
        data = {
            'user': member.id,
            'reason': reason,
            'moderator': ctx.author.id
        }
        json.dump(data, f, indent = 4)

client.run('OTg2NzMwMzk3OTY4Nzg1NTE4.GbAMrq.vlb3wjzuzbTJWLztfO6x8LaBfiKn5wHbQ3DEF8')