from rect import *
from label import *

class Menu(Rect):
   def __init__(self):
      super().__init__()
      self.x_spc=4
      self.y_spc=4
      self.bt_reset=Label()
      self.bt_add=Label()
      self.bt_del=Label()

   def Add(self,room,queue):
      room.SetTotal(room.total+1)
      queue.SetTotal(queue.total+1)

   def Rem(self,room,queue):
      room.SetTotal(room.total-1)
      queue.SetTotal(queue.total-1)

   def Align(self,w,h):
      x=(w-self.w)//2
      self.SetPos(x,0)

   def GetClick(self,pos):
      if(super().GetClick(pos)):
         x=pos[0]-self.x
         y=pos[1]-self.y
         pos=(x,y)
         if(self.bt_reset.GetClick(pos)):
            return(0)
         if(self.bt_add.GetClick(pos)):
            return(1)
         if(self.bt_del.GetClick(pos)):
            return(2)
      return(-1)

   def MakeMenu(self):
      # self.bt_reset.SetText("Reset")
      # self.bt_add.SetText("Add")
      # self.bt_del.SetText("Del")
      self.bt_reset.LoadBgImg("imgs/bt_reset.png")
      self.bt_add.LoadBgImg("imgs/bt_plus.png")
      self.bt_del.LoadBgImg("imgs/bt_minus.png")

   def CalcSize(self):
      self.MakeMenu()
      w=self.bt_reset.x+self.bt_reset.w+self.x_spc
      w=w+self.bt_add.x+self.bt_add.w+self.x_spc
      w=w+self.bt_del.x+self.bt_add.w+self.x_spc
      w=w+self.x_spc
      h=self.bt_add.h+self.y_spc
      h=h+self.y_spc
      self.SetSize(w,h)
      if(self.fg_surf==None):
         self.fg_surf=pg.Surface(self.size,pg.SRCALPHA)

   def Render(self):
      self.FillBgColor()

      x=self.x_spc
      y=self.y_spc
      self.bt_reset.SetPos(x,y)
      x=self.bt_reset.x+self.bt_reset.w+self.x_spc
      self.bt_add.SetPos(x,y)
      x=self.bt_add.x+self.bt_add.w+self.x_spc
      self.bt_del.SetPos(x,y)

      self.bt_reset.Render()
      self.bt_add.Render()
      self.bt_del.Render()

      self.bt_reset.Draw(self.fg_surf)
      self.bt_add.Draw(self.fg_surf)
      self.bt_del.Draw(self.fg_surf)