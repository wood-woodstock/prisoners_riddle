import pygame
from rect import *
from label import *

class Box(Rect):
   def __init__(self):
      super().__init__()
      self.label_number=Label()
      self.label_content=Label()
      self.LoadBgImg('imgs/box_open.png')
      self.LoadFgImg('imgs/box_closed.png')
      w=self.bg_surf.get_width()
      h=self.bg_surf.get_height()
      self.SetSize(w,h)
      self.SetBgColor(0x960096FF)
      self.label_content.SetBgColor(0xFFFFFF00)
      self.label_content.SetFgColor(0x000000FF)
      self.number=0
      self.content=0
      self.opened=False

   def SetSize(self,w,h):
      # ~16px each char, 3 char == 48
      fsize=int(w/48*10)
      # print("Box.SetSize: ",fsize)
      self.label_number.SetFontSize(fsize)
      # self.label_number.CenterOn(w,0)
      self.label_number.SetPos(int(w*0.5),int(h*0.5))
      self.label_content.SetFontSize(fsize)
      self.label_content.CenterOn(w,h)
      super().SetSize(w,h)

   def SetNumber(self,n):
      self.LoadBgImg('imgs/box_open.png')
      self.number=n
      self.label_number.SetText("{:03}".format(n))
      # self.label_number.CenterOn(self.w,0)
      self.label_number.SetPos(int(self.w*0.45),int(self.h*0.55))

   def SetContent(self,n):
      self.content=n
      self.label_content.SetText("{:03}".format(n))
      x=self.w//3
      y=self.h//3
      self.label_content.SetPos(x,y)
      # self.label_content.CenterOn(self.w,self.h)

   def Show(self):
      self.opened=True

   def Hide(self):
      self.opened=False

   def Draw(self,scr):
      if(scr==None):
         return
      if self.opened:
         scr.blit(self.bg_surf,self.pos)
      else:
         scr.blit(self.fg_surf,self.pos)

   def Render(self):
      self.label_number.Render()
      self.label_number.Rotate(27)
      self.label_number.Draw(self.fg_surf)
      self.label_number.Draw(self.bg_surf)

      if(self.opened):
         self.label_content.Render()
         self.label_content.Draw(self.bg_surf)
      else:
         pass