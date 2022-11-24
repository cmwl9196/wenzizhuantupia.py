from PIL import Image
import math as ma
def 加密(text):
    str_len = len(text)
    width = ma.ceil(str_len**0.5)
    im = Image.new('RGB',(width,width),0x0)

    x,y = 0,0
    a = int(input('密码'))
    for i in text:
        index = ord(i) ^ a
        rgb = (255,(index & 0xFF00)>>8,index & 0xFF)
        im.putpixel((x,y),rgb)
        if x == width -1:
            x = 0
            y += 1
        else:
            x += 1
    return im

if __name__ == '__main__':
    with open("XXX.txt",encoding='utf-8') as f:
        all_text = f.read()
    im = 加密(all_text)
    im.save('结果.bmp')
