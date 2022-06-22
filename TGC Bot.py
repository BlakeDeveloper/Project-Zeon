import discord
from discord.ext import commands
from dislash import InteractionClient, Button, ActionRow, ButtonStyle

client = commands.Bot(command_prefix = 't.', case_insensitive = True)
slash = InteractionClient(client)

@client.event
async def on_ready():
    # Set the bot's activity to be listening
    await client.change_presence(activity = discord.Game(name = 'Listening to t.help!'))
    print('Bot is ready and status was set.')

@client.command()
async def ping(ctx):
    Embed = discord.Embed(title = "Pong!", description = f"{round(client.latency * 1000)}ms!", color = 0x00ff00)
    await ctx.send(embed = Embed)

@client.command()
async def invite(ctx):
    embed = discord.Embed(title = "Invite me to your server!", description = "Invite link: [here](https://discord.com/api/oauth2/authorize?client_id=986730397968785518&permissions=8&scope=bot)", color = 0x00ff00)
    await ctx.send(embed = embed)

@client.command()
async def about(ctx):
    embed = discord.Embed(title = "About me!", description = """
Hi, I'm a bot made by BlakePrograms#0001 for the TGC Discord server. I was made since the admin of the server wanted a bot for the server which could be controlled by a secured user, ensuring any backdoors are sealed. I'm still a growing bot, so I'm always looking for new ideas on features and commands.
    """
    , color = 0x00ff00)
    await ctx.send(embed = embed)

# set a command cooldown of 10 minutes
@client.command()
async def idea(ctx, catogory, *, idea):
    ideas = ['general', 'feature', 'command']

    if catogory.lower() not in ideas:
        embed = discord.Embed(title = "Error!", color = 0x00ff00)
        embed.add_field(name = "Catorgory", value = "Please enter a valid catogory.")
        embed.add_field(name = "Available catogories", value = "general, feature, command")
        await ctx.send(embed = embed)

    if catogory.lower() == 'command':
        channel_id = 986739167448928349
        channel = client.get_channel(channel_id)

        embed = discord.Embed(title = "New command idea!", color = 0x00ff00)
        embed.add_field(name = "From", value = f"{ctx.author.mention}")
        embed.add_field(name = "Idea", value = idea)
        await channel.send(embed = embed)

        embed = discord.Embed(title = "Success!", color = 0x00ff00)
        embed.add_field(name = "Message", value = "Your idea has been sent to the command idea channel.")
        await ctx.send(embed = embed)

    
    if catogory.lower() == 'feature':
        channel_id = 986739167448928349
        channel = client.get_channel(channel_id)

        embed = discord.Embed(title = "New feature idea!", color = 0x00ff00)
        embed.add_field(name = "From", value = f"{ctx.author.mention}")
        embed.add_field(name = "Idea", value = idea)
        await channel.send(embed = embed)

        embed = discord.Embed(title = "Success!", color = 0x00ff00)
        embed.add_field(name = "Message", value = "Your idea has been sent to the feature idea channel.")
        await ctx.send(embed = embed)
    
    if catogory.lower() == 'general':
        channel_id = 986739167448928349
        channel = client.get_channel(channel_id)

        embed = discord.Embed(title = "New general idea!", color = 0x00ff00)
        embed.add_field(name = "From", value = f"{ctx.author.mention}")
        embed.add_field(name = "Idea", value = idea)
        await channel.send(embed = embed)

        embed = discord.Embed(title = "Success!", color = 0x00ff00)
        embed.add_field(name = "Message", value = "Your idea has been sent to the general idea channel.")
        await ctx.send(embed = embed)

@commands.has_permissions(administrator = True)
@client.command()
async def ban(ctx, member: discord.Member, *, reason = "No reason specified."):

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

    embed = discord.Embed(title = "Moderation system notification", color = 0x00ff00)
    embed.add_field(name = "Action", value = "Banned")
    embed.add_field(name = "User", value = "You.")
    embed.add_field(name = "Reason", value = reason)
    embed.add_field(name = "Moderator", value = f"{ctx.author.mention}")
    await member.send(embed = embed)

    await member.ban(reason = reason)

@slash.command(
    name = 'help',
    description = 'Shows the help menu.',
    guild_ids = [981611193984749578]
)
async def help(ctx):
    embed = discord.Embed(title = "Help menu", color = 0x00ff00)
    embed.add_field(name = "t.help", value = "Shows the help menu.")
    embed.add_field(name = "t.ping", value = "Shows the bot latency.")
    embed.add_field(name = "t.invite", value = "Shows the bot invite link.")
    embed.add_field(name = "t.about", value = "Shows the bot about me.")
    embed.add_field(name = "t.idea", value = "Send ideas to the owners!.")
    embed.add_field(name = "t.ban", value = "Bans the mentioned user.")
    embed.add_field(name = "t.kick", value = "Kicks the user mentioned.")

    await ctx.send(embed = embed)

@client.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return

    if message.content.startswith('t.ping'):
        return

    with open('messages.txt', 'a') as f:
        f.writelines(f'{message.author.name}: {message.content}\n')

@commands.is_owner()
@slash.command(
    name = 'message-logs',
    description = 'Sends the message logs to the owner.',
    guild_ids = [981611193984749578]
)
async def MessageLogs(ctx):
    with open('messages.txt', 'r') as f:
        # send the owner the message logs file
        await ctx.author.send(file = discord.File(f, 'messages.txt'))

client.run('OTg2NzMwMzk3OTY4Nzg1NTE4.GbAMrq.vlb3wjzuzbTJWLztfO6x8LaBfiKn5wHbQ3DEF8')