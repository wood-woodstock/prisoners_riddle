from rect import *

class Screen(Rect):
   def __init__(self):
      super().__init__()
      self.title="100 Prisoners Riddle"
      self.SetSize(1024,768)
      self.flags=pg.RESIZABLE
      self.scr=None
      pg.display.set_caption(self.title)

   def SetTitle(self,title):
      self.title=title
      pg.display.set_caption(self.title)

   def Resize(self,w,h):
      super().SetSize(w,h)
      self.scr=pg.display.set_mode(self.size,self.flags)
      pass

   def Render(self,rm,iq,oq,st):
      self.FillBgColor()
      rm.Draw(self.fg_surf)
      iq.Draw(self.fg_surf)
      oq.Draw(self.fg_surf)
      st.Draw(self.fg_surf)
      pass

   def Draw(self, scr):
      return super().Draw(scr)