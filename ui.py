import pathlib
import pygubu
import tkinter as tk
import tkinter.ttk as ttk


PADX = 30
PADY = 20
class NewprojectApp:
    def __init__(self, master=None):
        # build ui
        self.nb = ttk.Notebook(root)
        self.nb.pack()
        self.mainFrame = ttk.Frame(master)
        self.button1 = ttk.Button(self.mainFrame)
        self.img_lightbulbiconOn = tk.PhotoImage(file='light-bulb-icon.png')
        self.img_lightbulbiconOff = tk.PhotoImage(file='light-bulb-icon-off.png')
        self.switch1Text = tk.StringVar(value='switch1 (OFF)')
        self.button1.configure(compound='top', cursor='sailboat', image=self.img_lightbulbiconOff, state='normal')
        self.button1.configure(text='switch1', textvariable=self.switch1Text)
        self.button1.grid(column='0', ipadx='0', ipady='0', padx=PADX, pady=PADY, row='0')
        self.button1.configure(command=self.toggleSwitch1)
        self.button1State = False
        self.button2 = ttk.Button(self.mainFrame)
        self.switch2Text = tk.StringVar(value='switch2 (OFF)')
        self.button2.configure(compound='top', cursor='sailboat', image=self.img_lightbulbiconOff, state='normal')
        self.button2.configure(text='switch2', textvariable=self.switch2Text)
        self.button2.grid(column='1', ipadx='0', ipady='0', padx=PADX, pady=PADY, row='0')
        self.button2.configure(command=self.toggleSwitch2)
        self.button2State = False
        self.button3 = ttk.Button(self.mainFrame)
        self.switch3Text = tk.StringVar(value='switch3 (OFF)')
        self.button3.configure(compound='top', cursor='sailboat', image=self.img_lightbulbiconOff, state='normal')
        self.button3.configure(text='switch3', textvariable=self.switch3Text)
        self.button3.grid(column='2', ipadx='0', ipady='0', padx=PADX, pady=PADY, row='0')
        self.button3.configure(command=self.toggleSwitch3)
        self.button3State = False
        self.button4 = ttk.Button(self.mainFrame)
        self.switch4Text = tk.StringVar(value='switch4 (OFF)')
        self.button4.configure(compound='top', cursor='sailboat', image=self.img_lightbulbiconOff, state='normal')
        self.button4.configure(text='switch4', textvariable=self.switch4Text)
        self.button4.grid(column='3', ipadx='0', ipady='0', padx=PADX, pady=PADY, row='0')
        self.button4.configure(command=self.toggleSwitch4)
        self.button4State = False
        self.button5 = ttk.Button(self.mainFrame)
        self.switch5Text = tk.StringVar(value='switch5 (OFF)')
        self.button5.configure(compound='top', cursor='sailboat', image=self.img_lightbulbiconOff, state='normal')
        self.button5.configure(text='switch5', textvariable=self.switch5Text)
        self.button5.grid(column='0', ipadx='0', ipady='0', padx=PADX, pady=PADY, row='1')
        self.button5.configure(command=self.toggleSwitch5)
        self.button5State = False
        self.button6 = ttk.Button(self.mainFrame)
        self.switch6Text = tk.StringVar(value='switch6 (OFF)')
        self.button6.configure(compound='top', cursor='sailboat', image=self.img_lightbulbiconOff, state='normal')
        self.button6.configure(text='switch6', textvariable=self.switch6Text)
        self.button6.grid(column='1', ipadx='0', ipady='0', padx=PADX, pady=PADY, row='1')
        self.button6.configure(command=self.toggleSwitch6)
        self.button6State = False
        self.button7 = ttk.Button(self.mainFrame)
        self.switch7Text = tk.StringVar(value='switch7 (OFF)')
        self.button7.configure(compound='top', cursor='sailboat', image=self.img_lightbulbiconOff, state='normal')
        self.button7.configure(text='switch7', textvariable=self.switch7Text)
        self.button7.grid(column='2', ipadx='0', ipady='0', padx=PADX, pady=PADY, row='1')
        self.button7.configure(command=self.toggleSwitch7)
        self.button7State = False
        self.button8 = ttk.Button(self.mainFrame)
        self.switch8Text = tk.StringVar(value='switch8 (OFF)')
        self.button8.configure(compound='top', cursor='sailboat', image=self.img_lightbulbiconOff, state='normal')
        self.button8.configure(text='switch8', textvariable=self.switch8Text)
        self.button8.grid(column='3', ipadx='0', ipady='0', padx=PADX, pady=PADY, row='1')
        self.button8.configure(command=self.toggleSwitch8)
        self.button8State = False
        self.mainFrame.configure(cursor='pirate', height='600', width='800')
        # self.mainFrame.grid(column='0', row='0')
        self.nb.add(self.mainFrame,text="main")

        # second page
        self.options = ttk.Frame(master)
        self.update = ttk.Button(self.options)
        self.img_update = tk.PhotoImage(file='update.png')
        self.update.configure(compound='top', image=self.img_update, text='Update')
        self.update.grid(column='2', padx='220', pady='40', row='0')
        self.update.configure(command=self.runUpdate)
        self.exit = ttk.Button(self.options)
        self.img_exit = tk.PhotoImage(file='exit.png')
        self.exit.configure(compound='top', cursor='arrow', image=self.img_exit, state='normal')
        self.exit.configure(text='Exit')
        self.exit.grid(column='2', padx='220', pady='40', row='1')
        self.exit.configure(command=self.closeUI)
        self.options.configure(height='200', width='200')
        self.nb.add(self.options,text="options")     
        # Main widget
        self.mainwindow = self.nb
    
    def run(self):
        self.mainwindow.mainloop()

    def toggleSwitch1(self):
        if self.button1State:
            self.button1.configure(compound='top', cursor='sailboat', image=self.img_lightbulbiconOff, state='normal')
            self.switch1Text = tk.StringVar(value='switch1 (OFF)')
            self.button1.configure(text='switch1', textvariable=self.switch1Text)    
            print("turned off 1")
            self.button1State = False
        else:
            self.button1.configure(compound='top', cursor='sailboat', image=self.img_lightbulbiconOn, state='normal')
            self.switch1Text = tk.StringVar(value="switch1 (ON)")
            self.button1.configure(text='switch1', textvariable=self.switch1Text) 
            print("turned on 1")
            self.button1State = True

    def toggleSwitch2(self):
        if self.button2State:
            self.button2.configure(compound='top', cursor='sailboat', image=self.img_lightbulbiconOff, state='normal')    
            self.switch2Text = tk.StringVar(value='switch2 (OFF)')
            self.button2.configure(text='switch2', textvariable=self.switch2Text)    
            print("turned off 2")
            self.button2State = False
        else:
            self.button2.configure(compound='top', cursor='sailboat', image=self.img_lightbulbiconOn, state='normal')    
            self.switch2Text = tk.StringVar(value='switch2 (ON)')
            self.button2.configure(text='switch2', textvariable=self.switch2Text)    
            print("turned on 2")
            self.button2State = True

    def toggleSwitch3(self):
        if self.button3State:
            self.button3.configure(compound='top', cursor='sailboat', image=self.img_lightbulbiconOff, state='normal')    
            self.switch3Text = tk.StringVar(value='switch3 (OFF)')
            self.button3.configure(text='switch3', textvariable=self.switch3Text)    
            print("turned off 3")
            self.button3State = False
        else:
            self.button3.configure(compound='top', cursor='sailboat', image=self.img_lightbulbiconOn, state='normal')    
            self.switch3Text = tk.StringVar(value='switch3 (ON)')
            self.button3.configure(text='switch3', textvariable=self.switch3Text)    
            print("turned on 3")
            self.button3State = True

    def toggleSwitch4(self):
        if self.button4State:
            self.button4.configure(compound='top', cursor='sailboat', image=self.img_lightbulbiconOff, state='normal')    
            self.switch4Text = tk.StringVar(value='switch4 (OFF)')
            self.button4.configure(text='switch4', textvariable=self.switch4Text)    
            print("turned off 4")
            self.button4State = False
        else:
            self.button4.configure(compound='top', cursor='sailboat', image=self.img_lightbulbiconOn, state='normal')    
            self.switch4Text = tk.StringVar(value='switch4 (ON)')
            self.button4.configure(text='switch4', textvariable=self.switch4Text)    
            print("turned on 4")
            self.button4State = True

    def toggleSwitch5(self):
        if self.button5State:
            self.button5.configure(compound='top', cursor='sailboat', image=self.img_lightbulbiconOff, state='normal')    
            self.switch5Text = tk.StringVar(value='switch5 (OFF)')
            self.button5.configure(text='switch5', textvariable=self.switch5Text)    
            print("turned off 5")
            self.button5State = False
        else:
            self.button5.configure(compound='top', cursor='sailboat', image=self.img_lightbulbiconOn, state='normal')    
            self.switch5Text = tk.StringVar(value='switch5 (ON)')
            self.button5.configure(text='switch5', textvariable=self.switch5Text)    
            print("turned on 5")
            self.button5State = True

    def toggleSwitch6(self):
        if self.button6State:
            self.button6.configure(compound='top', cursor='sailboat', image=self.img_lightbulbiconOff, state='normal')    
            self.switch6Text = tk.StringVar(value='switch6 (OFF)')
            self.button6.configure(text='switch6', textvariable=self.switch6Text)    
            print("turned off 6")
            self.button6State = False
        else:
            self.button6.configure(compound='top', cursor='sailboat', image=self.img_lightbulbiconOn, state='normal')    
            self.switch6Text = tk.StringVar(value='switch6 (ON)')
            self.button6.configure(text='switch6', textvariable=self.switch6Text)    
            print("turned on 6")
            self.button6State = True

    def toggleSwitch7(self):
        if self.button7State:
            self.button7.configure(compound='top', cursor='sailboat', image=self.img_lightbulbiconOff, state='normal')    
            self.switch7Text = tk.StringVar(value='switch7 (OFF)')
            self.button7.configure(text='switch7', textvariable=self.switch7Text)    
            print("turned off 7")
            self.button7State = False
        else:
            self.button7.configure(compound='top', cursor='sailboat', image=self.img_lightbulbiconOn, state='normal')    
            self.switch7Text = tk.StringVar(value='switch7 (ON)')
            self.button7.configure(text='switch7', textvariable=self.switch7Text)    
            print("turned on 7")
            self.button7State = True

    def toggleSwitch8(self):
        if self.button8State:
            self.button8.configure(compound='top', cursor='sailboat', image=self.img_lightbulbiconOff, state='normal')    
            self.switch8Text = tk.StringVar(value='switch8 (OFF)')
            self.button8.configure(text='switch8', textvariable=self.switch8Text)    
            print("turned off 8")
            self.button8State = False
        else:
            self.button8.configure(compound='top', cursor='sailboat', image=self.img_lightbulbiconOn, state='normal')    
            self.switch8Text = tk.StringVar(value='switch8 (ON)')
            self.button8.configure(text='switch8', textvariable=self.switch8Text)    
            print("turned on 8")
            self.button8State = True
    
    def runUpdate(self):
        import os
        import subprocess
        import time
        dir_path = os.path.dirname(os.path.realpath(__file__))
        os.chdir(dir_path)
        updateProcess = subprocess.Popen("git pull", shell=True)
        # while updateProcess.poll() is None: time.sleep(0.1)
        self.img_updated = tk.PhotoImage(file='updated.png')
        self.update.configure(compound='top', image=self.img_updated, text='Updated!')

    def closeUI(self):
        root.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    style = ttk.Style()
    style.theme_create( "MyStyle", parent="vista", settings={
        # "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0] } },
        "TNotebook.Tab": {"configure": {"padding": [120, 10] },}})

    style.theme_use("MyStyle")
    app = NewprojectApp(root)
    app.run()


