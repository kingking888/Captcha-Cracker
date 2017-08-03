from PIL import Image
import os
def ParseCaptcha(img):
    captcha=""
    dirs=os.listdir("Chars")
    pix=img.load()
    for y in range(1,49):
        for x in range(1,149):
            if pix[x,y-1]==(255,255,255) and pix[x,y]==(0,0,0) and pix[x,y+1]==(255,255,255):
                pix[x,y]=(255,255,255)
            if pix[x-1,y]==(255,255,255) and pix[x,y]==(0,0,0) and pix[x+1,y]==(255,255,255):
                pix[x,y]=(255,255,255)
    for j in range(25,151,25):
        ch=img.crop((j-25,19,j,49))
        pix1=ch.load()
        for i in dirs:
            match=0
            black=0
            im2=Image.open("Chars\\"+i)
            pix2=im2.load()
            for y in range(0,30):
                for x in range(0,25):
                    if pix1[x,y]==pix2[x,y] and pix2[x,y]==(0,0,0):
                        match+=1
                    if pix2[x,y]==(0,0,0):
                        black+=1
            if float(match)/float(black)>=0.94:
                captcha+=str(i[0]).upper()
    return captcha
def main():
    img=Image.open("10.png")
    print ParseCaptcha(img)
main()
    
                
            
