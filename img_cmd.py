from PIL import Image, ImageDraw, ImageFont
import discord

selectedFont = ImageFont.truetype('fonts/gulim.ttc', 24)

async def img_cmd(message):
    target_img = Image.open('images/image.png')
    draw = ImageDraw.Draw(target_img)

    y = 45

    msg = message.content.split(" ")
    str = " ".join(msg[1:]).split("-")


    for i in range(len(str)):
        draw.text((330, y), str[i], fill="black", font=selectedFont)
        y += 24
    target_img.save('images/asdf.png')
    await message.delete()
    await message.channel.send(file=discord.File('images/asdf.png'))
