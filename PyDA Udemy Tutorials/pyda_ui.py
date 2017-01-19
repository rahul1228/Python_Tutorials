import wx

class MyFrame(wx.Frame): #class MyFrame inherits from wx.Frame

	# Below function initializes/instatiates a wx Frame with certain perameters
	# 1st creates window then panel in window
	def __init__(self):
		#-- Creates Window --
		wx.Frame.__init__(self, None,
			pos=wx.DefaultPosition, size=wx.Size(450, 100),
			style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN,
			title="PyDA")
			
		#-- Creates Panel --
		panel = wx.Panel(self)  
		mySizer = wx.BoxSizer(wx.VERTICAL)
		lbl = wx.StaticText(panel,
			label="Hello, I am PyDA the Python Digital Assisatant. How can I help you?") #label in panel
		mySizer.Add(lbl, 0, wx.ALL, 5)
		self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER, size=(400,30)) #input area in panel
		self.txt.SetFocus() #focus text
		self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter) #binds PROCESS_ENTER fucntion from above with OnEnter function
		mySizer.Add(self.txt, 0, wx.ALL, 5)
		panel.SetSizer(mySizer) #set sizer to panel
		self.Show() #shows panel in window

	# OnEnter function used above in Bind function from wx
	def OnEnter(self, event):
		input = self.txt.GetValue()
		input = input.lower()
		print "It Worked!"

#Main call
if __name__ == "__main__":
	app = wx.App(True)
	frame = MyFrame()
	app.MainLoop()

