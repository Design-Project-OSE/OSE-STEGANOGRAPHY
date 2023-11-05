import os
import CTkMessagebox as messagebox
from PIL import Image
import webbrowser
import pyautogui
from tkinter import filedialog as fd
from pygame import mixer
import wave
class File_Tool:
    def open_link(self,link):
        super().__init__()
        webbrowser.open(link, new=2)
    count=1
    def open_file(self):
        super().__init__()

        self.loc_file=fd.askopenfilename(initialdir=os.getcwd(),  
                                            title='Open Image File', 
                                            filetypes=(("PNG File", "*.png"), 
                                                        ("JPG File", "*.jpg"), 
                                                        ("JPEG Fİle", "*.jpeg"), ("All Files", "*.*")))
        


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

class Voice_Hide():
    def voice_open_file(self):#Dosya açma fonksiyonu return ile açılan dosyanın konumunu geri döndürmeniz gerekiyor mp3,wav formatlarını desteklesin
        return 

    def voice_save_file(self):#Dosyayu kaydetme fonksiyonu return ile dosya konumu geri döndirmeniz gerekiyor

        return 
    
    def voice_play(self):#Müzik Play butonu ile çalışacak fonksiyon
        return

    def voice_stop(self):#Müzik Stop butonu ile çalışacak fonksiyon
        return

    def voice_pause(self):#Müzik Pause ile çalışacak fonksiyon
        return

    def voice_resume(self):#Müzik Resume butonu ile çalışacak fonksiyon
        return

    def voice_hide(self,music_loc,message):#Müziğin içine bilginin gizlendiği fonksiyon music_loc=müziğin konumu ve message= gizlenecek mesajı arayüzden iletecem bu tuşa bastıktan sonra save butonuna tıklanması lazım
        return 

    def voice_show(self):#gizlenen mesajı açığa çıkaran fonksiyon
        return 
