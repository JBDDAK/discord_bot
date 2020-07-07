import re

async def rename(message):
    msg = f"<@{message.author.id}> : " + re.sub("현[^현구]*구", "깜찍", message.content)
    await message.delete()
    message = await message.channel.send(msg)
    # await message.channel.send(message)