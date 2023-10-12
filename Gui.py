import customtkinter as ctg
from PIL import Image
from tkinter import filedialog as fd
import librosa
import pyautogui



class MyTabView(ctg.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # create tabs
        self.add("Image")
        self.add("Voice")

        #Global Varible
        global select_image_loc
        global select_voice_loc

        def event_button_image_add():
            global select_image_loc
            self.select_image_name=fd.askopenfilename()
            select_image_loc=self.select_image_name
            self.select_image=ctg.CTkImage(Image.open(f"{self.select_image_name}"),size=(100,100))
            self.label_select_image=ctg.CTkLabel(
                master=self.tab("Image")
                ,image=self.select_image
                ,width=100
                ,height=100
                ,text=""
            )
            self.label_select_image.grid(row=1,column=0,padx=20,pady=10)
            print(select_image_loc)

        def event_button_voice_add():
            global select_voice_loc
            self.select_voice_name=fd.askopenfilename()
            select_voice_loc=self.select_voice_name
            # Voice file load
            self.select_voice=librosa.load(self.select_voice_name)

        # add widgets on images tabs
        self.image_add=ctg.CTkImage(Image.open("Project_Images\\SeyfDesigner.png"),size=(50,50))
        self.button_image_add = ctg.CTkButton(
            master=self.tab("Image")
            ,image=self.image_add
            ,text=""
            ,width=50
            ,height=50
            ,command=event_button_image_add
            )
        self.button_image_add.grid(row=0, column=0, padx=20, pady=10)
        # add widgets on voices tabs
        self.image_voice=ctg.CTkImage(Image.open("Project_Images\\afif_fudin.png"),size=(50,50))
        self.button_voice_add=ctg.CTkButton(
            master=self.tab("Voice")
            ,image=self.image_voice
            ,text=""
            ,width=50
            ,height=50
            ,command=event_button_voice_add
        )
        self.button_voice_add.grid(row=0,column=0,padx=20,pady=10)


class App(ctg.CTk):
    def __init__(self):
        super().__init__()

        #Display size 
        widht_size,height_size=pyautogui.size()

        #ekran kaplama alanını ayarlamak için (400 önerilir)
        widht_size-=400
        height_size-=400


        #App configure
        self.title("Project OSE")
        self.iconbitmap("Project_Images\\freepick.ico")
        self.geometry(f"{widht_size}x{height_size}")


        # Frame Configure
        self.frame_main=ctg.CTkFrame(master=self,width=(widht_size/4),height=height_size-20)
        self.frame_main.grid(row=0,column=0,padx=10,pady=10)

        self.frame_tabview=ctg.CTkFrame(master=self,width=(3*(widht_size/4))-60,height=height_size-20)
        self.frame_tabview.grid(row=0,column=1,padx=10,pady=10)


        self.tab_view = MyTabView(master=self.frame_tabview,width=(3*(widht_size/4))-60,height=height_size-40)
        self.tab_view.grid(row=0, column=0, padx=10, pady=10)


app = App()
app.mainloop()