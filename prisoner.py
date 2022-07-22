import pygame
from label import Label
from rect import *

class Prisoner(Rect):
   def __init__(self):
      super().__init__()
      self.number=0
      self.attempts=0
      self.max_attempts=0
      self.win=0
      self.SetBgColor(0x80808000)
      self.SetFgColor(0x961496FF)
      self.label=Label()
      self.label.SetBgColor(0xFFFFFFFF)
      self.label.SetFgColor(0x000000FF)
      self.LoadBgImg("imgs/prisoner.png")
      self.LoadFgImg("imgs/prisoner.png")
      # self.LoadFgImg("data/cage.png")
      # self.SetSize(36,60)

   def SetSize(self,w,h):
      # ~16px each char, 3 char == 48
      fsize=int(w/48*18)
      # print("Prisoner.SetSize: ",fsize)
      self.label.SetFontSize(fsize)
      # self.label.CenterOn(w,h)
      # h=h+self.label.h
      self.label.SetPos(w//2,self.h)
      super().SetSize(w,h)

   def SetNumber(self,n):
      self.number=n
      self.label.SetText("{:03}".format(n))
      self.label.CenterOn(self.w,self.h+20)

   def SetMaxAttempts(self,n):
      self.max_attempts=n

   def CheckBox(self,b):
      self.attempts=self.attempts+1
      if(self.number==b.content):
         self.win=1
      else:
         if(self.attempts>self.max_attempts):
            self.win=-1

   def Render(self):
      self.FillBgColor()
      if(self.fg_surf==None):
         self.fg_surf=pg.Surface(self.size,pg.SRCALPHA)
      self.label.Render()
      self.label.Draw(self.fg_surf)