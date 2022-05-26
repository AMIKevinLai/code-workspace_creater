from asyncio.windows_events import NULL
from pickle import FALSE
from queue import Empty
from re import X
import tkinter as tk
from tkinter import NW, filedialog
import os

## Function define
# Browse folder function for path
def BrowseProjectFolder():
    Path=tk.filedialog.askdirectory(title='Select Project Path')
    pjpath_var.set(Path)

# Browse file function for path
def BrowseProgramFile():
    Path=tk.filedialog.askopenfilename(title='Select Build Python File Path')
    pgpath_var.set(Path)

# Browse file function for path
def BrowseCwdFolder():
    Path=tk.filedialog.askdirectory(title='Select Intel Folder Path')
    cwdpath_var.set(Path)

# Set How mant config in the .code-workspace file
def SetConfig():
    #Get the user setting number
    number = int(Config_var.get())
    #Initial the config frame
    for i in range(0,number):
        config_frame[i].pack_forget()

    for i in range(0,number):
        config_frame[i].pack(side=tk.LEFT)

## Windows define
window = tk.Tk()
window.title('Create .code_workspace')
window.geometry("1000x800+300+150")

# Empty label define 
# For composition using
empty_label = tk.Label(window, text=' ')
empty_label.grid(row=0, column=0, sticky='w')

## Procject setting
# Procject frame define
pjpath_frame = tk.Frame(window)
pjpath_frame.grid(row=1, column=0, sticky='w')
# Procject Label define
pjpath_label = tk.Label(pjpath_frame, text='Project Path :    ')
pjpath_label.pack(side=tk.LEFT)
# Procject entry define 
pjpath_var = tk.StringVar()
pjpath_entry = tk.Entry(pjpath_frame, textvariable=pjpath_var, width=100)
pjpath_entry.pack(side=tk.LEFT)
# For composition using
empty_label = tk.Label(pjpath_frame, text=' ')
empty_label.pack(side=tk.LEFT)
# Project button define 
pjpath_button = tk.Button(pjpath_frame,             # 按鈕所在視窗
                   text = 'Browse',                 # 顯示文字
                   command = BrowseProjectFolder)   # 按下按鈕所執行的函數
pjpath_button.pack(side=tk.LEFT)


# Empty label define 
# For composition using
empty_label = tk.Label(window, text=' ')
empty_label.grid(row=2, column=0, sticky='w')


## Program setting
# Program frame define
pgpath_frame = tk.Frame(window)
pgpath_frame.grid(row=3, column=0, sticky='w')
# Program Label define
pgpath_label = tk.Label(pgpath_frame, text='Program Path : ')
pgpath_label.pack(side=tk.LEFT)
# Program entry define 
pgpath_var = tk.StringVar()
pgpath_entry = tk.Entry(pgpath_frame, textvariable=pgpath_var, width=100)
pgpath_entry.pack(side=tk.LEFT)
# For composition using
empty_label = tk.Label(pgpath_frame, text=' ')
empty_label.pack(side=tk.LEFT)
# Program button define 
pgpath_button = tk.Button(pgpath_frame,         # 按鈕所在視窗
                   text = 'Browse',             # 顯示文字
                   command = BrowseProgramFile) # 按下按鈕所執行的函數
pgpath_button.pack(side=tk.LEFT)


# Empty label define 
# For composition using
empty_label = tk.Label(window, text=' ')
empty_label.grid(row=4, column=0, sticky='w')


## Program setting
# Program frame define
cwdpath_frame = tk.Frame(window)
cwdpath_frame.grid(row=5, column=0, sticky='w')
# Program Label define
cwdpath_label = tk.Label(cwdpath_frame, text='Cwd Path :         ')
cwdpath_label.pack(side=tk.LEFT)
# Program entry define 
cwdpath_var = tk.StringVar()
cwdpath_entry = tk.Entry(cwdpath_frame, textvariable=cwdpath_var, width=100)
cwdpath_entry.pack(side=tk.LEFT)
# For composition using
empty_label = tk.Label(cwdpath_frame, text=' ')
empty_label.pack(side=tk.LEFT)
# Program button define 
cwdpath_button = tk.Button(cwdpath_frame,       # 按鈕所在視窗
                   text = 'Browse',             # 顯示文字
                   command = BrowseCwdFolder)   # 按下按鈕所執行的函數
cwdpath_button.pack(side=tk.LEFT)


# Empty label define 
# For composition using
empty_label = tk.Label(window, text=' ')
empty_label.grid(row=6, column=0, sticky='w')


# Config number define
Config_var = tk.StringVar()
config_spin = tk.Spinbox(window,textvariable=Config_var, from_=0, to=8)
config_spin.grid(row=7, column=0, sticky='n')
# Config number define (above)
above_config_frame = tk.Frame(window)
above_config_frame.grid(row=10, column=0, sticky='n')
# Empty label define 
# For composition using
empty_label = tk.Label(window, text=' ')
empty_label.grid(row=11, column=0, sticky='w')
# Config number define (bottom)
bottom_config_frame = tk.Frame(window)
bottom_config_frame.grid(row=12, column=0, sticky='n')

# Initial list for use
config_frame = []
config_name_label = []
config_name_var = []
config_name_entry = []
config_arg_label = []
config_arg_var = []
config_arg_entry = []
# Setting the config frame with for loop 
for i in range(0,8):
    if(i < 4):
        #Setting Frame
        config_frame.append(tk.LabelFrame(above_config_frame, width=500, height=50, text="Config - "+ str(i+1)))
        config_frame[i].pack_forget()
    elif(i >= 4):
        #Setting Frame
        config_frame.append(tk.LabelFrame(bottom_config_frame, width=500, height=50, text="Config - "+ str(i+1)))
        config_frame[i].pack_forget()

    #Setting Name Label
    config_name_label.append(tk.Label(config_frame[i], text = 'Name', width=30))
    config_name_label[i].pack(anchor=NW,fill = 'x')
    #Setting Name Entry
    config_name_var.append(tk.StringVar())
    config_name_entry.append(tk.Entry(config_frame[i], textvariable=config_name_var[i], width=25))
    config_name_entry[i].pack()
    #Setting Args Label
    config_arg_label.append(tk.Label(config_frame[i], text = 'Args', width=30))
    config_arg_label[i].pack(anchor=NW,fill = 'x')
    #Setting Args Entry
    config_arg_var.append(tk.StringVar())
    config_arg_entry.append(tk.Entry(config_frame[i], textvariable=config_arg_var[i], width=25))
    config_arg_entry[i].pack()
    # Empty label define 
    # For composition using
    empty_label = tk.Label(config_frame[i], text=' ')
    empty_label.pack()

# Empty label define 
# For composition using
empty_label = tk.Label(window, text=' ')
empty_label.grid(row=8, column=0, sticky='w')


# 建立按鈕
Set_button = tk.Button(window,     # 按鈕所在視窗
                   text = 'Set',  # 顯示文字
                   command = SetConfig) # 按下按鈕所執行的函數
# 以預設方式排版按鈕
Set_button.grid(row=9, column=0, sticky='n')

def WriteFile(workspace_file):
    workspace_file.write("{\n")
    workspace_file.write("  \"folders\": [\n")
    workspace_file.write("    {\n")
    workspace_file.write("      \"path\": \".\"\n")
    workspace_file.write("    }\n")
    workspace_file.write("  ],\n")
    workspace_file.write("  \"settings\": {\n")
    workspace_file.write("    \"launch\": {\n")
    workspace_file.write("      \"configurations\": [\n")

    config_nunber = int(Config_var.get())
    #config_name_var
    #down_config_name_var
    type = "python"
    request = "launch"
    console = "integratedTerminal" 
    pgpath = "${workspaceRoot}" + str(pgpath_var.get()).replace(str(pjpath_var.get()),"")
    cwdpath = "${workspaceFolder}" +  str(cwdpath_var.get()).replace(str(pjpath_var.get()),"") +"/"

    for i in range(config_nunber):
        # Write the file
        workspace_file.write("        {\n")
        workspace_file.write("          \"name\": ")
        workspace_file.write("\""+ config_name_var[i].get() +"\",\n")
        workspace_file.write("          \"type\": ")
        workspace_file.write("\""+ type +"\",\n")
        workspace_file.write("          \"request\": ")
        workspace_file.write("\""+ request +"\",\n")
        workspace_file.write("          \"program\": ")
        workspace_file.write("\""+ pgpath +"\",\n")
        workspace_file.write("          \"console\": ")
        workspace_file.write("\""+ console +"\",\n")
        workspace_file.write("          \"args\": ")
        workspace_file.write("[")

        # Write args in the file
        args = str(config_arg_var[i].get()).split(",")
        for j in range(len(args)):
            arg = args[j].replace("\"","")
            arg = arg.replace(" ","")
            if(j == 0):
                workspace_file.write("\""+arg+"\"")
            else:
                workspace_file.write(", \""+arg+"\"")

        workspace_file.write("],\n")
        workspace_file.write("          \"cwd\": ")
        workspace_file.write("\""+ cwdpath +"\",\n")
        workspace_file.write("        },\n")

    workspace_file.write("      ]\n")
    workspace_file.write("      ,\n")
    workspace_file.write("      \"compounds\": [],\n")
    workspace_file.write("      \"inputs\": [ ],\n")
    workspace_file.write("      \"version\": \"0.2.0\"\n")
    workspace_file.write("    },\n")
    workspace_file.write("  }\n")
    workspace_file.write("}\n")

# Create function
def Create():
    filename="Project.code-workspace"
    path = str(pjpath_var.get())
    #Check if the .code-workspace is exist ot not
    workspace_file = open(path+"/"+filename,'w+')
    WriteFile(workspace_file)


# Empty label define 
# For composition using
empty_label = tk.Label(window, text=' ')
empty_label.grid(row=13, column=0, sticky='w')

# 建立按鈕
Create_button = tk.Button(window,     # 按鈕所在視窗
                   text = 'Create',  # 顯示文字
                   command = Create) # 按下按鈕所執行的函數
# 以預設方式排版按鈕
Create_button.grid(row=14, column=0, sticky='n')

# Main function
window.mainloop()