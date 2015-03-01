import wx

import panels

class Main_Window(wx.Frame):
    def __init__(self, parent, title = 'Corio Control', *args, **kwargs):
        wx.Frame.__init__(self, parent, title = title, *args, **kwargs)
        
        panels.Main_Panel(self)
        
        self.Show()