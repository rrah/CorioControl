import wx

from time import sleep

from common import fade_speed_to_seconds
    

class Corio_Button(wx.Button):
    def __init__(self, parent, device = None, label = 'Fade in', size = (160, 160), *args, **kwargs):
        wx.Button.__init__(self, parent, label = label, size = size, *args, **kwargs)
        self.faded_in = False
        self.corio = device
        
    def fade_in(self):
        with self.corio:
            if self.corio.fade_in():
                self.fading()
                self.SetLabel('Fade out')
                self.SetBackgroundColour((255, 0, 0))
                self.faded_in = True
        
     
    def fade_out(self):
        with self.corio:
            if self.corio.fade_out():
                self.fading()
                self.SetLabel('Fade in')
                self.SetBackgroundColour((0, 255, 0))
                self.faded_in = False
        
        
    def fading(self):
        
        self.SetLabel('Fading')
        self.SetBackgroundColour((0, 0, 0))
        sleep(fade_speed_to_seconds(self.corio.get_fade_speed()))
        
    def Enable(self, *args, **kwargs):
        return wx.Button.Enable(self, *args, **kwargs)
        
class Textctrl(wx.BoxSizer):
    
    """
    Allows easy setting of wxTextCtrl with added label.""" 
    
    def SetValue(self, *args, **kwargs):
        
        return self.text_ctrl.SetValue(*args, **kwargs)
        
    def GetValue(self, *args, **kwargs):
        
        return self.text_ctrl.GetValue(*args, **kwargs)
    
    def __init__(self, parent, label = None, *args, **kwargs):
        wx.BoxSizer.__init__(self, wx.HORIZONTAL)
        self.text_ctrl = wx.TextCtrl(parent, *args, **kwargs)
        text_label = wx.StaticText(parent, label = label)
        
        self.AddMany([(text_label, 3, wx.EXPAND), (self.text_ctrl, 7, wx.EXPAND)])