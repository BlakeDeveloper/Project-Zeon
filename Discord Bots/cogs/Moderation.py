from time import strftime
import discord
import json
from discord.ext import commands

class Moderation(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    @commands.has_permissions(administrator = True)
    @commands.command(description = 'Bans a user from the server.')
    async def ban(self, ctx, member: discord.Member, *, reason = "No reason specified."):
        if ctx.guild.id == 981611193984749578:
            if member.id == 938876130897829938:
                embed = discord.Embed(title = "Error! Whitelisted user.", color = 0x00ff00)
                embed.add_field(name = "Error", value = "You cannot ban BlakePrograms#0001 as they are a whitelisted user.")
                return await ctx.send(embed = embed)
        
        embed = discord.Embed(title = "Moderation system notification", color = 0x00ff00)
        embed.add_field(name = "Action", value = "Banned")
        embed.add_field(name = "User", value = f"{member.mention}")
        embed.add_field(name = "Reason", value = reason)
        embed.add_field(name = "Moderator", value = f"{ctx.author.mention}")
        await ctx.send(embed = embed)

        embed = discord.Embed(title = "Moderation system notification", description = f"You was banned in {ctx.author.guild} for: {reason}",color = 0x00ff00)
        member.send(embed = embed)

        member.ban(reason = reason)

    @commands.has_permissions(kick_members = True)
    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason = "No reason specified."):
        if ctx.guild.id == 981611193984749578:
            if member.id == 938876130897829938:
                embed = discord.Embed(title = "Error! Whitelisted user.", color = 0x00ff00)
                embed.add_field(name = "Error", value = "You cannot kick BlakePrograms#0001 as they are a whitelisted user.")
                return await ctx.send(embed = embed)
        
        embed = discord.Embed(title = "Moderation system notification", color = 0x00ff00)
        embed.add_field(name = "Action", value = "Kicked")
        embed.add_field(name = "User", value = f"{member.mention}")
        embed.add_field(name = "Reason", value = reason)
        embed.add_field(name = "Moderator", value = f"{ctx.author.mention}")
        await ctx.send(embed = embed)

        embed = discord.Embed(title = "Moderation system notification", description = f"You was kicked in {ctx.author.guild} for: {reason}",color = 0x00ff00)
        member.send(embed = embed)

        member.kick(reason = reason)
    
    @commands.has_permissions(kick_members = True)
    @commands.command()
    async def purge(self, ctx, amount: int):
        await ctx.channel.purge(limit = amount)
        embed = discord.Embed(title = "Moderation system notification", description = f"{ctx.author.mention} has purged {amount} messages.",color = 0x00ff00)
        await ctx.send(embed = embed)

    # When a message is deleted store it in the del_messages.txt file
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.author.bot:
            return
        
        with open("del_messages.txt", "a") as f:
            # Get when the message was deleted
            time = strftime("%H:%M:%S")
            f.writelines(f"{message.author} - {message.content} - {time}\n")
            f.close()
    
    @commands.is_owner()
    @commands.command()
    async def del_messages(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author

        with open("./del_messages.txt", "r") as f:
            for line in f:
                embed = discord.Embed(Title = f"{member}' deleted messages", color = 0x00ff00)
                if str(member) in line:
                    # find time in the line
                    time = line.split(" - ")[2]
                    line = line.split(" - ")[1]
                    embed.add_field(name = f'Message deleted at {time}', value = line, inline = False)
            await ctx.send(embed = embed)

def setup(client):
    client.add_cog(Moderation(client))