import os
import CTkMessagebox as messagebox
from PIL import Image
import webbrowser
import pyautogui
from tkinter import filedialog as fd
import wave
from pydub import AudioSegment
from pygame import mixer
import re

class File_Tool:
    def open_link(self,link):
        webbrowser.open(link, new=2)
    count=1
    def open_file(self):

        self.loc_file=fd.askopenfilename(initialdir=os.getcwd(),  
                                            title='Open Image File', 
                                            filetypes=(("PNG File", "*.png"), 
                                                        ("JPG File", "*.jpg"), 
                                                        ("JPEG Fİle", "*.jpeg"), ("All Files", "*.*")))
        


        return self.loc_file

    def saveData(self,save_file):
        loc_save=fd.asksaveasfilename(defaultextension=".png",initialdir=os.getcwd(),  
                                                title='Save Image File', 
                                                filetypes=(("PNG File", "*.png"), 
                                                            ("JPG File", "*.jpg"), 
                                                            ("JPEG Fİle", "*.jpeg"), ("All Files", "*.*")))
        if loc_save:
            save_file.save(loc_save)

        return loc_save



class Get_Info:
        def screen_size(self):
            try:
                self.width,self.height=pyautogui.size()
            except:
                messagebox.showwarning("warning","Something went wrong.")
            return self.width,self.height

from stegano import lsb
class Steganografy():

    def hideData(self,filename,message):
        return lsb.hide(str(filename), message,encoding="UTF-8",auto_convert_rgb=True) # lsb.hide() fonksiyonu, mesajı resim dosyasına gizler. Mesaj gizlenen resim secret değişkeninde atılır


    def showData(self,filename):
        return lsb.reveal(filename,encoding="UTF-8") # lsb.reveal() fonksiyonu, gizlenmiş mesajı resim dosyasından çıkarır.

        
from cryptography.fernet import Fernet        
class Cryptograph():
    def get_key(self):
        return Fernet.generate_key()
        
    def transform_bytes(self,str):#key ve şifrelenmiş yapının bayt formatında olması lazım
        return bytes(str,'utf-8')    

    def encrypt_msg(self,msg,key):
        fernet=Fernet(key)
        return fernet.encrypt(msg)

    def decrypt_msg(self,msg,key):
        fernet=Fernet(key)
        return fernet.decrypt(msg)

class Voice_Hide():
    def name_check(self,loc_dir):
        index_start=loc_dir.rfind("/")
        index_final=loc_dir.rfind(".mp3")
        music_name=loc_dir[index_start+1:index_final]
        return music_name

    
    def voice_open_file(self):#Dosya açma fonksiyonu return ile açılan dosyanın konumunu geri döndürmeniz gerekiyor mp3,wav formatlarını desteklesin
        patch=fd.askopenfilename(defaultextension=".mp3",initialdir=os.getcwd(),  
                                                title='Open Voice File', 
                                                filetypes=(("mp3 File", "*.mp3"), 
                                                            ("wav File", "*.wav"), 
                                                             ("All Files", "*.*")))
        return patch

    def voice_save_file(self):#Dosyayu kaydetme fonksiyonu return ile dosya konumu geri döndirmeniz gerekiyor

        return 
    
    def voice_play(self,loc_music):#Müzik Play butonu ile çalışacak fonksiyon
        pygame.mixer.init()
        mixer.music.load(loc_music)
        mixer.music.play()
        return

    def voice_stop(self):#Müzik Stop butonu ile çalışacak fonksiyon
        mixer.music.stop(),
        pygame.quit()
        return

    def voice_pause(self):#Müzik Pause ile çalışacak fonksiyon
        mixer.music.pause()
        return

    def voice_resume(self):#Müzik Resume butonu ile çalışacak fonksiyon
        mixer.music.unpause()
        return

    def voice_hide(self,music_loc,message):#Müziğin içine bilginin gizlendiği fonksiyon music_loc=müziğin konumu ve message= gizlenecek mesajı arayüzden iletecem bu tuşa bastıktan sonra save butonuna tıklanması lazım
        loc_wav=Voice_Hide.voice_wav_convert(music_loc)

    def voice_show(self):#gizlenen mesajı açığa çıkaran fonksiyon
        return 

    def control_file(patch):
        ver=0
        while(os.path.exists(patch)):
            delete_ver=f"{ver}"+".wav"
            patch=patch.replace(delete_ver,'')
            ver=ver+1
            patch=patch+f"{ver}"+".wav"
        return patch

    def voice_wav_convert(voice_file):
        wav_save_file="Project_Voice\\wav_ver_h0.wav"
        wav_save_file=Voice_Hide.control_file(wav_save_file)
        wav_file=AudioSegment.from_mp3(voice_file)
        wav_file.export(wav_save_file,format='.wav')
        return wav_save_file