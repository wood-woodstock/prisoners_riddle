import pygame
from random import randint
from copy import copy
from math import sqrt,ceil,floor
from rect import *
from box import *
from prisoner import *

class Room(Rect):
   def __init__(self):
      super().__init__()
      self.prisoner=Prisoner()
      self.wincolor=0x00FF00FF
      self.losecolor=0xFF0000FF
      self.total=0
      self.done=False
      self.occupied=False
      self.boxes=[]
      self.sorted=[]
      self.SetPos(0,0)
      self.SetSize(0,0)
      self.x_spc=3
      self.y_spc=3

   def SetTotal(self,total):
      if(total==0):
         return
      self.total=total
      self.boxes.clear()

      # for n in range(1,total+1):
      #    self.boxes.append(Box())
      #    self.boxes[-1].SetNumber(n)
      self.boxes=[Box() for _ in range(total)]
      # self.sorted=[False for _ in range(1,total+1)]
      self.Fill()
      self.CalcSize()

   def CalcSize(self):
      self.cols=ceil(sqrt(self.total))
      self.rows=floor(sqrt(self.total))
      if(self.cols*self.rows<self.total):
         self.rows=self.rows+1
      self.w=self.cols*self.boxes[0].w
      self.h=self.rows*self.boxes[0].h

   def CenterOn(self,w,h):
      x=int((w-self.w)/2)
      y=int((h-self.h)/2)
      self.SetPos(x,y)

   def Click(self,pos):
      mx,my=pos
      mx=mx-self.x
      my=my-self.y
      if(self.prisoner==None):
         return(None)
      for b in self.boxes:
         if(b.GetClick((mx,my))):
            if(self.prisoner.number!=0):
               b.Show()
               return(b)
      return(None)

   def CheckBox(self,b):
      if(self.prisoner==None):
         return
      self.prisoner.CheckBox(b)

      if(self.prisoner.win!=0):
         self.done=True
         if(self.prisoner.win==1):
            self.prisoner.SetBgColor(self.wincolor)
         elif(self.prisoner.win==-1):
            self.prisoner.SetBgColor(self.losecolor)

   def Reset(self):
      self.done=False
      self.occupied=False
      self.attempts=0
      self.prisoner=Prisoner()
      for b in self.boxes:
         b.Hide()

   def Fill(self):
      self.sorted=[False for _ in range(1,self.total+1)]
      n=1
      for b in self.boxes:
         rnd=randint(1,self.total)
         while(self.sorted[rnd-1]):
            rnd=randint(1,self.total)
         b.SetNumber(n)
         b.SetContent(rnd)
         self.sorted[rnd-1]=True
         n=n+1

   def DistributeBoxes(self):
      x_max=(self.cols*(self.boxes[0].w+self.x_spc))+self.x_spc
      y_max=(self.rows*(self.boxes[0].h+self.y_spc))+self.y_spc+self.prisoner.h

      c=1 # Column
      r=0 # Row
      x=self.x_spc
      y=self.y_spc+self.prisoner.h

      for b in self.boxes:
         b.SetPos(x,y)
         x=x+b.w+self.x_spc
         if(c==self.cols):
            x=self.x_spc
            y=y+b.h+self.y_spc
            c=0
         c=c+1

      self.SetSize(x_max,y_max)
      self.fg_surf=pg.Surface(self.size,pg.SRCALPHA)
      self.bg_surf=pg.Surface(self.size,pg.SRCALPHA)

   def SetSpace(self,spc):
      self.x_spc=spc
      self.y_spc=spc

   def EnterPrisoner(self,p):
      self.Reset()
      self.occupied=True
      self.prisoner=copy(p)
      # self.prisoner.SetSize(36,60)

   def ExitPrisonerTo(self,q):
      q.AddPrisoner(self.prisoner)
      self.prisoner=Prisoner()
      self.occupied=False

   # def ExitPrisoner(self):
   #    self.prisoner=None
   #    self.occupied=False
   #    return(self.prisoner)

   def IncrementTotal(self):
      self.total=self.total+1
      self.boxes.append(Box())
      self.boxes[-1].SetNumber(self.total)
      self.CalcSize()
      # self.SetTotal(self.total+1)

   def DecrementTotal(self):
      if(self.total-1>=1):
         self.total=self.total-1
         self.boxes.pop(-1)
         self.CalcSize()
         # self.SetTotal(self.total-1)

   def Render(self):
      self.FillBgColor()
      self.FillFgColor()
      if(self.prisoner):
         x=(self.w-self.prisoner.w)//2
         self.prisoner.SetPos(x,0)
         self.prisoner.Render()
         self.prisoner.Draw(self.fg_surf)

      for b in self.boxes:
         b.Render()
         b.Draw(self.fg_surf)