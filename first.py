import os
import shutil
import tkinter as tk
import tkinter.messagebox as msg
base = tk.Tk()
base.geometry('400x200')
base.title('File Sorter')
path1 = tk.StringVar()
tk.Label(base,text = 'WELCOME TO THE FILE SORTER',font ='Bold' ).place(x=72,y=40)
tk.Label(base,text = 'Folder Path').place(x=80,y=80)
tk.Entry(base,text = path1,width =15).place(x=200,y=80)
tk.Button(base,text = 'Exit',command = quit,bg='lightgrey').place(x=290,y=130)
def sort():
    if path1.get() == '':
        msg.showinfo('Error','Please Enter The Path')
        quit
    else:
        path = path1.get()+'/'
        name = os.listdir(path)
        foldername = ['image','documents','mp3','mp4']
        for i in foldername:
          if not os.path.exists(path+i):
             os.makedirs(path+i)
        for j in name:
            if ".jpg" in j or '.png' in j and not os.path.exists(path+'image/'+j):
               shutil.move(path+j,path+'image/'+j)
            elif '.mp3' in j and not os.path.exists(path + 'mp3/' + j):
                shutil.move(path+j,path+'mp3/'+j)
            elif 'txt' in j and not os.path.exists(path + 'documents/' + j):
                shutil.move(path+j, path+'documents/'+j)
            elif '.webm' in j and not os.path.exists(path + 'mp4/' + j):
                shutil.move(path+j, path+'mp4/'+j)
        msg.showinfo('Complete','Sorting completed')
        quit

tk.Button(base,text = 'Start',command = sort,bg='lightgrey').place(x=50,y=130)
base.mainloop()
