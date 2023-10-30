from tkinter import filedialog as fd
import pyautogui
import os
import CTkMessagebox as messagebox

class File_Tool:
    def open_file(self):
        super().__init__()
        try:
            self.loc_file=fd.askopenfilename(initialdir=os.getcwd(),  
                                                title='Select Image File', 
                                                filetypes=(("PNG File", "*.png"), 
                                                            ("JPG File", "*.jpg"), 
                                                            ("JPEG Fİle", "*.jpeg"), ("All Files", "*.*")))

        except:
            messagebox.showwarning("warning", "You didn't pick an image! Please choose an image")
        return self.loc_file

class Get_Info:
        def screen_size(self):
            super().__init__()
            try:
                self.width,self.height=pyautogui.size()
            except:
                messagebox.showwarning("warning","Something went wrong.")
            return self.width,self.height



