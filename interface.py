import customtkinter as ctk
from tkinter import filedialog
import Sorter as s

selected_folder = None

def btnAddFolder_clicked():
    folder = AddFolder.get()
    s.create_if_not_exist(folder)
    show_folders()

def btnAddExtension_Clicked():
    ext = AddExtension.get()
    if selected_folder:
        s.add_ext(ext, selected_folder)
    show_allExtensions()

def select_folder(folder):
    global selected_folder
    selected_folder = folder
    show_allExtensions()

def show_folders():
    for widget in AllFolders.winfo_children():
        widget.destroy()
    for folder in s.folders:
        ctk.CTkButton(AllFolders, text = folder, font = ("Arial", 16), command=lambda f=folder: select_folder(f)).pack(anchor = "w", padx=10)

def show_allExtensions():
    for widget in AllExtensions.winfo_children():
        widget.destroy()
    if selected_folder:
        for ext in s.con[selected_folder]:
            ctk.CTkLabel(AllExtensions, text=ext, font=("Arial", 16)).pack(anchor="w", padx=10)
    

def Set_SourceFolder():
    s.sourceFolder = filedialog.askdirectory()
    lblSourceFolder.configure(text=s.sourceFolder)

app = ctk.CTk()
app.title("Sorter")
app.geometry("1000x700")

title_frame = ctk.CTkFrame(app)
title_frame.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

source_frame = ctk.CTkFrame(app)
source_frame.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

left_frame = ctk.CTkFrame(app)
left_frame.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)

right_frame = ctk.CTkFrame(app)
right_frame.grid(row=2, column=1, sticky="nsew", padx=10, pady=10)

app.columnconfigure(0, weight=1)
app.columnconfigure(1, weight=2)
app.rowconfigure(0, weight=1)
app.rowconfigure(1, weight=3)
app.rowconfigure(2, weight=20)

naslov = ctk.CTkLabel(title_frame, text = "Sorter", font = ("Arial", 24))
naslov.pack(pady = 20)

SourceFolder = ctk.CTkButton(source_frame, text = "Add Source Folder", font = ("Arial", 16), border_color="black", command=Set_SourceFolder)
SourceFolder.pack()
lblSourceFolder = ctk.CTkLabel(source_frame, text = "No folder selected", font = ("Arial", 16))
lblSourceFolder.pack()
Sort = ctk.CTkButton(source_frame, text = "Add Source Folder", font = ("Arial", 16), border_color="black", command=s.Sort)
Sort.pack(pady=10)

lblAddFolder = ctk.CTkLabel(left_frame, text = "Add folder:", font = ("Arial", 16))
lblAddFolder.pack()

AddFolder = ctk.CTkEntry(left_frame, font = ("Arial", 16), border_color="black")
AddFolder.pack()

btnAddFolder = ctk.CTkButton(left_frame, text = "Add Folder", font = ("Arial", 16), border_color="black", command=btnAddFolder_clicked)
btnAddFolder.pack()

AllFolders = ctk.CTkScrollableFrame(left_frame, label_text="Yours sorting folders:")
AllFolders.pack(pady = 10, fill = "both", expand=True)

lblAddExtension = ctk.CTkLabel(right_frame, text = "Add Extension:", font = ("Arial", 16))
lblAddExtension.pack()

AddExtension = ctk.CTkEntry(right_frame, font = ("Arial", 16), border_color="black")
AddExtension.pack()

btnAddExtension = ctk.CTkButton(right_frame, text = "Add Extension:", font = ("Arial", 16), border_color="black", command=btnAddExtension_Clicked)
btnAddExtension.pack()

AllExtensions = ctk.CTkScrollableFrame(right_frame, label_text="Yours extensions for this folder:")
AllExtensions.pack(pady = 10, fill = "both", expand=True)




app.mainloop()


