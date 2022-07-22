from rect import *
from label import *

class Stats(Rect):
   def __init__(self):
      super().__init__()
      self.lb_total=Label()
      self.lb_checked=Label()
      self.lb_win=Label()
      self.lb_lost=Label()
      self.total=0
      self.checked=0
      self.win=0
      self.lost=0
      self.lb_checked.SetText("Checked: 000; ")
      self.lb_lost.SetText("Lost: 000; ")
      self.lb_win.SetText("Win: 000; ")
      self.lb_total.SetText("Total: 000")
      self.SetFontSize(18)

   def IncChecked(self):
      self.checked=self.checked+1
      self.lb_checked.SetText("Checked: {:03}; ".format(self.checked))

   def ResetChecked(self):
      self.checked=0
      self.lb_checked.SetText("Checked: {:03}; ".format(self.checked))

   def IncLost(self):
      self.lost=self.lost+1
      self.lb_lost.SetText("Lost: {:03}; ".format(self.lost))

   def IncWin(self):
      self.win=self.win+1
      self.lb_win.SetText("Win: {:03}; ".format(self.win))

   def SetTotal(self,n):
      self.total=n
      self.lb_total.SetText("Total: {:03}".format(n))

   def SetFontSize(self,sz):
      self.lb_total.SetFontSize(sz)
      self.lb_checked.SetFontSize(sz)
      self.lb_win.SetFontSize(sz)
      self.lb_lost.SetFontSize(sz)
      self.CalcSize()

   def CalcSize(self):
      max_w=self.lb_total.w
      max_w=max_w+self.lb_checked.w
      max_w=max_w+self.lb_win.w
      max_w=max_w+self.lb_lost.w
      max_h=self.lb_total.h
      self.CalcPos()
      self.SetSize(max_w,max_h)
      self.fg_surf=pg.Surface(self.size,pg.SRCALPHA)

   def SetBgColor(self,cl):
      self.lb_total.SetBgColor(cl)
      self.lb_checked.SetBgColor(cl)
      self.lb_win.SetBgColor(cl)
      self.lb_lost.SetBgColor(cl)

   def SetFgColor(self,cl):
      self.lb_total.SetFgColor(cl)
      self.lb_checked.SetFgColor(cl)
      self.lb_win.SetFgColor(cl)
      self.lb_lost.SetFgColor(cl)

   def CalcPos(self):
      self.lb_checked.SetPos(0,0)
      self.lb_lost.SetPos(self.lb_checked.x+self.lb_checked.w,0)
      self.lb_win.SetPos(self.lb_lost.x+self.lb_lost.w,0)
      self.lb_total.SetPos(self.lb_win.x+self.lb_win.w,0)

   def CenterAtBottom(self,w_win,h_win):
      x=(w_win-self.w)//2
      y=h_win-self.h
      self.SetPos(x,y)

   def Update(self):
      self.lb_checked.SetText("Checked: {:03}; ".format(self.checked))
      self.lb_lost.SetText("Lost: {:03}; ".format(self.lost))
      self.lb_win.SetText("Win: {:03}; ".format(self.win))
      self.lb_total.SetText("Total: {:03}".format(self.total))
      self.lb_total.Render()
      self.lb_checked.Render()
      self.lb_lost.Render()
      self.lb_win.Render()

   def Reset(self):
      self.total=0
      self.checked=0
      self.win=0
      self.lost=0
      self.Update()

   def Render(self):
      self.FillBgColor()

      self.lb_total.Draw(self.fg_surf)
      self.lb_checked.Draw(self.fg_surf)
      self.lb_lost.Draw(self.fg_surf)
      self.lb_win.Draw(self.fg_surf)