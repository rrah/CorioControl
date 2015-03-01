import wx

from buttons import Corio_Button, Textctrl

from Device import corio

import socket

def error_message():
    dlg = wx.MessageDialog(None, message = 'Oops! There\'s been an error', style = wx.OK)
    return dlg.ShowModal()

class Main_Panel(wx.Panel):
    
    def __init__(self, *args, **kwargs):
        
        wx.Panel.__init__(self, *args, **kwargs)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        
        self.corio = corio.Corio(host = 'localhost', port = 2003)
        
        self.host_text = Textctrl(self, label = 'Host')
        self.port_text = Textctrl(self, label = 'Port')
        self.connect_button = wx.Button(self, label = 'Connect')
        
        # Button for fading in and out
        self.fade_button = Corio_Button(self, device = self.corio)
        self.fade_button.Enable(False)
        self._connected = False
        
        sizer.AddMany([(self.host_text), (self.port_text), (self.connect_button), (self.fade_button)])
        
        self.SetSizer(sizer)
        
        # All the bindings
        self.Bind(wx.EVT_BUTTON, self.on_fade_button, self.fade_button)
        self.Bind(wx.EVT_BUTTON, self.on_connect_button, self.connect_button)
        
    def on_fade_button(self, e):
        
        try:
            button = e.GetEventObject()
            if button.faded_in:
                button.fade_out()
            else:
                button.fade_in()
        except socket.error:
            error_message()
            
            
    def on_connect_button(self, e):
        
        try:
            if self._connected:
                self.fade_button.Enable(False)
                self.fade_button.SetBackgroundColour((255,255,255))
                self.connect_button.SetLabel('Connect')
                self._connected = False
            else:
                self.corio.setHost(self.host_text.GetValue())
                self.corio.setPort(int(self.port_text.GetValue()))
                if self.corio.update():
                    if self.corio.is_faded_in():
                        self.fade_button.SetLabel('Fade out')
                        self.fade_button.SetBackgroundColour((255, 0, 0))
                        self.faded_in = True
                    else:
                        self.fade_button.SetLabel('Fade in')
                        self.fade_button.SetBackgroundColour((0, 255, 0))
                        self.faded_in = False
                    self.fade_button.Enable(True)
                    self._connected = True
                    self.connect_button.SetLabel('Disconnect')
        except socket.timeout:
            error_message()
        
    