import os
import CTkMessagebox as messagebox
from PIL import Image

import pyautogui
from tkinter import filedialog as fd
class File_Tool:
    count=1
    def open_file(self):
        super().__init__()
        try:
            self.loc_file=fd.askopenfilename(initialdir=os.getcwd(),  
                                                title='Open Image File', 
                                                filetypes=(("PNG File", "*.png"), 
                                                            ("JPG File", "*.jpg"), 
                                                            ("JPEG Fİle", "*.jpeg"), ("All Files", "*.*")))
        

        except:
            messagebox.showwarning("warning", "You didn't pick an image! Please choose an image")
        return self.loc_file

    def saveData(self,save_file):
        super().__init__()
        loc_save=fd.asksaveasfilename(defaultextension=".png",initialdir=os.getcwd(),  
                                                title='Save Image File', 
                                                filetypes=(("PNG File", "*.png"), 
                                                            ("JPG File", "*.jpg"), 
                                                            ("JPEG Fİle", "*.jpeg"), ("All Files", "*.*")))
        if loc_save:
            save_file.save(loc_save)

        return loc_save

    def bos():
        print("")



class Get_Info:
        def screen_size(self):
            super().__init__()
            try:
                self.width,self.height=pyautogui.size()
            except:
                messagebox.showwarning("warning","Something went wrong.")
            return self.width,self.height

from stegano import lsb
class Steganografy():

    def hideData(self,filename,message):
        super().__init__()
        return lsb.hide(str(filename), message,encoding="UTF-8",auto_convert_rgb=True) # lsb.hide() fonksiyonu, mesajı resim dosyasına gizler. Mesaj gizlenen resim secret değişkeninde atılır


    def showData(self,filename):
        super().__init__()
        return lsb.reveal(filename,encoding="UTF-8") # lsb.reveal() fonksiyonu, gizlenmiş mesajı resim dosyasından çıkarır.

        
from cryptography.fernet import Fernet        
class Cryptograph():
    def get_key(self):
        super().__init__()
        return Fernet.generate_key()
        
    def transform_bytes(self,str):#key ve şifrelenmiş yapının bayt formatında olması lazım
        super().__init__()
        return bytes(str,'utf-8')    

    def encrypt_msg(self,msg,key):
        super().__init__()
        fernet=Fernet(key)
        return fernet.encrypt(msg)

    def decrypt_msg(self,msg,key):
        super().__init__()
        fernet=Fernet(key)
        return fernet.decrypt(msg)


