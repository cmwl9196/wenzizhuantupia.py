from PIL import Image

def 解密(im):
    width,height = im.size
    lst = []
    a = int(input('密码'))
    for y in range(height):
        for x in range(width):
            r,g,b = im.getpixel((x,y))
            if (b|g|r) == 0:
                break
            index = (g<<8) + b
            
            lst.append(chr(index ^ a))

    return ''.join(lst)

if __name__ == '__main__':

    all_text = 解密(Image.open("结果.bmp","r"))
    with open("结果.txt","w",encoding="utf-8") as f:
        f.write(all_text)