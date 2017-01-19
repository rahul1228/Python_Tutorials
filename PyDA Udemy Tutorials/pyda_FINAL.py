import wx
import wolframalpha
import wikipedia
import talkey

tts = talkey.Talkey(
    # These languages are given better scoring by the language detector
    # to minimise the chance of it detecting a short string completely incorrectly.
    # Order is not important here
    preferred_languages=['en'],

    # The factor by which preferred_languages gets their score increased, defaults to 80.0
    preferred_factor=80.0,

    # The order of preference of using a TTS engine for a given language.
    # Note, that networked engines (Google, Mary) is disabled by default, and so is dummy
    # default: ['google', 'mary', 'espeak', 'festival', 'pico', 'flite', 'dummy']
    # This sets eSpeak as the preferred engine, the other engines may still be used
    #  if eSpeak doesn't support a requested language.
    engine_preference=['espeak'],

    # Here you segment the configuration by engine
    # Key is the engine SLUG, in this case ``espeak``
    espeak={
        # Specify the engine options:
        'options': {
            'enabled': True,
        },

        # Specify some default voice options
        'defaults': {
                'words_per_minute': 110,
                'variant': 'f4',
        },

        # Here you specify language-specific voice options
        # e.g. for english we prefer the mbrola en1 voice
        'languages': {
            'en': {
                'voice': 'english-mb-en1',
                'words_per_minute': 110
            },
        }
    }
)
tts.say('Welcome Ya Bish!')

class MyFrame(wx.Frame): #class MyFrame inherits from wx.Frame

	# Below function initializes/instatiates a wx Frame with certain perameters
	# 1st creates window then panel in window
	def __init__(self):
		#-- Creates Window --
		wx.Frame.__init__(self, None,
			pos=wx.DefaultPosition, size=wx.Size(450, 200),
			style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN,
			title="PyDA")
			
		#-- Creates Panel --
		panel = wx.Panel(self)  
		mySizer = wx.BoxSizer(wx.VERTICAL)
		lbl = wx.StaticText(panel,
			label="""Hello, I am PyDA the Python Digital Assisatant. How can I help you?\n Format your input as a question (e.g. Who is Lebron James)
			""") #label in panel
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
		try:
			#-- Wolfram Alpha --
			app_id = "XGUKWK-AU3YR5AVAJ"
			client = wolframalpha.Client(app_id) #create client from app_id
			res = client.query(input) #user question put into query function from wolfram
			answer = next(res.results).text #displays results as text. next function keeps running query until text data is found for user question
			print answer
		except:
			#-- Wikipedia --
			input = input.split(' ') # this splits user query for "who is" error fix
			input = " ".join(input[2:]) # omits "who is" from user query 
			print wikipedia.summary(input, sentences=5) 
			# ^wikipedia.summary function takes user inputs and only shows 1st 5 sentences of article


#Main call
if __name__ == "__main__":
	app = wx.App(True)
	frame = MyFrame()
	app.MainLoop()



