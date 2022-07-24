
from copy import copy
from math import ceil
import pygame as pg
from prisoner import Prisoner
from rect import *

class Line(Rect):
   def __init__(self):
      super().__init__()
      self.prisoners=[]
      self.total=0
      self.x_spc=2
      self.y_spc=2
      self.cols=0
      self.rows=0
      self.win_h=0

   def RoomSize(self,w,h):
      self.SetSize(w-150,h-20)

   def SetWinHeight(self,h):
      self.win_h=h
      self.SetSize(0,h)
      self.DistributePrisoners()

   def SetTotal(self,total):
      if(total==0):
         return
      self.total=total
      self.prisoners.clear()

      for n in range(1,total+1):
         self.prisoners.append(Prisoner())
         self.prisoners[-1].SetNumber(n)
         self.prisoners[-1].SetMaxAttempts(total//2)
      self.CalcSize()

   def Fill(self):
      for n in range(1,self.total+1):
         self.prisoners[n-1].SetNumber(n)
         self.prisoners[n-1].SetMaxAttempts(self.total//2)

   def CalcSize(self):
      self.rows=self.win_h//self.prisoners[-1].h
      self.cols=ceil(self.total/self.rows)
      w=self.cols*(self.prisoners[-1].w+self.x_spc)
      h=self.rows*(self.prisoners[-1].h+self.y_spc)
      self.SetSize(w,h)
      self.fg_surf=pg.Surface(self.size,pg.SRCALPHA)
      self.bg_surf=pg.Surface(self.size,pg.SRCALPHA)

   def IncrementTotal(self):
      self.total=self.total+1
      self.prisoners.append(Prisoner())
      self.prisoners[-1].SetNumber(self.total)
      # self.SetTotal(self.total+1)
      self.DistributePrisoners()
      self.CalcSize()

   def DecrementTotal(self):
      if(self.total-1>=1):
         self.total=self.total-1
         self.prisoners.pop(-1)
         # self.SetTotal(self.total-1)
         self.DistributePrisoners()
         self.CalcSize()

   def Click(self,pos):
      mx,my=pos
      mx=mx-self.x
      my=my-self.y
      for p in self.prisoners:
         if(p.GetClick((mx,my))):
            return(p)
      return(None)

   def DistributePrisoners(self):
      x=self.x_spc
      y=self.y_spc
      r=1
      for p in self.prisoners:
         p.SetPos(x,y)
         y=y+self.y_spc+p.h
         if(r==self.rows):
            y=self.y_spc
            x=x+self.x_spc+p.w
            r=0
         r=r+1
      self.LoadBgTileImg("imgs//tile_brick.png",self.w,self.h)

   def RemPrisoner(self,p):
      self.prisoners.remove(p)

   def AddPrisoner(self,p):
      np=copy(p)
      self.prisoners.append(np)
      self.prisoners[-1].SetNumber(p.number)
      self.total=self.total+1
      self.CalcSize()
      self.DistributePrisoners()

   def Clear(self):
      self.prisoners.clear()
      self.Render()

   def Reset(self):
      self.SetTotal(self.total)
      self.DistributePrisoners()
      self.Render()

   def RightAlign(self,w):
      x=(w-self.w)
      self.SetPos(x,self.y)

   def Render(self):
      # self.FillBgColor()
      self.FillFgColor()
      for p in self.prisoners:
         p.Render()
         p.Draw(self.fg_surf)