import tkinter as tk
from tkinter import ttk
from tkinter import colorchooser, filedialog, messagebox,font
import os

main_application = tk.Tk()
main_application.geometry('800x500+800+200')
main_application.title("Notepad")


#---------------------------main menu----------------------



main_menu = tk.Menu()

#files icon
new_icon = tk.PhotoImage(file='icons/new.png')
open_icon = tk.PhotoImage(file='icons/open.png')
save_icon = tk.PhotoImage(file='icons/save.png')
save_as_icon = tk.PhotoImage(file='icons/save_as.png')
exit_icon = tk.PhotoImage(file='icons/exit.png')

file = tk.Menu(main_application, tearoff=False)



#edit icon
copy_icon = tk.PhotoImage(file='icons/copy.png')
paste_icon = tk.PhotoImage(file='icons/paste.png')
cut_icon = tk.PhotoImage(file='icons/cut.png')
clear_all_icon = tk.PhotoImage(file='icons/clear_all.png')
find_icon = tk.PhotoImage(file='icons/find.png')

edit = tk.Menu(main_application, tearoff=False)




#view icons
toolbar_icon = tk.PhotoImage(file='icons/toolbar.png')
statusbar_icon = tk.PhotoImage(file='icons/statusbar.png')

view = tk.Menu(main_application, tearoff=False)




#color_thems icons
light_default_icon = tk.PhotoImage(file='icons/light_default.png')
light_plus_icon = tk.PhotoImage(file='icons/light_plus.png')
cyan_icon = tk.PhotoImage(file='icons/cyan.png')
purple_icon = tk.PhotoImage(file='icons/purple.png')
gray_icon = tk.PhotoImage(file='icons/gray.png')#missing
dark_cyan_icon = tk.PhotoImage(file='icons/dark_cyan.png')#missing
medium_purple_icon = tk.PhotoImage(file='icons/medium_purple.png')#missing
silver_icon = tk.PhotoImage(file='icons/silver.png')#missing
neptune_icon = tk.PhotoImage(file='icons/neptune.png')#missing
blue_icon = tk.PhotoImage(file='icons/blue.png')
dark_icon = tk.PhotoImage(file = 'icons/dark.png')



color_theme = tk.Menu(main_application, tearoff=False)


#user choice color

theme_choice = tk.StringVar()



#extra creation about color dict
color_icons = (light_default_icon, light_plus_icon, cyan_icon, purple_icon, gray_icon, dark_cyan_icon, medium_purple_icon, silver_icon, neptune_icon, blue_icon, dark_icon)


color_dict = {
    'Terminal_Color' : ('#ffffff', '#300A24'),  
    'Light Plus' : ('#474747', '#e0e0e0'),
    'Cyan' : ('#FFFFFF', '#6BD4CF'),
    'Purple': ('#41754E', '#300A24'),
    'Gray' : ('#FFFFFF', '#9C9E9B'),
    'Dark_Cyan' : ('#FFFFFF', '#008B8B'),
    'Medium_Purple' : ('#FFFFFF', '#9370DB'),
    'Silver' : ('#000000', '#E6E8FA'),
    'Neptune' : ('#FFFFFF', '#6D9BF1'),
    'Blue' : ('#ededed', '#6b9dc2'),
    'Dark' : ('#ffffff','#000000')


}


help = tk.Menu(main_application, tearoff = False)


help.add_command(label='Contact_Us', compound=tk.LEFT, accelerator='Ctrl+Alt+H')
help.add_command(label='Visit Us', compound=tk.LEFT)





#cascade
main_menu.add_cascade(label='File', menu=file)
main_menu.add_cascade(label='Edit', menu=edit)
main_menu.add_cascade(label='View', menu=view)
main_menu.add_cascade(label='Color_Theme', menu=color_theme)
main_menu.add_cascade(label='Help', menu=help)



#---------------------------end amin menu----------------------


#---------------------------toolbar----------------------


toolbar = ttk.Label(main_application)#creating a label
toolbar.pack(side=tk.TOP, fill = tk.X)

#font box
font_tuple = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(toolbar, width=25, textvariable=font_family, state='readonly')
font_box['values'] = font_tuple
font_box.current(font_tuple.index('Arial'))
font_box.grid(row=0, column=0, padx=2)



#size box
size_var = tk.IntVar()
font_size = ttk.Combobox(toolbar,width=20, textvariable=size_var, state='readonly')
font_size['values'] = tuple(range(8,52,2))
font_size.current(2)
font_size.grid(row=0, column=1, padx=5)


#bold button
bold_icon = tk.PhotoImage(file='icons/bold.png')
bold_btn = ttk.Button(toolbar, image=bold_icon)
bold_btn.grid(row=0, column=2, padx=2)

#italic button
italic_icon = tk.PhotoImage(file='icons/italic.png')
italic_btn = ttk.Button(toolbar, image=italic_icon)
italic_btn.grid(row=0, column=3, padx=2)

#underline button
underline_icon = tk.PhotoImage(file='icons/underline.png')
underline_btn = ttk.Button(toolbar, image=underline_icon)
underline_btn.grid(row=0, column=4, padx=2)


#font color button
font_color_icon = tk.PhotoImage(file = 'icons/color_chooser.png')
font_color_btn = ttk.Button(toolbar, image=font_color_icon)
font_color_btn.grid(row=0, column = 5, padx=2)


#Align left
align_left_icon = tk.PhotoImage(file ='icons/align_left.png')
align_left_btn = ttk.Button(toolbar, image=align_left_icon)
align_left_btn.grid(row=0, column = 6, padx=2)


#Align center
align_center_icon = tk.PhotoImage(file ='icons/align_center.png')
align_center_btn = ttk.Button(toolbar, image=align_center_icon)
align_center_btn.grid(row=0, column = 7, padx=2)


#Align right
align_right_icon = tk.PhotoImage(file ='icons/align_right.png')
align_right_btn = ttk.Button(toolbar, image=align_right_icon)
align_right_btn.grid(row=0, column = 8, padx=2)

#---------------------------end tool bar---------------------





#---------------------------start text editor----------------------

text_editor = tk.Text(main_application)
text_editor.config(wrap='word', relief=tk.FLAT)
scroll_bar = tk.Scrollbar(main_application)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
text_editor.pack(fill=tk.BOTH, expand = True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)



#font family & font size functionality

current_font_familiy = 'Nakula'
current_font_size = 12

def change_font(event=None):
    global current_font_familiy
    current_font_familiy = font_family.get()
    text_editor.configure(font=(current_font_familiy, current_font_size))

font_box.bind("<<ComboboxSelected>>", change_font)


def change_font_size(event=None):
    global current_font_size
    current_font_size = size_var.get()
    text_editor.configure(font=(current_font_familiy,current_font_size))

font_size.bind("<<ComboboxSelected>>",change_font_size)




#Bold button functionality
def change_bold():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight'] == 'normal':
        text_editor.configure(font=(current_font_familiy,current_font_size,'bold'))
    if text_property.actual()['weight'] == 'bold':
        text_editor.configure(font=(current_font_familiy,current_font_size,'normal'))


bold_btn.configure(command=change_bold)


#italic functionality
def change_italic():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant'] == 'roman':
        text_editor.configure(font=(current_font_familiy,current_font_size,'italic'))
    if text_property.actual()['slant'] == 'italic':
        text_editor.configure(font=(current_font_familiy,current_font_size,'roman'))

italic_btn.configure(command=change_italic)


#italic functionality
def change_underline():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline'] == 0:
        text_editor.configure(font=(current_font_familiy,current_font_size,'underline'))
    if text_property.actual()['underline'] == 1:
        text_editor.configure(font=(current_font_familiy,current_font_size,'normal'))

underline_btn.configure(command=change_underline)



#font color functionality
def change_font_color():
    color_var = tk.colorchooser.askcolor()

    text_editor.configure(fg=color_var[1])

font_color_btn.configure(command=change_font_color)


#Align functionality


def align_left():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('left', justify=tk.LEFT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'left')

align_left_btn.configure(command=align_left)


def align_center():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('center', justify=tk.CENTER)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'center')

align_center_btn.configure(command=align_center)




def align_right():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('right', justify=tk.RIGHT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'right')

align_right_btn.configure(command=align_right)








text_editor.configure(font=('Nakula',12))




#---------------------------end text editor----------------------




#---------------------------status bar----------------------

statusbar = ttk.Label(main_application, text='© All rights reserved by "Team of Sober"')#creating a label
statusbar.pack(side=tk.BOTTOM)

#this is something else, I add it as an extra 
text_changed = False
def changed(event=None):
    global text_changed
    if text_editor.edit_modified():
        text_changed = True
        words = len(text_editor.get(1.0,'end-1c').split())
        characters = len(text_editor.get(1.0,'end-1c'))
        statusbar.config(text=f'Characters : {characters} Words : {words}')
    text_editor.edit_modified(False)
text_editor.bind('<<Modified>>',changed)





#---------------------------end status bar---------------------



#---------------------------main menu functionality---------------------



#file commands

#new file functionality
url=''
def new_file(event=None):
    global url
    url=''
    text_editor.delete(1.0, tk.END)

file.add_command(label = "New", image=new_icon, compound = tk.LEFT,accelerator = 'Ctrl + N', command=new_file)


#open file functionality
def open_file(event=None):
    try:
        url = tk.filedialog.askopenfilename(initialdir=os.getcwd,title='Select File', filetypes=(('Text Files','*.txt'), ('All Files','*.*')))
        with open(url,'r') as fr:
            text_editor.delete(1.0, 'end')
            text_editor.insert(1.0,fr.read())
    except FileNotFoundError:
        return
    except:
        return
    main_application.title(os.path.basename(url))

file.add_command(label = "Open", image=open_icon, compound = tk.LEFT,accelerator = 'Ctrl + O',command=open_file)



#save file functionality
def save_file(event=None):
    global url
    try:
        if url:
            content_2 = str(text_editor.get(1.0, tk.END))
            with open(url, 'w', encoding='utf-8') as fw:
                fw.write(content_2)
                
        else:
            url = filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=(('Text Files','*.txt'),('All Files','*.*')))
            content_1 = text_editor.get(1.0,tk.END)
            url.write(content_1)
            url.close()
    except:
        return
        

file.add_command(label = "Save", image=save_icon, compound = tk.LEFT,accelerator = 'Ctrl + S', command=save_file)

#save as functionality
def save_as_file(event=None):
    global url
    try:
        
        content=text_editor.get(1.0, tk.END)
        url = filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=(('Text File','*.txt'), ('All Files','*.*')))
        url.write(content)
        url.close()
    except:
        return

file.add_command(label = "Save As", image=save_as_icon, compound = tk.LEFT,accelerator = 'Ctrl + Alt + S', command=save_as_file)


#exit functionality
def exit_file(event=None):
    global url, text_changed
    try:
        if text_changed:
            mbox = messagebox.askyesnocancel('Warning','Do you want to Save this file?')
            if mbox is True:
                if url:
                    content = text_editor.get(1.0, tk.END)
                    with open(url, 'w', encoding='utf-8') as fw:
                        fw.write(content)
                        main_application.destroy()
                else:
                    content_2 = str(text_editor.get(1.0, tk.END))
                    url = filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=(('Text File','*.txt'), ('All Files','*.*')))
                    url.write(content_2)
                    url.close()
                    main_application.destroy()

            elif mbox is False:
                main_application.destroy()
            
        else:
            main_application.destroy()
    except:
        return


file.add_command(label = "Exit", image=exit_icon, compound = tk.LEFT, accelerator = 'Ctrl + Q',command=exit_file)


#edit commands
edit.add_command(label='Copy', image=copy_icon,compound=tk.LEFT, accelerator='Ctrl + C', command=lambda: text_editor.event_generate("<Control c>"))
edit.add_command(label='Paste', image=paste_icon,compound=tk.LEFT, accelerator='Ctrl + V',command=lambda: text_editor.event_generate("<Control v>"))
edit.add_command(label='Cut', image=cut_icon, compound=tk.LEFT,accelerator='Ctrl + X', command=lambda: text_editor.event_generate("<Control x>"))
edit.add_command(label='Clear_All', image=clear_all_icon, compound=tk.LEFT,accelerator='Ctrl + Alt + X', command=lambda: text_editor.delete(1.0, tk.END))



#find functionality
def find_functionality(event=None):

    def find():
        word = find_entry.get()
        #text_editor.tag_remove('match', '1.0', tk.END)
        matches=0

        if word:
            start_pos = '1.0'
            while True:
                start_pos = text_editor.search(word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match', start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                text_editor.tag_config('match', foreground = 'white', background='black')

    
    def replace():
        word = find_entry.get()
        replace_text = replace_entry.get()
        content = text_editor.get(1.0, tk.END)
        new_content = content.replace(word, replace_text)
        text_editor.delete(1.0,tk.END)
        text_editor.insert(1.0, new_content)

    find_dialogue_frame = tk.Toplevel()
    find_dialogue_frame.title("Find & Replace")
    find_dialogue_frame.geometry('450x250+500+200')
    find_dialogue_frame.resizable(0,0)

    #label frame
    find_dialogue_label_frame = ttk.LabelFrame(find_dialogue_frame, text = 'Find/Replace')
    find_dialogue_label_frame.pack(pady=50)
    tk
    #labels
    find_label = ttk.Label(find_dialogue_label_frame, text='Find : ')
    replace_label = ttk.Label(find_dialogue_label_frame, text='Replace : ')

    #entry box
    find_entry = ttk.Entry(find_dialogue_label_frame, width=20)
    replace_entry = ttk.Entry(find_dialogue_label_frame, width=20)

    #buttons
    find_button = ttk.Button(find_dialogue_label_frame, text='Search', command=find)
    replace_button = ttk.Button(find_dialogue_label_frame, text='Replace', command=replace)

    find_label.grid(row=0, column=0)
    find_entry.grid(row=0, column=1, padx=3, pady=3)

    replace_label.grid(row=1, column=0)
    replace_entry.grid(row=1, column=1, padx=3, pady=3)
    
    find_button.grid(row=2, column=0, padx=3, pady=3)
    replace_button.grid(row=2, column=1, padx=3, pady=3)

    find_dialogue_frame.mainloop()

edit.add_command(label='Find', image=find_icon, compound=tk.LEFT,accelerator='Ctrl + F', command=find_functionality)




#view check buttons


show_toolbar = tk.BooleanVar()
show_toolbar.set(True)
show_statusbar = tk.BooleanVar()
show_statusbar.set(True)



def hide_toolbar(event=None):
    global show_toolbar
    if show_toolbar:
        toolbar.pack_forget()
        show_toolbar = False
    else:
        text_editor.pack_forget()
        statusbar.pack_forget()
        toolbar.pack(side=tk.TOP, fill=tk.X)
        text_editor.pack(fill=tk.BOTH, expand=True)
        statusbar.pack(side=tk.BOTTOM)
        show_toolbar = True


def hide_statusbar(event=None):
    global show_statusbar
    
    if show_statusbar:
        statusbar.pack_forget()
        show_statusbar = False
    else:
        statusbar.pack(side=tk.BOTTOM)
        show_statusbar = True

view.add_checkbutton(label='Toolbar', onvalue=True, offvalue=False, variable=show_toolbar, image=toolbar_icon, compound=tk.LEFT, command=hide_toolbar)
view.add_checkbutton(label='StatusBar', onvalue=True, offvalue=False, variable=show_statusbar, image=statusbar_icon, compound=tk.LEFT, command=hide_statusbar)


#color theme

def change_theme(event=None):
    choosen_theme = theme_choice.get()
    color_tuple = color_dict.get(choosen_theme)
    fg_color, bg_color = color_tuple[0], color_tuple[1]
    text_editor.config(background=bg_color, fg= fg_color)



count = 0
for i in color_dict:
    color_theme.add_radiobutton(label=i, image=color_icons[count], variable=theme_choice, compound=tk.LEFT, command=change_theme)
    count += 1









#---------------------------end main menu functionality----------------------
#bind shortcut keys
main_application.bind('<Control-n>', new_file)
main_application.bind('<Control-o>', open_file)
main_application.bind('<Control-s>', save_file)
main_application.bind('<Control-Alt-s>', save_as_file)
main_application.bind('<Control-q>', exit_file)
main_application.bind('<Control-f>', find_functionality)





main_application.config(menu = main_menu)
main_application.mainloop()