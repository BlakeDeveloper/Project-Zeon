import discord
from discord.ext import commands
import os
from dislash import *
import time

client = commands.AutoShardedBot(command_prefix = 't.')
slash = InteractionClient(client)
client.remove_command('help')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


@slash.command(
    name = 'help',
    description = 'Shows the help menu with sub-catergories.',
    guilds_ids = 981611193984749578,
)
async def help(ctx):
    row_of_buttons = ActionRow(
        Button(
            style=ButtonStyle.green,
            label="Moderation",
            custom_id="Moderation"
        ),
        Button(
            style=ButtonStyle.red,
            label="Utilites",
            custom_id="Utilites"
        )
    )
    # Send a message with buttons
    embed = discord.Embed(title = 'Help menu', description = 'Select a category using the buttons from below', color = 0x00ff00)
    embed.add_field(name = 'Note', value = 'This command is very new to me so you will experience bugs. **IGNORE THE INTERACTION FAILED**', inline = False)


    msg = await ctx.send(
        embed = embed,
        components=[row_of_buttons]
    )
    # Wait for someone to click on them
    def check(inter):
        return inter.message.id == msg.id
    # Wait until the button is clicked
    inter = await client.wait_for('interaction', check=check)
    # Get the custom id of the button that was clicked
    custom_id = inter.button.custom_id

    # if the button hasnt been click in 30 seconds delete the message
    def check_timeout(inter):
        return time.time() - inter.time_created > 30
    
    if custom_id == 'Moderation':
        embed = discord.Embed(title = 'Moderation', color = 0x00ff00)
        embed.add_field(name = 'Ban', value = 'Bans a user from the server.')
        embed.add_field(name = 'Kick', value = 'Kicks a user from the server.')
        embed.add_field(name = 'Purge', value = 'Purges a number of messages from the channel.')
        await msg.edit(embed = embed, components=[row_of_buttons])

        await time.sleep(10)
        await msg.delete()
        await help(ctx)
    
    elif custom_id == 'Utilites':
        embed = discord.Embed(title = 'Utilites', color = 0x00ff00)
        embed.add_field(name = 'Help', value = 'Shows the help menu.')
        embed.add_field(name = 'Ping', value = 'Shows the ping of the bot.')
        embed.add_field(name = 'Userinfo', value = 'Shows the info of a user.')
        embed.add_field(name = 'Serverinfo', value = 'Shows the info of the server.')
        embed.set_footer(text = 'This message will be deleted in 10 seconds.')
        await msg.edit(embed = embed, components=[row_of_buttons])

        await time.sleep(10)
        await msg.delete()
        await help(ctx)


client.run('OTg2NzMwMzk3OTY4Nzg1NTE4.GbAMrq.vlb3wjzuzbTJWLztfO6x8LaBfiKn5wHbQ3DEF8')