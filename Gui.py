import customtkinter as ctg
from tkinter import messagebox
from PIL import Image
from Project_Tools import * 



info=Get_Info()
tl_file=File_Tool()
cry=Cryptograph()
stg=Steganografy()
class App(ctg.CTk):
    def __init__(self):
        super().__init__()
        #Bilgisayarın ekran boyutu bilgisini alıyor
        
        self.widht_size,self.height_size=info.screen_size()

        #ekran kaplama alanını ayarlamak için (400 önerilir)
        self.widht_size-=400
        self.height_size-=400


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

        #Logo ekleme
        self.loc_main_logo="Project_Images\\logo.png"
        self.image_logo=ctg.CTkImage(Image.open(self.loc_main_logo),size=((self.widht_size/4),(self.height_size-20)/4))
        self.ilabel_image_logo=ctg.CTkLabel(master=self.frame_main,
        text="",
        image=self.image_logo,
        width=(self.widht_size/4),
        height=((self.height_size-20)/4))
        self.ilabel_image_logo.grid(row=0,column=0,padx=10,pady=10)


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
            self.loc_file_image=tl_file.open_file()
            self.image_tool=Image.open(self.loc_file_image)
            self.open_image=ctg.CTkImage(Image.open(self.loc_file_image),size=((4*(self.widht_size/16)-40),(self.height_size/2-60)))
            self.ilabel_mainimage.configure(image=self.open_image)



        def event_button_clear_text():
            self.entry.delete("0.0","end")

        def event_button_encrypt():
            self.key=cry.get_key()
            self.msg_byt=cry.transform_bytes(self.entry.get("0.0","end"))
            self.msg_enc=cry.encrypt_msg(self.msg_byt,self.key)
            self.entry.delete("0.0","end")
            self.entry_key.delete(0,"end")
            self.entry_key.insert(0,self.key.decode('utf-8'))
            self.entry.insert("end",f"{self.msg_enc.decode('utf-8')}")

        def event_button_hide_text():
            self.key=cry.get_key()
            self.msg_byt=cry.transform_bytes(self.entry.get("0.0","end"))
            self.msg_enc=cry.encrypt_msg(self.msg_byt,self.key)
            self.entry.delete("0.0","end")
            self.entry_key.delete(0,"end")
            self.entry_key.insert(0,self.key.decode('utf-8'))
            self.entry.insert("end",f"{self.msg_enc.decode('utf-8')}")
            self.image_hide=stg.hideData(self.loc_file_image,self.entry.get("0.0","end"))
            self.ilabel_mainimage.configure(image=image_configure(self.image_hide))



        def event_button_show_text():
            self.show_text=stg.showData(self.loc_file_image)
            self.entry.delete("0.0","end")
            self.entry.insert("end",f"{self.show_text}")

        def event_button_unlock_key():
            self.unlock_key=cry.transform_bytes(self.entry_key.get())
            self.unlock_text=cry.transform_bytes(self.entry.get("0.0","end"))
            self.unlock_decrypt=cry.decrypt_msg(self.unlock_text,self.unlock_key)
            self.entry.delete("0.0","end")
            self.entry.insert("end",self.unlock_decrypt.decode("utf-8"))

        def event_button_save_image():
            self.loc_file_image=tl_file.saveData(self.image_hide)
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

       


app = App()
app.mainloop()