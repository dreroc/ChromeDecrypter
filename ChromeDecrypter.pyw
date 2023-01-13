import customtkinter
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import filedialog
import os.path
import os
import sys
import time
import string
import random
import subprocess
import base64

customtkinter.set_default_color_theme("dark-blue")
customtkinter.set_appearance_mode("dark")

class MainScreen(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("ChromeDecrypt ~ UNC0V3R3D")
        self.geometry("700x300")
        self.resizable(False, False)
        self.configure(background="white")
        self.grid_columnconfigure(0,weight=1)

        self.sidebar_frame = customtkinter.CTkFrame(self, width=180, corner_radius=0, height=300)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.sidebar_frame.configure(border_width=1, border_color="white")

        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Home", border_width=1, border_color="white", fg_color="transparent", text_color="white", hover_color="grey", command=self.display_home_frame)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Decrypter", border_width=1, border_color="white", fg_color="transparent", text_color="white", hover_color="grey", command=self.display_decrypter_frame)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, text="Other", border_width=1, border_color="white", fg_color="transparent", text_color="white", hover_color="grey", command=self.display_other_frame)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.sidebar_button_31 = customtkinter.CTkButton(self.sidebar_frame, text=" ", fg_color="transparent", hover=False)
        self.sidebar_button_31.grid(row=5, column=0, padx=20, pady=10)
        self.sidebar_button_32 = customtkinter.CTkButton(self.sidebar_frame, text="Update", border_width=1, border_color="white", fg_color="transparent", text_color="white", hover_color="grey", hover=False, state="disabled")
        self.sidebar_button_32.grid(row=6, column=0, padx=20, pady=10)
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, text="Exit", border_width=1, border_color="white", fg_color="transparent", text_color="white", hover_color="grey", hover=True, command=self.exit)
        self.sidebar_button_4.grid(row=7, column=0, padx=20, pady=12)

        # Create the frame that will appear on the right side of the window
        self.home_frame = customtkinter.CTkFrame(self, width=520, corner_radius=0, height=300)
        self.decrypter_frame = customtkinter.CTkFrame(self, width=520, corner_radius=0, height=300)
        self.other_frame = customtkinter.CTkFrame(self, width=520, corner_radius=0, height=300)

        # Hide the frames initially
        self.display_home_frame()
        self.other_frame.grid_remove()
        self.decrypter_frame.grid_remove()


    def display_home_frame(self):
        # Hide the scripts frame if it is currently displayed
        self.other_frame.grid_remove()
        self.decrypter_frame.grid_remove()
        # Display the home frame
        self.home_frame.grid(row=0, column=1, sticky="nsew")
        self.home_frame.configure(border_width=1, border_color="white")

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self.home_frame, width=300, height=200)
        self.textbox.grid(padx=(20, 0), pady=(20, 0))
        self.textbox.place(relx=0.49, rely=0.41, anchor='center')
        self.textbox.insert("0.0", "Welcome!\n\n" + "Thank you for visiting this small project,\nplease note that this project is currently not\nfinished and can contain bugs.\n\n" + "How to use this ?\nWell just press on the 'Decrypter' Button and start decrypting!\nYou can also take a look at the 'Other' section.\nThere you will find some helpful tools.")
        
        self.textbox.configure(state="disabled")

        self.start_button = customtkinter.CTkButton(self.home_frame, text="Start!", border_width=1, border_color="white", fg_color="MediumBlue", text_color="white", hover_color="DodgerBlue", command=self.display_decrypter_frame)

        self.start_button.place(relx=0.49, rely=0.9, anchor='center')


    def display_decrypter_frame(self):
        # Hide the home frame if it is currently displayed
        self.home_frame.grid_remove()
        self.other_frame.grid_remove()
        # Display the scripts frame
        self.decrypter_frame.grid(row=0, column=1, sticky="nsew")
        self.decrypter_frame.configure(border_width=1, border_color="white")

        self.info_text = customtkinter.CTkTextbox(self.decrypter_frame, width=300, height=110)
        self.info_text.grid(row=0, column=0, padx=(20, 0), pady=(20, 0))
        self.info_text.place(relx=0.49, rely=0.39, anchor='center')
        self.info_text.insert("0.0", "Decrypter\n\n" + "By clicking one of the buttons below, you can\nchoose how to start decrypting.\nNote that some bugs can occur.")

        self.info_text.configure(state="disabled")

        self.SD_button = customtkinter.CTkButton(self.decrypter_frame, text="Self-Decrypter", border_width=1, border_color="white", fg_color="grey16", command=self.self_decrypt_gui)
        self.D_button = customtkinter.CTkButton(self.decrypter_frame, text="Decrypter", border_width=1, border_color="white", fg_color="grey16", command=self.decrypting_pre)

        # Place the boxes in a grid
        self.SD_button.place(relx=0.51, rely=0.8, anchor='w')
        self.D_button.place(relx=0.475, rely=0.8, anchor='e')

    
    def display_other_frame(self):
        self.home_frame.grid_remove()
        self.decrypter_frame.grid_remove()
        # Display the scripts frame
        self.other_frame.grid(row=0, column=1, sticky="nsew")
        self.other_frame.configure(border_width=1, border_color="white")

        self.other_text = customtkinter.CTkTextbox(self.other_frame, width=260, height=76)
        self.other_text.grid(row=0, column=0, padx=(20, 0), pady=(20, 0))
        self.other_text.place(relx=0.49, rely=0.2, anchor='center')
        self.other_text.insert("0.0", "Welcome to this section.\nBelow you can find some useful tools,\nmaybe you need them sometime.\nMore tools coming soon!!")

        self.other_text.configure(state="disabled")

        self.b64en_button = customtkinter.CTkButton(self.other_frame, text="Base64-Encode", border_width=1, border_color="white", fg_color="grey16", command=self.base64_enc)
        self.b64de_button = customtkinter.CTkButton(self.other_frame, text="Base64-Decode", border_width=1, border_color="white", fg_color="grey16", command=self.base64_dec)


        # Place the boxes in a grid
        self.b64en_button.place(relx=0.56, rely=0.5, anchor='w')
        self.b64de_button.place(relx=0.43, rely=0.5, anchor='e')

    def base64_enc(self):
        self.base64_enc_win = customtkinter.CTkToplevel(self)
        self.base64_enc_win.geometry("450x330")
        self.base64_enc_win.resizable(False, False)
        self.base64_enc_win.title("Encoder")

        self.base64_enc_frame = customtkinter.CTkFrame(self.base64_enc_win)
        self.base64_enc_frame.pack(anchor=N, fill=BOTH, expand=True, side=LEFT )
        self.base64_enc_frame.configure(border_width=1, border_color="white")

        self.base64_enc_label = customtkinter.CTkLabel(self.base64_enc_frame, text="Insert text you want to encode below", width=60, height=20, font=("Railway", 17))
        self.base64_enc_label.place(relx=0.5, rely=0.10, anchor='center')

        self.base64_tbox = customtkinter.CTkTextbox(self.base64_enc_frame, width=300, height=150, state="normal")
        self.base64_tbox.place(relx=0.5, rely=0.41, anchor='center')

        self.b64_go_button = customtkinter.CTkButton(self.base64_enc_frame, text="Encode!", border_width=1, border_color="white", fg_color="grey16", command=self.base64_enc_proc)
        self.b64_go_button.place(relx=0.5, rely=0.85, anchor='center')

    def base64_enc_proc(self):
        self.base64_enc_proc_win = customtkinter.CTkToplevel(self)
        self.base64_enc_proc_win.geometry("200x200")
        self.base64_enc_proc_win.resizable(False, False)
        self.base64_enc_proc_win.title("Results")

        self.b64text = self.base64_tbox.get("0.0", "end")

        self.b64encoded_text = base64.b64encode(self.b64text.encode('utf-8'))
        
        self.b64_text_tbox = customtkinter.CTkTextbox(self.base64_enc_proc_win, width=130, height=100, state="normal")
        self.b64_text_tbox.place(relx=0.5, rely=0.34, anchor='center')
        self.b64_text_tbox.insert("0.0", self.b64encoded_text)

        self.base64_enc_proc_but = customtkinter.CTkButton(self.base64_enc_proc_win, text="Close", border_width=1, border_color="white", fg_color="grey16", command=self.base64_enc_close)
        self.base64_enc_proc_but.place(relx=0.5, rely=0.75, anchor='center')

    def base64_enc_close(self):
        self.base64_enc_win.destroy()
        self.base64_enc_proc_win.destroy()

    def base64_dec(self):
        self.base64_dec_win = customtkinter.CTkToplevel(self)
        self.base64_dec_win.geometry("450x330")
        self.base64_dec_win.resizable(False, False)
        self.base64_dec_win.title("Decoder")

        self.base64_dec_frame = customtkinter.CTkFrame(self.base64_dec_win)
        self.base64_dec_frame.pack(anchor=N, fill=BOTH, expand=True, side=LEFT )
        self.base64_dec_frame.configure(border_width=1, border_color="white")

        self.base64_dec_label = customtkinter.CTkLabel(self.base64_dec_frame, text="Insert Base64 encoded string below", width=60, height=20, font=("Railway", 17))
        self.base64_dec_label.place(relx=0.5, rely=0.10, anchor='center')

        self.base64_dec_tbox = customtkinter.CTkTextbox(self.base64_dec_frame, width=300, height=150, state="normal")
        self.base64_dec_tbox.place(relx=0.5, rely=0.41, anchor='center')

        self.b64_dec_button = customtkinter.CTkButton(self.base64_dec_frame, text="Decode!", border_width=1, border_color="white", fg_color="grey16", command=self.base64_dec_proc)
        self.b64_dec_button.place(relx=0.5, rely=0.85, anchor='center')

    def base64_dec_proc(self):
        self.base64_dec_proc_win = customtkinter.CTkToplevel(self)
        self.base64_dec_proc_win.geometry("200x200")
        self.base64_dec_proc_win.resizable(False, False)
        self.base64_dec_proc_win.title("Results")

        self.b64dectext = self.base64_dec_tbox.get("0.0", "end")

        self.b64decoded_text = base64.b64decode(self.b64dectext)
        
        self.b64_text_tbox = customtkinter.CTkTextbox(self.base64_dec_proc_win, width=130, height=100, state="normal")
        self.b64_text_tbox.place(relx=0.5, rely=0.34, anchor='center')
        self.b64_text_tbox.insert("0.0", self.b64decoded_text)

        self.base64_dec_proc_but = customtkinter.CTkButton(self.base64_dec_proc_win, text="Close", border_width=1, border_color="white", fg_color="grey16", command=self.base64_dec_close)
        self.base64_dec_proc_but.place(relx=0.5, rely=0.75, anchor='center')

    def base64_dec_close(self):
        self.base64_dec_win.destroy()
        self.base64_dec_proc_win.destroy()

    def self_decrypt_gui(self):
        self.sedecrypting_proc_win = customtkinter.CTkToplevel(self)
        self.sedecrypting_proc_win.geometry("250x200")
        self.sedecrypting_proc_win.resizable(False, False)
        self.sedecrypting_proc_win.title("Save")

        self.sedecrypting_proc_frame = customtkinter.CTkFrame(self.sedecrypting_proc_win)
        self.sedecrypting_proc_frame.pack(anchor=N, fill=BOTH, expand=True, side=LEFT )
        self.sedecrypting_proc_frame.configure(border_width=1, border_color="white")

        self.sedecrypting_proc_label = customtkinter.CTkLabel(self.sedecrypting_proc_frame, text="Choose a location to save the file!", font=("Railway", 15))
        self.sedecrypting_proc_label.place(relx=0.5, rely=0.15, anchor='center')

        self.sedecrypting_proc_but = customtkinter.CTkButton(self.sedecrypting_proc_frame, text="Savepath", border_width=1, border_color="white", fg_color="transparent", hover=False, command=self.self_decrypting_pre)
        self.sedecrypting_proc_but.place(relx=0.5, rely=0.5, anchor='center')

        self.sedecrypting_proc_go_but = customtkinter.CTkButton(self.sedecrypting_proc_frame, text="Decrypt!", border_width=1, border_color="white", fg_color="DodgerBlue", command=self.self_decrypt_process)
        self.sedecrypting_proc_go_but.place(relx=0.5, rely=0.85, anchor='center')

    def self_decrypting_pre(self):

        self.sedecrypt_save = filedialog.askdirectory()

        self.sedecrypt_save_loc = os.path.abspath(self.sedecrypt_save)

    def self_decrypt_process(self):
        
        self.sedecrypting_proc_win.destroy()

        current_file = os.path.abspath(__file__)
        current_dir = os.path.dirname(current_file)
        file_path_var = os.path.join(current_dir, "var.txt")

        os.path.join(current_dir, "var.txt")

        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=8))

        kek = "\\"
        
        mod_path = self.sedecrypt_save_loc + kek + random_string + ".txt"

        try:
            with open(file_path_var, "w") as file:
                file.write(mod_path)
                file.close()
        except Exception as e:
            print("An error occurred while writing to var.txt: ", e)

        time.sleep(1)

        current_file = os.path.abspath(__file__)
        current_dir = os.path.dirname(current_file)
        file_path_test = os.path.join(current_dir, "sd.py")

        process = subprocess.Popen(['python', file_path_test])

        process.wait()

    def decrypting_pre(self):
        
        self.decrypting_win = customtkinter.CTkToplevel(self)
        self.decrypting_win.geometry("520x300")
        self.decrypting_win.resizable(False, False)
        self.decrypting_win.title("Decrypter")

        self.decrypting_frame = customtkinter.CTkFrame(self.decrypting_win)
        self.decrypting_frame.pack(anchor=N, fill=BOTH, expand=True, side=LEFT )
        self.decrypting_frame.configure(border_width=1, border_color="white")

        self.decrypting_label = customtkinter.CTkLabel(self.decrypting_frame, text="Choose the 'key' and 'encrypted' file to begin!", font=("Railway", 18))
        self.decrypting_label.place(relx=0.5, rely=0.12, anchor='center')

        self.decrypting_keyfile_but = customtkinter.CTkButton(self.decrypting_frame, text="Keyfile", border_width=1, border_color="white", fg_color="grey16", hover=False, command=self.getPathKey)
        self.decrypting_keyfile_but.place(relx=0.295, rely=0.5, anchor='center')

        self.decrypting_encrypfile_but = customtkinter.CTkButton(self.decrypting_frame, text="Encrypted-File", border_width=1, border_color="white", fg_color="grey16", hover=False, command=self.getPathEnc)
        self.decrypting_encrypfile_but.place(relx=0.71, rely=0.5, anchor='center')

        self.decrypting_go_but = customtkinter.CTkButton(self.decrypting_frame, text="Go!", border_width=1, border_color="white", fg_color="grey16", command=self.decrypting_process)
        self.decrypting_go_but.place(relx=0.5, rely=0.86, anchor='center')
        
    def getPathKey(self):
        self.keyfile_loc = filedialog.askopenfile(mode='r', filetypes=[('All', '*')])

        if self.keyfile_loc:
            self.keyfile_path_r = os.path.abspath(self.keyfile_loc.name)
            print(self.keyfile_path_r)

    def getPathEnc(self):
        self.encrypfile_loc = filedialog.askopenfile(mode='r', filetypes=[('All', '*')])

        if self.encrypfile_loc:
            self.encryptfile_path_r = os.path.abspath(self.encrypfile_loc.name)
            print(self.encryptfile_path_r)

    def decrypting_process(self):
        self.decrypting_win.destroy()

        self.decrypting_proc_win = customtkinter.CTkToplevel(self)
        self.decrypting_proc_win.geometry("250x200")
        self.decrypting_proc_win.resizable(False, False)
        self.decrypting_proc_win.title("Save")

        self.decrypting_proc_frame = customtkinter.CTkFrame(self.decrypting_proc_win)
        self.decrypting_proc_frame.pack(anchor=N, fill=BOTH, expand=True, side=LEFT )
        self.decrypting_proc_frame.configure(border_width=1, border_color="white")

        self.decrypting_proc_label = customtkinter.CTkLabel(self.decrypting_proc_frame, text="Choose a location to save the file!", font=("Railway", 15))
        self.decrypting_proc_label.place(relx=0.5, rely=0.15, anchor='center')

        self.decrypting_proc_but = customtkinter.CTkButton(self.decrypting_proc_frame, text="Savepath", border_width=1, border_color="white", fg_color="transparent", hover=False, command=self.get_savepath_decr)
        self.decrypting_proc_but.place(relx=0.5, rely=0.5, anchor='center')

        self.decrypting_proc_go_but = customtkinter.CTkButton(self.decrypting_proc_frame, text="Decrypt!", border_width=1, border_color="white", fg_color="DodgerBlue", command=self.savepath_decrypting_proc)
        self.decrypting_proc_go_but.place(relx=0.5, rely=0.85, anchor='center')

    def get_savepath_decr(self):
        self.decryp_folder = filedialog.askdirectory()

        print(self.decryp_folder)

    def savepath_decrypting_proc(self):
        
        self.decrypting_proc_win.destroy()

        if self.decryp_folder:
            self.decrypt_folder_path = self.decryp_folder
        
        current_file = os.path.abspath(__file__)
        current_dir = os.path.dirname(current_file)
        file_path_var = os.path.join(current_dir, "var.txt")

        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=8))

        kek = "\\"
        
        mod_path1 = self.decrypt_folder_path + kek + random_string + ".txt"

        try:
            with open(file_path_var, "w") as file:
                file.write(f"{self.keyfile_path_r}\n")
                file.write(f"{self.encryptfile_path_r}\n")
                file.write(f"{mod_path1}")
        except Exception as e:
            print("An error occurred while writing to var.txt: ", e)
        
        file.close()

        time.sleep(2)

        current_file = os.path.abspath(__file__)
        current_dir = os.path.dirname(current_file)
        file_path_test = os.path.join(current_dir, "d.py")

        process = subprocess.Popen(['python', file_path_test])

        process.wait()

    def exit(self):
        sys.exit()

if __name__ == "__main__":
    start = MainScreen()
    start.mainloop()