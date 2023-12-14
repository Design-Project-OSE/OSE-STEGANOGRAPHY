import os

class Name_Detect:
    def file_name_controller(self,file_path, search_word, file_format):
        files_in_path = os.listdir(file_path)
        if not files_in_path:
            return file_path + search_word + '.' + file_format
        
        # Aranacak kelimeyle eşleşen dosya adını kontrol et
        matched_files = [file_name for file_name in files_in_path if search_word in file_name]
        
        if not matched_files:
            return file_path + search_word + '.' + file_format
        
        # Eşleşen bir dosya adı varsa, en sonuncusunu alıp numarasını artır
        last_matched_file = matched_files[-1]
        index_start = last_matched_file.rfind(search_word)
        index_end = last_matched_file.rfind('.')
        number = last_matched_file[index_start + len(search_word):index_end]
        
        if number.isdigit():
            new_number = str(int(number) + 1)
        else:
            # Dosya adından sayısal ifade alınamadı veya boş bir dize geldi, 0'dan başlayarak yeni bir numara oluştur
            new_number = '1'
        
        # Yeni dosya adını oluştur ve döndür
        new_file_name = file_path + search_word + new_number + '.' + file_format
        return new_file_name

    def process_message(self,message):
        index = message.find("=")  # "=" işaretinin konumunu bul
        if index != -1:  # Eğer "=" işareti bulunduysa
            number_str = message[index + 1:]  # "=" işaretinden sonrasını al
            if number_str.isdigit():  # Eğer sayısal bir ifadeyse
                number_len = len(number_str)
                modified_message = message[:-number_len]  # Sayısal ifadeyi mesajdan sil
                return int(number_str), modified_message
            else:
                print("Sayısal ifade bulunamadı.")
                return None, message
        else:
            print("'=' işareti bulunamadı.")
            return None, message

    def name_check(self,loc_dir):
        index_start=loc_dir.rfind("/")
        index_final=loc_dir.rfind(".")
        name=loc_dir[index_start+1:index_final]
        return name

    def key_info_write(self,msg,info):
        info=len(msg)
        strinfo=str(info)
        if(len(strinfo)%2==1):
            strinfo='0'+strinfo
        msg=strinfo[:len(strinfo)//2]+'='+msg+'='+strinfo[len(strinfo)//2:]

        return msg

    def key_scizor(self,msg):
        first_index=msg.find('=')
        msg=msg[first_index+1:]
        second_index=msg.rfind('=')
        msg=msg[:second_index]
        return msg

    def key_info_read(self,msg:str):
        first_index=msg.find('=')
        first_numb=msg[:first_index]
        second_index=msg.rfind('=')
        second_numb=msg[second_index+1:]
        numb=first_numb+second_numb
        numb=int(numb)
        return numb


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

