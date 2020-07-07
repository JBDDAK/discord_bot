import discord
from PIL import Image, ImageDraw, ImageFont

target_img = Image.open('images/image.png')
selectedFont = ImageFont.truetype('fonts/gulim.ttc', 24)
draw = ImageDraw.Draw(target_img)
y = 60

msg = "!정훈티콘 테 스트"
msg = msg.split(" ")
str = " ".join(msg[1:])
str = str.split("-")
print()

for i in range(len(str)):
    draw.text((340, y), str[i], fill="black", font=selectedFont)
    y+=24
target_img.save('images/asdf.png')

