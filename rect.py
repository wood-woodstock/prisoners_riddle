import pygame as pg

class Rect():
   def __init__(self):
      self.x=0
      self.y=0
      self.pos=(self.x,self.y)
      self.w=0
      self.h=0
      self.size=(self.w,self.h)
      self.rect=pg.Rect(self.pos,self.size)
      self.scr=None
      # self.bg_surf=pg.Surface(self.size,pg.SRCALPHA)
      # self.fg_surf=pg.Surface(self.size,pg.SRCALPHA)
      self.bg_surf=None
      self.fg_surf=None
      self.bg_color=(0,0,0,0)
      self.fg_color=(0,0,0,0)

   def SetScreen(self,scr):
      self.scr=scr

   def SetPos(self,x,y):
      self.x=x
      self.y=y
      self.pos=(x,y)
      self.rect=pg.Rect(self.pos,self.size)

   def SetSize(self,w,h):
      if(w!=0):
         self.w=w
      if(h!=0):
         self.h=h
      # self.size=(w,h)
      self.size=(self.w,self.h)
      # print("SetSize:",self.size)
      # self.bg_surf=pg.Surface(self.size,pg.SRCALPHA)
      # self.fg_surf=pg.Surface(self.size,pg.SRCALPHA)
      self.rect=pg.Rect(self.pos,self.size)

   def MaxSize(self,nw,nh):
      w=self.w
      h=self.h
      if(nw>w):
         w=nw
      if(nh>h):
         h=nh
      self.SetSize(w,h)

   def Draw(self,scr):
      if(scr):
         if(self.bg_surf):
            scr.blit(self.bg_surf,self.pos)
         if(self.fg_surf):
            scr.blit(self.fg_surf,self.pos)

   def GetClick(self,pos):
      return(self.rect.collidepoint(pos))
      # if(self.rect.collidepoint(pos)):
      #    return True
      # else:
      #    return False

   def SetBgColor(self,c):
      r=(c>>24)&255
      g=(c>>16)&255
      b=(c>>8)&255
      a=c&255
      self.bg_color=(r,g,b,a)

   def SetFgColor(self,c):
      r=(c>>24)&255
      g=(c>>16)&255
      b=(c>>8)&255
      a=c&255
      self.fg_color=(r,g,b,a)

   def FillBgColor(self):
      if(self.bg_surf==None):
         self.bg_surf=pg.Surface(self.size,pg.SRCALPHA)
      self.bg_surf.fill(self.bg_color)

   def FillFgColor(self):
      if(self.fg_surf==None):
         self.fg_surf=pg.Surface(self.size,pg.SRCALPHA)
      self.fg_surf.fill(self.fg_color)

   def LoadBgImg(self,path):
      self.bg_surf=pg.image.load(path)
      (w,h)=self.bg_surf.get_size()
      self.MaxSize(w,h)

   def LoadFgImg(self,path):
      self.fg_surf=pg.image.load(path)
      (w,h)=self.fg_surf.get_size()
      self.MaxSize(w,h)

   def LoadBgTileImg(self,path,w,h):
      self.SetSize(w,h)
      self.bg_surf=pg.Surface(self.size,pg.SRCALPHA)
      temp=pg.image.load(path)
      tw=temp.get_width()
      th=temp.get_height()
      for y in range(0,h,th):
         for x in range(0,w,tw):
            print(x,y)
            self.bg_surf.blit(temp,(x,y))

      # (w,h)=self.bg_surf.get_size()
      # self.MaxSize(w,h)

   def LoadFgTileImg(self,path,w,h):
      self.SetSize(w,h)
      self.fg_surf=pg.Surface(self.size,pg.SRCALPHA)
      temp=pg.image.load(path)
      tw=temp.get_width()
      th=temp.get_height()
      for y in range(0,h,th):
         for x in range(0,w,tw):
            print(x,y)
            self.fg_surf.blit(temp,(x,y))
