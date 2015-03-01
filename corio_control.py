def main():
    import wx

    import gui.frames
    
    app = wx.App(False)
    
    gui.frames.Main_Window(None)
    
    app.MainLoop()
    
if __name__ == '__main__':
    main()