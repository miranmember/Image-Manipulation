######################################################
# Project: Project 4
# Student Name:  Member, Miran
# UIN: 654424039
# repl.it URL: https://repl.it/@mmembe2/Project-4
######################################################
from PIL import Image
import random

class ImageSpecial:
  def __init__ (self, image):
    self.image=image.copy()
  
  def set_background(self, rgb):
    h, w = self.image.size
    for x in range(w):
      for y in range(h):
        r,g,b,a =self.image.getpixel((x,y))
        if ( a == 0):
          self.image.putpixel((x,y),rgb)

  def remove_color(self,color):
    h, w = self.image.size
    if color=='red':
      for x in range(w):
        for y in range(h):
          r,g,b,a =self.image.getpixel((x,y))
          if (a!=0):
            if (r<(g+b)):
              self.image.putpixel((x,y),(0,g,b))
    elif color=='green':
      for x in range(w):
        for y in range(h):
          r,g,b,a =self.image.getpixel((x,y))
          if (a!=0):
            if (g<(r+b)):
              self.image.putpixel((x,y),(r,0,b))
    elif color=='blue':
      for x in range(w):
        for y in range(h):
          r,g,b,a =self.image.getpixel((x,y))
          if (a!=0):
            if (b<(g+r)):
              mirror_x = h-x-1  
              self.image.putpixel((mirror_x,y), (r,g,b))
  
  def mirror_img(self):
    h,w= self.image.size
    for x in range(int(w/2)):
      for y in range(h):
        r,g,b,a = self.image.getpixel((x,y))
        if (a!=0):
          mirror_x = h-x-1  
          self.image.putpixel((mirror_x,y), (r,g,b))   

  def set_color(self,color):
    h, w = self.image.size
    for x in range(w):
      for y in range(h):
        r,g,b,a =self.image.getpixel((x,y))
        if (a!=0):
          if color=='red':
            new=(255,g,b)
            self.image.putpixel((x,y),new)
          if color=='blue':
            new=(r,g,int(b/2))
            self.image.putpixel((x,y),new)
          if color=='green':
            new=(r,255,b)
            self.image.putpixel((x,y),new)
  
  def rotate_img(self,value):
    self.image = self.image.rotate(value)


        

def main():
  img=Image.open("Chrome_Canary.png")
  h,w= img.size
  rand_w=random.randrange(1,5)
  rand_h=random.randrange(2,5)
  new = Image.new(img.mode,(rand_h*h,rand_w*w),'blue')
  counter=0
  for row in range(rand_w):
    for col in range(rand_h):
      pic= ImageSpecial(img)
      rand_value=random.randrange(0,9)
      print(rand_value)
      counter+=1
      if counter==1:
        pic.image
      else:
        if rand_value==0:
          pic.set_background((random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)))
        elif rand_value==1:
          pic.set_background((random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)))
          pic.remove_color('red')
        elif rand_value==2:
          pic.set_background((random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)))
          pic.mirror_img()
        elif rand_value==3:
          pic.set_background((random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)))
          pic.set_color('red')
        elif rand_value==4:
          pic.set_background((random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)))
          pic.rotate_img(random.randrange(10,180))
        elif rand_value==5:
          pic.remove_color('blue')
        elif rand_value==6:
          pic.set_color('green')
        elif rand_value==7:
          pic.set_color('blue')
        else:
          pic.remove_color('green')
        
      paste_x=col*h
      paste_y=row*w
      new.paste(pic.image, (paste_x,paste_y))
  new.save('image_654424039.png')

main()
