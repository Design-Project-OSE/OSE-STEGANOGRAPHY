import os
import webbrowser
import pyautogui
from tkinter import filedialog as fd
import wave
import re

class File_Tool:


    def image_open_file(self):

        self.loc_file=fd.askopenfilename(initialdir=os.getcwd(),  
                                            title='Open Image File', 
                                            filetypes=(("PNG File", "*.png"), 
                                                        ("JPG File", "*.jpg"), 
                                                        ("JPEG Fİle", "*.jpeg"), ("All Files", "*.*")))
        


        return self.loc_file

    def image_saveData(self,save_file):
        loc_save=fd.asksaveasfilename(defaultextension=".png",initialdir=os.getcwd(),  
                                                title='Save Image File', 
                                                filetypes=(("PNG File", "*.png"), 
                                                            ("JPG File", "*.jpg"), 
                                                            ("JPEG Fİle", "*.jpeg"), ("All Files", "*.*")))
        if loc_save:
            save_file.save(loc_save)

        return loc_save



    
    def voice_open_file(self):#Dosya açma fonksiyonu return ile açılan dosyanın konumunu geri döndürmeniz gerekiyor mp3,wav formatlarını desteklesin
        patch=fd.askopenfilename(defaultextension=".mp3",initialdir=os.getcwd(),  
                                                title='Open Voice File', 
                                                filetypes=(("mp3 File", "*.mp3"), 
                                                            ("wav File", "*.wav"), 
                                                             ("All Files", "*.*")))
        return patch

    def voice_save_file(self):#Dosyayu kaydetme fonksiyonu return ile dosya konumu geri döndirmeniz gerekiyor
        current_directory=fd.asksaveasfilename(defaultextension=".mp3",initialdir=os.getcwd(),  
                                                title='Save Voice File', 
                                                filetypes=(("mp3 File", "*.mp3"), 
                                                            ("wav File", "*.wav"), 
                                                             ("All Files", "*.*")))
        with wave.open(current_directory, 'wb') as fd:
            fd.setparams(song.getparams())
            fd.writeframes(frame_modified)
            song.close()
        return 


class Get_Info:
        def open_link(self,link):
            webbrowser.open(link, new=2)
        def screen_size(self):
            self.width,self.height=pyautogui.size()
            return self.width,self.height


        


    






