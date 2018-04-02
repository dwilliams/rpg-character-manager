#!/usr/bin/env python3

### IMPORTS ###
import logging
import wx

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class HelloFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        # Ensure the parent's __init__ is called
        super().__init__(*args, **kwargs)

        # Setup logging for the class
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("Initializing")

        # Create an image list to be used in the listctrl
        self.logolist = wx.ImageList(32, 32)
        sr_logo_bitmap = wx.Bitmap()
        sr_logo_bitmap.LoadFile("sr_logo.png")
        self.logolist.Add(sr_logo_bitmap)

        # Create a panel in the frame
        hf_panel = wx.Panel(self)

        # Put stuff in
        #st = wx.StaticText(hf_panel, label="Hello World!", pos=(25, 25))
        #font = st.GetFont()
        #font.PointSize = font.PointSize + 10
        #font = font.Bold()
        #st.SetFont(font)

        self.makeMenuBar()

        self.CreateStatusBar()
        self.SetStatusText("Welcome to wxPython!")

        # Overall sizers
        sizer1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer2 = wx.BoxSizer(wx.VERTICAL)
        sizer3 = wx.BoxSizer(wx.VERTICAL)
        sizer1.Add(sizer2, 0, 0, 0)
        sizer2.Add(sizer3, 1, wx.EXPAND | wx.ALL, 1)

        # Char list
        self.listctrl1 = wx.ListCtrl(self, size = wx.Size(250, 600), style = (wx.LC_ICON | wx.LC_ALIGN_LEFT))
        self.listctrl1.SetImageList(self.logolist, wx.IMAGE_LIST_NORMAL)
        sizer2.Add(self.listctrl1, 0, 0, 0)

        # Buttons below list
        sizer4 = wx.BoxSizer(wx.HORIZONTAL)
        button1 = wx.Button(self, label = "Add Char")
        self.Bind(wx.EVT_BUTTON, self.OnAddButton, button1)
        button2 = wx.Button(self, label = "Del Char")
        self.Bind(wx.EVT_BUTTON, self.OnDelButton, button2)
        sizer4.Add(button1, 0, 0, 0)
        sizer4.Add(button2, 0, 0, 0)
        sizer2.Add(sizer4, 0, 0, 0)

        self.SetSizerAndFit(sizer1)

    def makeMenuBar(self):
        self.logger.debug("makeMenuBar")
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
        self.logger.debug("OnExit")
        self.Close(True)

    def OnHello(self, event):
        self.logger.debug("OnHello")
        wx.MessageBox("Hello again from wxPython")

    def OnAbout(self, event):
        self.logger.debug("OnAbout")
        wx.MessageBox("This is a wxPython Hello World sample", "About Hello World 2", wx.OK | wx.ICON_INFORMATION)

    def OnAddButton(self, event):
        self.logger.debug("OnAddButton")
        # Open a dialog asking for game type, char name, etc
        # Gather the info from the dialog
        # Create a new listctrl item
        #new_list_item = wx.ListItem()
        #new_list_item.SetImage(0)
        #new_list_item.SetText("Character One")
        self.listctrl1.InsertItem(0, "Character One", 0)
        pass

    def OnDelButton(self, event):
        self.logger.debug("OnDelButton")
        # Remove the selected character from the listctrl
        pass

class DerivedApp(wx.App):
    def OnInit(self):
        # Setup logging for the class
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("Initializing")

        # Initialization and creation of the base/first frame
        the_frame = HelloFrame(None, title = "Hello World 2")
        the_frame.Show(True)
        return True

### MAIN ###
def main():
    # Init Logging
    logging.basicConfig(level=logging.DEBUG)

    app = DerivedApp()
    app.MainLoop()

if __name__ == '__main__':
    main()
