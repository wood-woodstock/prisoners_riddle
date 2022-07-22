import pygame as pg
from rect import *

class Label(Rect):
   def __init__(self):
      super().__init__()
      self.fsize=32
      self.font=pg.font.SysFont("lucidaconsole",self.fsize)
      self.text=""
      self.SetBgColor(0x00000000)
      self.SetFgColor(0xFFFFFFFF)

   def SetText(self,text):
      self.text=text
      (w,h)=self.font.size(text)
      self.SetSize(w,h)

   def SetFontSize(self,n):
      self.fsize=n
      self.font=pg.font.SysFont("lucidaconsole",n)
      (w,h)=self.font.size(self.text)
      self.SetSize(w,h)

   def CenterOn(self,w,h):
      if(w==0):
         x=0
      else:
         x=int((w-self.w)/2)
      if(h==0):
         y=0
      else:
         y=int((h-self.h)/2)
      self.SetPos(x,y)

   def Rotate(self,ang):
      if(self.fg_surf):
         (w,h)=self.fg_surf.get_size()
         if((w!=0) and (h!=0)):
            self.fg_surf=pg.transform.rotate(self.fg_surf,ang)
      if(self.bg_surf):
         (w,h)=self.bg_surf.get_size()
         if((w!=0) and (h!=0)):
            self.bg_surf=pg.transform.rotate(self.bg_surf,ang)

   def Render(self):
      if(self.bg_color[-1]!=0):
         self.FillBgColor()
      self.fg_surf=self.font.render(self.text,True,self.fg_color)