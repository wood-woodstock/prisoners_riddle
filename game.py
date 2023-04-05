import pygame as pg
from rect import *
import menu as mn
import line as ln
import room as rm
import stats as st
import colors as cl

class Game(Rect):
   def __init__(self):
      super().__init__()
      super().SetSize(1024,768)
      self.SetBgColor(cl.BACKGROUND_HEX)
      self.scr=pg.display.set_mode((self.w,self.h),pg.RESIZABLE)
      self.run=True
      self.menu=mn.Menu()
      self.stats=st.Stats()
      self.room=rm.Room()
      self.in_line=ln.Line()
      self.out_line=ln.Line()

   def Init(self):
      pg.display.set_caption("Prisoners Riddle")
      self.bg_surf=pg.Surface(self.size,pg.SRCALPHA)
      self.fg_surf=pg.Surface(self.size,pg.SRCALPHA)
      self.menu.CalcSize()
      self.menu.Align(self.w,self.h)
      self.menu.SetBgColor(cl.MENU_BG)
      self.menu.Render()
      total=20
      self.stats.CenterAtBottom(self.w,self.h)
      self.stats.SetBgColor(cl.STATS_BG)
      self.stats.SetTotal(total)
      self.stats.Update()
      self.stats.Render()
      self.room.SetTotal(total)
      self.room.Fill()
      self.room.DistributeBoxes()
      self.room.CenterOn(self.w,self.h)
      self.room.SetBgColor(cl.ROOM_BG)
      self.room.Render()
      self.in_line.SetWinHeight(self.h)
      self.in_line.SetTotal(total)
      self.in_line.SetBgColor(cl.LINE_BG)
      self.in_line.DistributePrisoners()
      self.in_line.Render()
      self.out_line.SetWinHeight(self.h)
      self.out_line.SetPos(self.w-80,0)
      self.out_line.SetBgColor(cl.LINE_BG)
      self.out_line.Render()

   def Reset(self):
      self.room.Reset()
      self.room.Fill()
      self.room.DistributeBoxes()
      self.stats.Reset()
      self.stats.SetTotal(self.room.total)
      self.in_line.Reset()
      self.out_line.Clear()

   def Increment(self):
      self.room.IncrementTotal()
      self.room.DistributeBoxes()
      self.stats.SetTotal(self.room.total)
      self.room.CenterOn(self.w,self.h)
      self.in_line.IncrementTotal()
      self.out_line.Clear()
      self.room.Reset()
      self.room.Render()
      self.in_line.Render()
      self.out_line.Render()

   def Decrement(self):
      self.room.DecrementTotal()
      self.room.DistributeBoxes()
      self.stats.SetTotal(self.room.total)
      self.room.CenterOn(self.w,self.h)
      self.in_line.DecrementTotal()
      self.out_line.Clear()
      self.room.Reset()
      self.room.Render()
      self.in_line.Render()
      self.out_line.Render()

   def Resize(self,w,h):
      self.SetSize(w,h)
      self.scr=pg.display.set_mode((w,h),pg.RESIZABLE)
      self.bg_surf=pg.Surface(self.size,pg.SRCALPHA)
      self.fg_surf=pg.Surface(self.size,pg.SRCALPHA)

      self.room.CenterOn(w,h)

      # in_line.SetSize(0,WinH)
      self.in_line.SetWinHeight(h)
      self.in_line.Render()

      # out_line.SetSize(0,WinH)
      self.out_line.SetWinHeight(h)
      self.out_line.RightAlign(w)
      self.out_line.Render()

      self.stats.CenterAtBottom(w,h)
      self.stats.Render()

      self.menu.Align(w,h)

   def HandleEvents(self):
      for event in pg.event.get():
         if(event.type==pg.MOUSEBUTTONDOWN):
            pass

         if(event.type==pg.MOUSEBUTTONUP):
            if(event.button==1):
               p=self.in_line.Click(event.pos)
               act=self.menu.GetClick(event.pos)
               if act >= 0:                  
                  if act == 0:
                     self.Reset()
                  elif act == 1:
                     self.Increment()
                  elif act == 2:
                     self.Decrement()

               if(p):
                  if(not self.room.occupied):
                     self.room.EnterPrisoner(p)
                     self.stats.ResetChecked()
                     self.in_line.RemPrisoner(p)
                     self.in_line.Render()

               b=self.room.Click(event.pos)

               if(b):
                  self.room.CheckBox(b)
                  self.stats.IncChecked()
                  self.stats.Render()
               if(self.room.done):
                  if(self.room.prisoner.win==1):
                     self.stats.IncWin()
                  elif(self.room.prisoner.win==-1):
                     self.stats.IncLost()
                  self.stats.Render()
                  self.room.ExitPrisonerTo(self.out_line)
                  self.out_line.RightAlign(self.w)
                  self.out_line.Render()
                  self.room.Reset()

               self.stats.Update()
               self.stats.Render()
               self.room.Render()

         if(event.type==pg.VIDEORESIZE):
            self.Resize(event.w,event.h)

         if(event.type==pg.QUIT):
            self.run=False
            break

   def Loop(self):
      while(self.run):
         self.HandleEvents()
         self.Render()
         self.Draw(self.scr)
         pg.display.flip()

   def Render(self):
      self.FillBgColor()
      self.FillFgColor()
      self.room.Draw(self.fg_surf)
      self.stats.Draw(self.fg_surf)
      self.menu.Draw(self.fg_surf)
      self.in_line.Draw(self.fg_surf)
      self.out_line.Draw(self.fg_surf)