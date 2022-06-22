import discord
from discord.ext import commands
from dislash import *

class Utils(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(description = 'Returns the bots ping.')
    async def ping(self, ctx):
        embed = discord.Embed(title = "Pong!", color = 0x00ff00)
        embed.add_field(name = "Ping", value = f"{round(self.client.latency * 1000)}ms")
        await ctx.send(embed = embed)
    
    @commands.command(description = 'Returns info about the user.')
    async def userinfo(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author

        embed = discord.Embed(title = "User info", color = 0x00ff00)
        embed.add_field(name = "User", value = f"{ctx.author.mention}")
        embed.add_field(name = "ID", value = f"{ctx.author.id}")
        embed.add_field(name = "Status", value = f"{ctx.author.status}")
        # Create at field with the timezone being the timezone of the user
        embed.add_field(name = "Created at", value = f"{ctx.author.created_at.strftime('%Y-%m-%d %H:%M:%S %Z')}")
        embed.add_field(name = "Joined at", value = f"{ctx.author.joined_at.strftime('%Y-%m-%d %H:%M:%S %Z')}")
        embed.add_field(name = 'Status', value = f'{ctx.author.status}')
        # Get all the roles the user has and display the name of the role
        roles = [role.name for role in ctx.author.roles]
        if "@everyone" in roles:
            roles.remove("@everyone")
        embed.add_field(name = 'Roles', value = f'{roles}')
        embed.set_thumbnail(url = member.avatar_url)
        await ctx.send(embed = embed)
    
    @commands.command(description = 'Shows the loaded cogs.')
    async def cogs(self, ctx):
        # Return the cog names of all cogs in the bot
        embed = discord.Embed(title = "Cogs currently loaded", color = 0x00ff00)
        # Get the names of all cogs in the bot
        for cog in self.client.cogs:
            embed.add_field(name = 'Cog loaded.', value = f'{cog}')
        await ctx.send(embed = embed)

    @commands.command(description = 'Returns the users avatar.')
    async def avatar(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author
        
        embed = discord.Embed(title = "Avatar", color = 0x00ff00)
        embed.set_image(url = member.avatar_url)
        await ctx.send(embed = embed)
    
    @commands.command(description = 'Returns info about the server.')
    async def serverinfo(self, ctx):
        embed = discord.Embed(title = "Server info", color = 0x00ff00)
        embed.add_field(name = "Server name", value = f"{ctx.guild.name}")
        embed.add_field(name = "Server ID", value = f"{ctx.guild.id}")
        embed.add_field(name = "Server owner", value = f"{ctx.guild.owner}")
        embed.add_field(name = "Server created at", value = f"{ctx.guild.created_at}")
        embed.add_field(name = "Server member count", value = f"{ctx.guild.member_count}")
        await ctx.send(embed = embed)

def setup(client):
    client.add_cog(Utils(client))