import customtkinter as ctg
import CTkMessagebox as ctmb
from PIL import Image
from Project_Tools import * 


from PIL import Image
info=Get_Info()
tl_file=File_Tool()
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
        print(f"{self.widht_size}x{self.height_size}")


        # Frame Configure
        self.frame_main=ctg.CTkFrame(master=self,width=(self.widht_size/4),height=self.height_size-20)
        self.frame_main.grid(row=0,column=0,padx=10,pady=10)

        self.frame_tabview=ctg.CTkFrame(master=self,width=(3*(self.widht_size/4))-60,height=self.height_size-20)
        self.frame_tabview.grid(row=0,column=1,padx=10,pady=10)


        self.tab_view = MyTabView(master=self.frame_tabview,width=(3*(self.widht_size/4))-60,height=self.height_size-40)
        self.tab_view.grid(row=0, column=0, padx=10, pady=10)


class MyTabView(ctg.CTkTabview):
    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)
        self.widht_size,self.height_size=info.screen_size()

        #Sekme isimleri
        self.name_tab_image="IMAGE HIDE TEXT"
        self.name_tab_voice="VOİCE HIDE TEXT"

        #Dosyaların adresleri
        self.loc_addimage="Project_Images\\add_image.png"
        self.loc_addvoice="Project_Images\\add_voice.png"
        self.loc_download="Project_Images\\download.png"
        self.loc_imageframe="Project_Images\\image_frame.png"
        self.loc_playvoice="Project_Images\\play_voice.png"
        self.loc_save="Project_Images\\save.png"
        self.loc_stopvoice="Project_Images\\stop_voice.png"
        self.loc_voice="Project_Images\\voice.png"


        #Sekme Ekleme
        self.add(self.name_tab_image)
        self.add(self.name_tab_voice)

        #Button resimleri butim= Button İmage
        self.butim_addimage=ctg.CTkImage(Image.open(self.loc_addimage),size=(50,50))
        self.butim_addvoice=ctg.CTkImage(Image.open(self.loc_addvoice),size=(50,50))
        self.butim_download=ctg.CTkImage(Image.open(self.loc_download),size=(50,50))
        self.butim_imageframe=ctg.CTkImage(Image.open(self.loc_imageframe),size=((3*(self.widht_size/16)-20),self.height_size/2-40))
        self.butim_playvoice=ctg.CTkImage(Image.open(self.loc_playvoice),size=(50,50))
        self.butim_save=ctg.CTkImage(Image.open(self.loc_save),size=(50,50))
        self.butim_stopvoice=ctg.CTkImage(Image.open(self.loc_stopvoice),size=(50,50))
        self.butim_voice=ctg.CTkImage(Image.open(self.loc_voice),size=(50,50))


        #RESİM İÇİNE METİN GİZLEME ALANI İÇİN 
        #frameler

        self.frame_tabimage=ctg.CTkFrame(master=self.tab(self.name_tab_image),width=(3*(self.widht_size/16)),height=self.height_size/2-20)
        self.frame_tabimage.grid(row=1,column=0,padx=10,pady=10)

        self.frame_button_tabimage=ctg.CTkFrame(master=self.tab(self.name_tab_image),width=120,height=self.height_size/2-20)
        self.frame_button_tabimage.grid(row=1,column=1,padx=10,pady=10)

        self.frame_tabtextbox=ctg.CTkFrame(master=self.tab(self.name_tab_image),width=(3*(self.widht_size/16)),height=self.height_size/2-20)
        self.frame_tabtextbox.grid(row=1,column=2,padx=10,pady=10)

        self.frame_button_tabtextbox=ctg.CTkFrame(master=self.tab(self.name_tab_image),width=120,height=self.height_size/2-20)
        self.frame_button_tabtextbox.grid(row=1,column=3,padx=10,pady=10)


        #Eventler
        def event_button_open_image():
            self.loc_file_image=tl_file.open_file()
            self.open_image=ctg.CTkImage(Image.open(self.loc_file_image),size=(((3*(self.widht_size/16)-40),self.height_size/2-60)))
            self.ilabel_frimage.configure(image=self.open_image)

        #Buttonlar
        self.button_open_image=ctg.CTkButton(
            master=self.frame_button_tabimage,
            image=self.butim_addimage,
            width=50,
            height=50,
            text=None,
            command=event_button_open_image,
            fg_color="transparent"
        )
        self.button_open_image.grid(row=0,column=0,padx=10,pady=10)
        

        #Resim Alanı
        self.ilabel_frimage=ctg.CTkLabel(master=self.frame_tabimage,
        width=(3*(self.widht_size/16))-20,
        height=self.height_size/2-40,
        text="",
        image=self.butim_imageframe)
        self.ilabel_frimage.grid(row=0,column=0,padx=10,pady=10) 
       


app = App()
app.mainloop()