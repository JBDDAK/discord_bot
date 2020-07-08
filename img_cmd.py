from PIL import Image, ImageDraw, ImageFont
import discord

selectedFont = ImageFont.truetype('fonts/gulim.ttc', 21)

async def JH_emoticon(message):
    target_img = Image.open('images/JH_img.png')
    draw = ImageDraw.Draw(target_img)
    msg = message.content.split(" ")
    msg = "".join(msg[1:])
    print(msg)
    draw.text((330, 45), msg, fill="black", font=selectedFont)

    target_img.save('images/asdf.png')
    await message.delete()
    await message.channel.send(file=discord.File('images/asdf.png'))

async def JW_emoticon(message):
    target_img = Image.open('images/JW_img.png')
    draw = ImageDraw.Draw(target_img)
    msg = message.content.split(" ")
    msg = "".join(msg[1:])

    draw.text((300, 50), msg, fill="black", font=selectedFont)

    target_img.save('images/qwer.png')
    await message.delete()
    await message.channel.send(file=discord.File('images/qwer.png'))

