import discord
import rename
import img_cmd
import re
import dont_touch
client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("앙기무링")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("!정훈티콘"):
        await img_cmd.img_cmd(message)
    elif len(re.findall("현[^현구]*구", message.content)) != 0:
        await rename.rename(message)

client.run(dont_touch.token)