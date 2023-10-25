from tkinter import filedialog as fd
import pyautogui


class File_Tool:
    def open_file(self):
        super().__init__()
        self.loc_file=fd.askopenfilename()
        return self.loc_file




class Get_Info:
        def screen_size(self):
            super().__init__()
            self.width,self.height=pyautogui.size()
            return self.width,self.height



