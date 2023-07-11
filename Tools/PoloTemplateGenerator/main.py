from PIL import Image, ImageDraw, ImageFont
import math,os
height=int(input('Height: '))
width=int(input('Width: '))
headHeight=int(input('Head Height: '))
headscount=int(input('Head Count: '))
if os.path.exists('coordinates.txt'):
    os.remove('coordinates.txt')
nearest5=5*math.ceil(headscount/5)
rows=nearest5/5
col=nearest5/rows
print(width*col)
print(height+17+(rows*headHeight))
template=Image.new('RGBA',(int(width*col),int(height+17+(rows*headHeight))), (255, 255, 255, 0))
draw=ImageDraw.Draw(template)
draw.rectangle((0,0,width,height), fill=(255,0,0))
draw.text((width/2-width/10,height/2-height/20),"Default",fill=(0,0,0))
draw.rectangle((width,0,width*2,height), fill=(0,255,0))
draw.text((width+width/2-width/10,height/2-height/20),"Headless",fill=(0,0,0))
draw.rectangle((width*2,0,width*3,height), fill=(0,0,255))
draw.text((2*width+width/2-width/10,height/2-height/20),"Siloette",fill=(0,0,0))

heads=Image.new('RGBA',(int(width*col),int((rows*headHeight))), (255, 255, 255, 0))
headswidth=width*col
headsheight=rows*headHeight
draw2=ImageDraw.Draw(heads)
count=0
textcount=0
for i in range(0,int(rows)):
    for j in range(0,int(col)):
        count+=1
        textcount+=1
        if not textcount > headscount:
            if count%2 == 0:
                draw2.rectangle((j*width,i*headHeight,(j+1)*width,(i+1)*headHeight),fill=(255,255,0))
            else:
                draw2.rectangle((j*width,i*headHeight,(j+1)*width,(i+1)*headHeight),fill=(0,255,255))
            draw2.text((j*width,i*headHeight),f"Head {textcount}",fill=(0,0,0))
            with open('coordinates.txt','a') as f:
                f.write(f'Head {textcount} Coords: {j*width},{i*headHeight+height}\n')

template.paste(heads,(0,height+17),heads)
template.save('template.png')