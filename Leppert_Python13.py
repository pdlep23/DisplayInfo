import tkinter

class infoDisplayGUI:
	def __init__(self):
	#create a main window
		self.main_window = tkinter.Tk()
		#create a top frame and lower frame
		self.top_frame = tkinter.Frame(self.main_window)
		self.bottom_frame = tkinter.Frame(self.main_window)
		#set the showinfo to a string variable
		self.info = tkinter.StringVar()
		#create the label using the self info
		self.info_label = tkinter.Label(self.top_frame, textvariable = self.info)
		self.info_label.pack()
		
		#create the show info button which will call the show_info and the quit button which will exit
		self.show_button = tkinter.Button(self.bottom_frame, text='Show Info', command=self.show_info)
		self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)
		#display the buttons on the screen
		self.show_button.pack(side='left')
		self.quit_button.pack(side='right')
		#pack them
		self.top_frame.pack()
		self.bottom_frame.pack()
		#create the main loop
		tkinter.mainloop()
	
	#create my information for the self
	def show_info(self):
		name = 'Dylan Leppert'
		address = '1234 Hollywood Way'
		city = 'Burbank'
		state = 'California'
		zip = '91502'
		self.info.set(name + '\n' + address + '\n' + city + ', ' + state + ' ' + zip)
	
#create an instance of the class
my_info = infoDisplayGUI()