import wx

import panels

class Main_Window(wx.Frame):
    def __init__(self, parent, title = 'Corio Control', style = wx.STAY_ON_TOP, *args, **kwargs):
        wx.Frame.__init__(self, parent, title = title, *args, **kwargs)
        style = self.GetWindowStyle() | wx.STAY_ON_TOP
        self.SetWindowStyle(style)
        
        panels.Main_Panel(self)
        
        self.Show()