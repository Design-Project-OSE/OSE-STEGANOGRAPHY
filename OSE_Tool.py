import os

class Name_Detect:
    def file_name_controller(self,patch,search,extension):
        list_patch=os.listdir(patch)
        if len(list_patch)==0:
            name=patch_search+'0'+'.'+extension
        else:   
            last_file=list_patch[-1] 
            index_start=last_file.rfind(search)
            index_start=index_start+search.__len__()
            index_end=last_file.rfind('.')
            number=last_file[index_start:index_end]
            number=str(int(number)+1)
            name=patch+search+number+extension
        return name


    def name_check(self,loc_dir):
        index_start=loc_dir.rfind("/")
        index_final=loc_dir.rfind(".")
        name=loc_dir[index_start+1:index_final]
        return name

import soundfile as sf
import numpy as np
from scipy import signal

class Voice_Tool():
    def create_noisy(voice_patch):

        # Orijinal ses dosyasını oku
        ses, samplerate = sf.read(voice_patch)

        # Yeni gürültü oluştur
        noisy = np.random.randn(len(ses))

        #frekans ayarı
        cutoff_freq=500
        ord=4
        b, a = signal.butter(ord, cutoff_freq, btype='low', fs=samplerate)
        noisy_filt = signal.filtfilt(b, a, noisy)

        patch_noisy=Name_Detect.file_name_controller(self,"Project_Tools\\",'noisy')
        # Gürültü dosyasını oluştururken örnekleme frekansını belirt
        sf.write(patch_noisy, noisy_filt, samplerate)
        return patch_noisy

