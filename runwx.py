#!/usr/bin/env python3

### IMPORTS ###
import wx

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class HelloFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        # Ensure the parent's __init__ is called
        super().__init__(*args, **kwargs)
        
        # Create a panel in the frame
        hf_panel = wx.Panel(self)
        
        # Put stuff in
        st = wx.StaticText(hf_panel, label="Hello World!", pos=(25, 25))
        font = st.GetFont()
        font.PointSize = font.PointSize + 10
        font = font.Bold()
        st.SetFont(font)
        
        self.makeMenuBar()
        
        self.CreateStatusBar()
        self.SetStatusText("Welcome to wxPython!")
    
    def makeMenuBar(self):
        # Make a file menu with hello and exit items
        fileMenu = wx.Menu()
        helloItem = fileMenu.Append(-1, "&Hello...\tCtrl-H", "Help string shown in status bar for this menu item")
        fileMenu.AppendSeparator()
        exitItem = fileMenu.Append(wx.ID_EXIT)
        
        # Make a help menu with an about item
        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT)
        
        # Make a menubar and add the menus
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(helpMenu, "&Help")
        self.SetMenuBar(menuBar)
        
        # Associate handler functions
        self.Bind(wx.EVT_MENU, self.OnHello, helloItem)
        self.Bind(wx.EVT_MENU, self.OnExit, exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)
    
    def OnExit(self, event):
        self.Close(True)
    
    def OnHello(self, event):
        wx.MessageBox("Hello again from wxPython")
    
    def OnAbout(self, event):
        wx.MessageBox("This is a wxPython Hello World sample", "About Hello World 2", wx.OK | wx.ICON_INFORMATION)

class DerivedApp(wx.App):
    def OnInit(self):
        # Initialization and creation of the base/first frame
        the_frame = HelloFrame(None, title = "Hello World 2")
        the_frame.Show(True)
        return True

### MAIN ###
def main():
    app = DerivedApp()
    app.MainLoop()

if __name__ == '__main__':
    main()
