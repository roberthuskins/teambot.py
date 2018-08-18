import discord
import asyncio
from load import get_team
from load import potential_formats


client = discord.Client()

#replace the character between the quotes if you would like to change the command prefix
prefix = "-"

@client.event
async def on_ready():
    game = discord.Game(name="{}team <format>".format(prefix))
    await client.change_presence(game=game)
    print('------')
    print("USERNAME: " + client.user.name)
    print("ID: " + client.user.id)
    print("PREFIX: " + prefix)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith(prefix + "team"):
        format = ""
        command = message.content.upper()

        for x in potential_formats:
            if x.upper() in command:
                format = x
                break

        if format != "":
            await client.send_message(message.author, "```" + get_team(format) + "```")
            await client.send_message(message.channel, "Team PM'd.")
        else:
            await client.send_message(message.channel, "Format not recognized. Please use one of these formats:\n" + str(list(potential_formats)))



client.run('YOUR_TOKEN_HERE')
