import customtkinter as ctg
from tkinter import messagebox
from PIL import Image

from OSE_Image_Hide import *
i_lsb=image_Lsb()

from OSE_Voice_Hide import *
v_lsb=voice_Lsb

from OSE_File import * 
info=Get_Info()
fd=File_Tool()

from OSE_Cry import *
cry=cryptography_Fernet()

from OSE_Media_Player import *
mdp=player()

from OSE_Voice_Convert import *
convert=Convert_Media()

from OSE_Tool import *
name_detect=Name_Detect()
global cost

class App(ctg.CTk):

    def __init__(self):
        super().__init__()
        #Bilgisayarın ekran boyutu bilgisini alıyor

        def event_link(link):
            return webbrowser.open(link, new=2)
        
        self.widht_size,self.height_size=info.screen_size()

        #ekran kaplama alanını ayarlamak için (400 önerilir)
        self.widht_size-=self.widht_size/2
        self.height_size-=self.height_size/2


        #App configure
        self.title("Project OSE")
        self.iconbitmap("Project_Images\\logo.ico")
        self.geometry(f"{self.widht_size}x{self.height_size}")
        self.resizable(width=False,height=False)


        # Frame Configure
        self.frame_main=ctg.CTkFrame(master=self,width=(self.widht_size/4),height=self.height_size-20)
        self.frame_main.grid(row=0,column=0,padx=10,pady=10)

        self.frame_tabview=ctg.CTkFrame(master=self,width=(3*(self.widht_size/4))-60,height=self.height_size-20)
        self.frame_tabview.grid(row=0,column=1,padx=10,pady=10)


        self.tab_view = MyTabView(master=self.frame_tabview,width=(3*(self.widht_size/4))-60,height=self.height_size-40)
        self.tab_view.grid(row=0, column=0, padx=10, pady=10)

        self.frame_name0=ctg.CTkFrame(master=self.frame_main,width=(self.widht_size/4)-20,height=60)
        self.frame_name0.grid(row=1,column=0,padx=10,pady=10)

        self.frame_name1=ctg.CTkFrame(master=self.frame_main,width=(self.widht_size/4)-20,height=60)
        self.frame_name1.grid(row=2,column=0,padx=10,pady=10)

        self.frame_name2=ctg.CTkFrame(master=self.frame_main,width=(self.widht_size/4)-20,height=60)
        self.frame_name2.grid(row=3,column=0,padx=10,pady=10)

        #Logo ekleme ve resimler
        self.loc_main_logo="Project_Images\\logo.png"
        self.image_logo=ctg.CTkImage(Image.open(self.loc_main_logo),size=((self.widht_size/4),(self.height_size-20)/4))
        self.ilabel_image_logo=ctg.CTkLabel(master=self.frame_main,
        text="",
        image=self.image_logo,
        width=(self.widht_size/4),
        height=((self.height_size-20)/4))
        self.ilabel_image_logo.grid(row=0,column=0,padx=10,pady=10)

        self.loc_github="Project_Images\\github.png"
        self.loc_linkedin="Project_Images\\linkedin.png"
        self.image_github=ctg.CTkImage(Image.open(self.loc_github),size=(50,50))
        self.image_linkedin=ctg.CTkImage(Image.open(self.loc_linkedin),size=(50,50))

        #Button ve labelllar
        self.label_name0=ctg.CTkLabel(master=self.frame_name1,text="Sinan Uyğun",width=20,height=100,font=("Open Sans",21),text_color="#0174BE")
        self.label_name0.grid(row=0,column=0,padx=18,pady=10)

        self.label_name1=ctg.CTkLabel(master=self.frame_name0,text="Onur Karakaya",width=20,height=100,font=("Open Sans",21),text_color="#0174BE")
        self.label_name1.grid(row=0,column=0,padx=10,pady=10)

        self.label_name2=ctg.CTkLabel(master=self.frame_name2,text="Emre Yörük",width=20,height=100,font=("Open Sans",21),text_color="#0174BE")
        self.label_name2.grid(row=0,column=0,padx=22,pady=10)
        #eventler

        
        def event_lin_name0():
            info.open_link("https://linkedin.com/in/sinanuygun/")
        def event_lin_name1():
            info.open_link("https://linkedin.com/in/onur-karakaya-815517228/")
        def event_lin_name2():
            info.open_link("https://linkedin.com/in/emreyorukk/")
        def event_git_name1():
            info.open_link("https://github.com/OnuurKrky")
        def event_git_name2():
            info.open_link("https://github.com/emreyoruk0")
        def event_git_name0():
            info.open_link("https://github.com/YELBEGEN7")
        
        #butonlar
        self.button_git_name0=ctg.CTkButton(
            master=self.frame_name1,
            width=50,
            height=50,
            image=self.image_github,
            text="",
            command=event_git_name0
        )        
        self.button_git_name0.grid(row=0,column=1,padx=10,pady=10)

        self.button_lin_name0=ctg.CTkButton(
            master=self.frame_name1,
            width=50,
            height=50,
            image=self.image_linkedin,
            text="",
            command=event_lin_name0
        )        
        self.button_lin_name0.grid(row=0,column=2,padx=10,pady=10)

 

        self.button_git_name1=ctg.CTkButton(
            master=self.frame_name0,
            width=50,
            height=50,
            image=self.image_github,
            text="",
            command=event_git_name1
        )        
        self.button_git_name1.grid(row=0,column=1,padx=10,pady=10)

        self.button_lin_name1=ctg.CTkButton(
            master=self.frame_name0,
            width=50,
            height=50,
            image=self.image_linkedin,
            text="",
            command=event_lin_name1
        )        
        self.button_lin_name1.grid(row=0,column=2,padx=10,pady=10)



        self.button_git_name1=ctg.CTkButton(
            master=self.frame_name2,
            width=50,
            height=50,
            image=self.image_github,
            text="",
            command=event_git_name2
        )        
        self.button_git_name1.grid(row=0,column=1,padx=10,pady=10)

        self.button_lin_name2=ctg.CTkButton(
            master=self.frame_name2,
            width=50,
            height=50,
            image=self.image_linkedin,
            text="",
            command=event_lin_name2
        )        
        self.button_lin_name2.grid(row=0,column=2,padx=10,pady=10)


     


class MyTabView(ctg.CTkTabview):
    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)
        self.widht_size,self.height_size=info.screen_size()

        #Sekme isimleri
        self.name_tab_image="IMAGE HIDE TEXT"
        self.name_tab_voice="VOİCE HIDE TEXT"

        #Dosyaların adresleri
        self.loc_imagetab_addimage="Project_Images\\add_image.png"
        self.loc_imagetab_imageframe="Project_Images\\image_frame.png"
        self.loc_imagetab_saveimage="Project_Images\\save_image.png"
        self.loc_general_key="Project_Images\\key.png"
        self.loc_general_clean="Project_Images\\clean.png"
        self.loc_general_nonshow="Project_Images\\nonshow.png"
        self.loc_general_show="Project_Images\\show.png"
        self.loc_general_savebutton="Project_Images\\savebutton.png"

        #Sekme Ekleme
        self.add(self.name_tab_image)
        self.add(self.name_tab_voice)

        #Button resimleri butim= Button İmage
        self.butim_imagetab_saveimage=ctg.CTkImage(Image.open(self.loc_imagetab_saveimage),size=(50,50))
        self.butim_imagetab_addimage=ctg.CTkImage(Image.open(self.loc_imagetab_addimage),size=(40,40))
        self.butim_imagetab_imageframe=ctg.CTkImage(Image.open(self.loc_imagetab_imageframe),size=((4*(self.widht_size/16)-40),self.height_size/2-60))
        self.buttim_general_key=ctg.CTkImage(Image.open(self.loc_general_key),size=(40,40))
        self.butim_general_clean=ctg.CTkImage(Image.open(self.loc_general_clean),size=(35,35))
        self.butim_general_nonshow=ctg.CTkImage(Image.open(self.loc_general_nonshow),size=(40,40))
        self.butim_general_show=ctg.CTkImage(Image.open(self.loc_general_show),size=(40,40))
        self.butim_general_savebutton=ctg.CTkImage(Image.open(self.loc_general_savebutton),size=(35,35))

        #RESİM İÇİNE METİN GİZLEME ALANI İÇİN 
        #frameler

        self.frame_tabimage=ctg.CTkFrame(master=self.tab(self.name_tab_image),width=(4*(self.widht_size/16)),height=self.height_size/2-40)
        self.frame_tabimage.grid(row=1,column=0,padx=10,pady=10)

        self.frame_button_tabimage=ctg.CTkFrame(master=self.tab(self.name_tab_image),width=(4*(self.widht_size/16)),height=70)
        self.frame_button_tabimage.grid(row=2,column=0,padx=5,pady=5)

        self.frame_tabtextbox=ctg.CTkFrame(master=self.tab(self.name_tab_image),width=(4*(self.widht_size/16)),height=self.height_size/2-40)
        self.frame_tabtextbox.grid(row=1,column=1,padx=5,pady=5)

        self.frame_button_tabtextbox=ctg.CTkFrame(master=self.tab(self.name_tab_image),width=(4*(self.widht_size/16)),height=70)
        self.frame_button_tabtextbox.grid(row=2,column=1,padx=5,pady=5)

        self.frame_text_key=ctg.CTkFrame(master=self.frame_tabtextbox,width=(4*(self.widht_size/16))-20,height=70)
        self.frame_text_key.grid(row=1,column=0,padx=5,pady=5)

        #Textbox 
        self.entry=ctg.CTkTextbox(master=self.frame_tabtextbox,width=(4*(self.widht_size/16))-20,height=(self.height_size/2-120),text_color="#A5D7E8",font=("Open Sans",16))
        self.entry.grid(row=0,column=0,padx=5,pady=5)

        #Entry 
        self.entry_key=ctg.CTkEntry(master=self.frame_text_key,placeholder_text="key",width=((4*(self.widht_size/16))-20)/2,height=50,text_color="#A5D7E8",font=("Open Sans",16))
        self.entry_key.grid(row=0,column=0,padx=5,pady=5)

    

        #Resim Alanı
        self.ilabel_mainimage=ctg.CTkLabel(master=self.frame_tabimage,
        width=(4*(self.widht_size/16))-20,
        height=self.height_size/2-60,
        text="",
        image=self.butim_imagetab_imageframe)
        self.ilabel_mainimage.grid(row=0,column=0,padx=10,pady=10) 

        #fonksiyonlar
        def image_configure(image_pil):
            self.config_image=ctg.CTkImage(image_pil,size=((4*(self.widht_size/16)-40),self.height_size/2-60))
            return self.config_image

            

        #Eventler
        def event_button_open_image():
            self.loc_file_image=fd.image_open_file()
            self.image_tool=Image.open(self.loc_file_image)
            self.open_image=ctg.CTkImage(Image.open(self.loc_file_image),size=((4*(self.widht_size/16)-40),(self.height_size/2-60)))
            self.ilabel_mainimage.configure(image=self.open_image)



        def event_button_clear_text():
            self.entry.delete("0.0","end")
            self.entry_key.delete(0,'end')


        def event_button_hide_text():
            self.key=cry.get_key()
            self.msg_byt=cry.transform_bytes(self.entry.get("0.0","end"))
            self.msg_enc=cry.encrypt_msg(self.msg_byt,self.key)
            self.entry.delete("0.0","end")
            self.entry_key.delete(0,"end")
            self.entry_key.insert(0,self.key.decode('utf-8'))
            self.entry.insert("end",f"{self.msg_enc.decode('utf-8')}")
            self.image_hide=i_lsb.hideData(self.loc_file_image,self.entry.get("0.0","end"))
            self.ilabel_mainimage.configure(image=image_configure(self.image_hide))



        def event_button_show_text():
            self.show_text=i_lsb.showData(self.loc_file_image)
            self.entry.delete("0.0","end")
            self.entry.insert("end",f"{self.show_text}")

        def event_button_unlock_key():
            self.unlock_key=cry.transform_bytes(self.entry_key.get())
            self.unlock_text=cry.transform_bytes(self.entry.get("0.0","end"))
            self.unlock_decrypt=cry.decrypt_msg(self.unlock_text,self.unlock_key)
            self.entry.delete("0.0","end")
            self.entry.insert("end",self.unlock_decrypt.decode("utf-8"))

        def event_button_save_image():
            self.loc_file_image=fd.image_saveData(self.image_hide)
        #Buttonlar
        self.button_open_image=ctg.CTkButton(
            master=self.frame_button_tabimage,
            image=self.butim_imagetab_addimage,
            width=50,
            height=50,
            text="Open",
            text_color="#0174BE",
            font=("Open Sans",16),
            command=event_button_open_image,
            fg_color="#181D31"
        )
        self.button_open_image.grid(row=0,column=0,padx=10,pady=10)
        
        self.button_save_image=ctg.CTkButton(
            master=self.frame_button_tabimage,
            image=self.butim_general_savebutton,
            width=50,
            height=50,
            text="Save Image",
            text_color="#0174BE",
            font=("Open Sans",16),
            command=event_button_save_image,
            fg_color="#181D31"
        )
        self.button_save_image.grid(row=0,column=1,padx=10,pady=10)
        
        self.button_hide_text=ctg.CTkButton(
            master=self.frame_button_tabtextbox,
            image=self.butim_general_nonshow,
            width=50,
            height=50,
            text="Hide Text",
            text_color="#0174BE",
            font=("Open Sans",16),
            command=event_button_hide_text,
            fg_color="#181D31",
        )
        self.button_hide_text.grid(row=0,column=0,padx=10,pady=10)

        self.button_show_text=ctg.CTkButton(
            master=self.frame_button_tabtextbox,
            image=self.butim_general_show,
            width=50,
            height=50,
            text="Show Text",
            text_color="#0174BE",
            font=("Open Sans",16),
            command=event_button_show_text,
            fg_color="#181D31",
        )
        self.button_show_text.grid(row=0,column=1,padx=10,pady=10)

        self.button_clear_text=ctg.CTkButton(
            master=self.frame_button_tabtextbox,
            image=self.butim_general_clean,
            width=50,
            height=50,
            text="Clear Text",
            text_color="#0174BE",
            font=("Open Sans",16),
            command=event_button_clear_text,
            fg_color="#181D31",
        )
        self.button_clear_text.grid(row=0,column=2,padx=10,pady=10)


        self.button_unlock_key=ctg.CTkButton(
            master=self.frame_text_key,
            image=self.buttim_general_key,
            width=50,
            height=50,
            text="Unlock Text",
            text_color="#0174BE",
            font=("Open Sans",16),
            command=event_button_unlock_key,
            fg_color="#181D31",
        )
        self.button_unlock_key.grid(row=0,column=1,padx=5,pady=5)

       #Voice tab alanı
        self.frame_musicplayer=ctg.CTkFrame(master=self.tab(self.name_tab_voice),width=(4*(self.widht_size/16)),height=self.height_size/2-40)
        self.frame_musicplayer.grid(row=0,column=0,padx=10,pady=10)
        self.frame_musicplayer.pack_propagate(False)

        self.frame_voice_music=ctg.CTkFrame(master=self.frame_musicplayer,width=(4*(self.widht_size/16)),height=self.height_size/2-40)
        self.frame_voice_music.grid(row=0,column=0,padx=10,pady=10)
        self.frame_voice_music.pack_propagate(False)

        self.frame_hidevoice_music=ctg.CTkFrame(master=self.frame_musicplayer,width=(4*(self.widht_size/16)),height=self.height_size/2-40)
        self.frame_hidevoice_music.grid(row=1,column=0,padx=10,pady=10)
        self.frame_hidevoice_music.pack_propagate(False)

        self.frame_voice_button=ctg.CTkFrame(master=self.tab(self.name_tab_voice),width=(4*(self.widht_size/16)),height=self.height_size/2-40)
        self.frame_voice_button.grid(row=1,column=0,padx=10,pady=10)

        self.frame_voice_textbox=ctg.CTkFrame(master=self.tab(self.name_tab_voice),width=(4*(self.widht_size/16)),height=70)
        self.frame_voice_textbox.grid(row=0,column=1,padx=10,pady=10)

        self.frame_voice_textbox_button=ctg.CTkFrame(master=self.tab(self.name_tab_voice),width=(4*(self.widht_size/16)),height=self.height_size/2-40)
        self.frame_voice_textbox_button.grid(row=1,column=1,padx=10,pady=10)

        self.frame_voice_key=ctg.CTkFrame(master=self.frame_voice_textbox,width=(4*(self.widht_size/16)),height=50)
        self.frame_voice_key.grid(row=1,column=0,padx=10,pady=10)
        #voice resim location
        self.loc_voicetab_play="Project_Images\\play_voice.png"
        self.loc_voicetab_stop="Project_Images\\stop_voice.png"
        self.loc_voicetab_pause="Project_Images\\pause_voice.png"
        self.loc_voicetab_resume="Project_Images\\resume_voice.png"
        self.loc_voicetab_addvoice="Project_Images\\add_voice.png"


        #butim= buton image
        self.buttim_voicetab_play=ctg.CTkImage(Image.open(self.loc_voicetab_play),size=(40,40))
        self.buttim_voicetab_pause=ctg.CTkImage(Image.open(self.loc_voicetab_pause),size=(40,40))
        self.buttim_voicetab_stop=ctg.CTkImage(Image.open(self.loc_voicetab_stop),size=(40,40))
        self.buttim_voicetab_resume=ctg.CTkImage(Image.open(self.loc_voicetab_resume),size=(40,40))
        self.buttim_voicetab_addvoice=ctg.CTkImage(Image.open(self.loc_voicetab_addvoice),size=(40,40))
        #buton event
        def event_button_voicetab_play():
            mdp.voice_play(self.loc_voice_file)

        def event_button_voicetab_pause():
            mdp.voice_pause()

        def event_button_voicetab_stop():
            mdp.voice_stop()

        def event_button_voicetab_resume():
            mdp.voice_resume()
        def event_button_hidevoicetab_play():
            mdp.voice_play(self.loc_voice_wav)

        def event_button_hidevoicetab_pause():
            mdp.voice_pause()

        def event_button_hidevoicetab_stop():
            mdp.voice_stop()

        def event_button_hidevoicetab_resume():
            mdp.voice_resume()

        def event_voicetab_open_file():
            self.button_voice_play.configure(state='normal')
            self.button_voice_pause.configure(state='normal')
            self.button_voice_resume.configure(state='normal')
            self.button_voice_stop.configure(state='normal')

            self.loc_voice_file=fd.voice_open_file()
            self.music_name=name_detect.name_check(self.loc_voice_file)
            self.label_musicname1.configure(text=self.music_name)
            self.loc_voice_wav=convert.cnv_mp3_wav(self.loc_voice_file,"wavfile1")
            self.loc_hidedata_wav=self.loc_voice_wav

        def event_voicetab_save_file():
            self.loc_voice_save=fd.voice_save_file(self.song)
            
            self.loc_voice_save_file=fd.voice_save_file()
            self.hide_music_name=name_detect.name_check(self.loc_voice_save_file)
            self.label_musicname.configure(text=self.hide_music_name)

        def event_button_voice_unlock():
            self.voice_unlock_key=cry.transform_bytes(self.voice_entry_key.get())
            self.voice_unlock_text=cry.transform_bytes(self.voice_textbox.get("0.0","end"))
            self.voice_decrypt_text=cry.decrypt_msg(self.voice_unlock_text,self.voice_unlock_key)
            self.voice_textbox.delete("0.0","end")
            self.voice_textbox.insert("end",self.voice_decrypt_text)

        def event_button_voice_hidetext():
            self.button_hidevoice_play.configure(state='normal')
            self.button_hidevoice_pause.configure(state='normal')
            self.button_hidevoice_resume.configure(state='normal')
            self.button_hidevoice_stop.configure(state='normal')

            self.voice_key=cry.get_key()
            self.voice_entry_key.delete(0,"end")
            
            self.voice_byt_msg=cry.transform_bytes(self.voice_textbox.get("0.0","end"))
            self.voice_enc_msg=cry.encrypt_msg(self.voice_byt_msg,self.voice_key)
            self.voice_textbox.delete("0.0","end")
            self.voice_textbox.insert("end",self.voice_enc_msg.decode('utf-8'))

            self.voice_info=len(self.voice_textbox.get("0.0","end"))
            self.voice_entry_key.insert("end",f"{self.voice_key.decode('utf-8')}{self.voice_info}")

            self.loc_hidedata_wav=name_detect.file_name_controller("Project_Tools\\","hidewav1","wav")
            self.hidevoice_patch=v_lsb.hideData(self,self.voice_textbox.get("0.0","end"),self.loc_voice_wav,self.loc_hidedata_wav)
            

        def event_button_voice_showtext():
            self.voice_hit,self.voice_key= name_detect.process_message(self.voice_entry_key.get())
            print("sayı=",self.voice_hit,"\n","metin=",self.voice_key)
            self.hidevoice_msg=v_lsb.showdata(self,self.loc_hidedata_wav,self.voice_hit)
            self.voice_textbox.delete("0.0","end")
            self.voice_textbox.insert("end",self.hidevoice_msg)


        def event_button_voice_cleartext():
            self.voice_textbox.delete("0.0","end")
            self.voice_entry_key.delete(0,'end')

        #voice button
        self.label_musicname1=ctg.CTkLabel(master=self.frame_voice_music,text="Music Name",width=100,height=75,text_color="#0174BE",font=("Open Sans",24))
        self.label_musicname1.grid(row=0,column=0,padx=5,pady=5,sticky='nsew')

        self.label0=ctg.CTkLabel(master=self.frame_voice_music,text="",width=50,height=0)
        self.label0.grid(row=1,column=0,padx=5,pady=5)

        self.label_musicname=ctg.CTkLabel(master=self.frame_hidevoice_music,text="Hide Music Name",width=100,height=75,text_color="#0174BE",font=("Open Sans",24))
        self.label_musicname.grid(row=0,column=0,padx=5,pady=5,sticky='nsew')

        self.label1=ctg.CTkLabel(master=self.frame_hidevoice_music,text="",width=50,height=0,)
        self.label1.grid(row=1,column=0,padx=5,pady=5)

        self.button_voice_play=ctg.CTkButton(
            master=self.frame_voice_music,
            image=self.buttim_voicetab_play,
            width=50,
            height=50,
            text="Play",
            text_color="#0174BE",
            font=("Open Sans",16),
            command=event_button_voicetab_play,
            fg_color="#181D31",
            state='disable'
        )
        self.button_voice_play.grid(row=1,column=1,padx=5,pady=5)

        self.button_voice_pause=ctg.CTkButton(
            master=self.frame_voice_music,
            image=self.buttim_voicetab_pause,
            width=50,
            height=50,
            text="Pause",
            text_color="#0174BE",
            font=("Open Sans",16),
            command=event_button_voicetab_pause,
            fg_color="#181D31",
            state='disable'
        )
        self.button_voice_pause.grid(row=2,column=0,padx=5,pady=5)

        self.button_voice_stop=ctg.CTkButton(
            master=self.frame_voice_music,
            image=self.buttim_voicetab_stop,
            width=50,
            height=50,
            text="Stop",
            text_color="#0174BE",
            font=("Open Sans",16),
            command=event_button_voicetab_stop,
            fg_color="#181D31",
            state='disable'
        )
        self.button_voice_stop.grid(row=2,column=1,padx=5,pady=5)

        self.button_voice_resume=ctg.CTkButton(
            master=self.frame_voice_music,
            image=self.buttim_voicetab_resume,
            width=50,
            height=50,
            text="Resume",
            text_color="#0174BE",
            font=("Open Sans",16),
            command=event_button_voicetab_resume,
            fg_color="#181D31",
            state='disable'
        )
        self.button_voice_resume.grid(row=2,column=2,padx=5,pady=5)

        self.button_hidevoice_play=ctg.CTkButton(
            master=self.frame_hidevoice_music,
            image=self.buttim_voicetab_play,
            width=50,
            height=50,
            text="Play",
            text_color="#0174BE",
            font=("Open Sans",16),
            command=event_button_hidevoicetab_play,
            fg_color="#181D31",
            state="disable"
        )
        self.button_hidevoice_play.grid(row=1,column=1,padx=5,pady=5)

        self.button_hidevoice_pause=ctg.CTkButton(
            master=self.frame_hidevoice_music,
            image=self.buttim_voicetab_pause,
            width=50,
            height=50,
            text="Pause",
            text_color="#0174BE",
            font=("Open Sans",16),
            command=event_button_hidevoicetab_pause,
            fg_color="#181D31",
            state="disable"
        )
        self.button_hidevoice_pause.grid(row=2,column=0,padx=5,pady=5)

        self.button_hidevoice_stop=ctg.CTkButton(
            master=self.frame_hidevoice_music,
            image=self.buttim_voicetab_stop,
            width=50,
            height=50,
            text="Stop",
            text_color="#0174BE",
            font=("Open Sans",16),
            command=event_button_hidevoicetab_stop,
            fg_color="#181D31",
            state="disable"
        )
        self.button_hidevoice_stop.grid(row=2,column=1,padx=5,pady=5)

        self.button_hidevoice_resume=ctg.CTkButton(
            master=self.frame_hidevoice_music,
            image=self.buttim_voicetab_resume,
            width=50,
            height=50,
            text="Resume",
            text_color="#0174BE",
            font=("Open Sans",16),
            command=event_button_hidevoicetab_resume,
            fg_color="#181D31",
            state="disable"
        )
        self.button_hidevoice_resume.grid(row=2,column=2,padx=5,pady=5)

        self.button_voice_openfile=ctg.CTkButton(
            master=self.frame_voice_button,
            image=self.buttim_voicetab_addvoice,
            width=50,
            height=50,
            text="Open Voice",
            text_color="#0174BE",
            font=("Open Sans",16),
            command=event_voicetab_open_file,
            fg_color="#181D31"
        )
        self.button_voice_openfile.grid(row=0,column=0,padx=5,pady=5)  

        self.button_voice_savefile=ctg.CTkButton(
            master=self.frame_voice_button,
            image=self.butim_general_savebutton,
            width=50,
            height=50,
            text="Save Voice",
            text_color="#0174BE",
            font=("Open Sans",16),
            command=event_voicetab_save_file,
            fg_color="#181D31"
        )
        self.button_voice_savefile.grid(row=0,column=1,padx=5,pady=5)  

        #textbox
        self.voice_textbox=ctg.CTkTextbox(master=self.frame_voice_textbox,width=(4*(self.widht_size/16))-20,height=(self.height_size/2-120),text_color="#A5D7E8",font=("Open Sans",16))
        self.voice_textbox.grid(row=0,column=0,padx=5,pady=5)

        #Entry 
        self.voice_entry_key=ctg.CTkEntry(master=self.frame_voice_key,placeholder_text="key",width=((4*(self.widht_size/16))-20)/2,height=50,text_color="#A5D7E8",font=("Open Sans",16))
        self.voice_entry_key.grid(row=1,column=0,padx=5,pady=5)

        self.button_voice_unlock=ctg.CTkButton(
            master=self.frame_voice_key,
            image=self.buttim_general_key,
            width=50,
            height=50,
            text="Unlock Text",
            text_color="#0174BE",
            font=("Open Sans",16),
            command=event_button_voice_unlock,
            fg_color="#181D31",
        )
        self.button_voice_unlock.grid(row=1,column=1,padx=5,pady=5) 


        self.button_voice_hidetext=ctg.CTkButton(
            master=self.frame_voice_textbox_button,
            image=self.butim_general_nonshow,
            width=50,
            height=50,
            text="Hide Text",
            text_color="#0174BE",
            font=("Open Sans",16),
            command=event_button_voice_hidetext,
            fg_color="#181D31",
        )
        self.button_voice_hidetext.grid(row=0,column=0,padx=5,pady=5)  

        self.button_voice_showtext=ctg.CTkButton(
            master=self.frame_voice_textbox_button,
            image=self.butim_general_show,
            width=50,
            height=50,
            text="Show Text",
            text_color="#0174BE",
            font=("Open Sans",16),
            command=event_button_voice_showtext,
            fg_color="#181D31",
        )
        self.button_voice_showtext.grid(row=0,column=1,padx=5,pady=5)  

        self.button_voice_cleartext=ctg.CTkButton(
            master=self.frame_voice_textbox_button,
            image=self.butim_general_clean,
            width=50,
            height=50,
            text="Clear Text",
            text_color="#0174BE",
            font=("Open Sans",16),
            command=event_button_voice_cleartext,
            fg_color="#181D31",
        )
        self.button_voice_cleartext.grid(row=0,column=2,padx=5,pady=5)  




app = App()
app.mainloop()
