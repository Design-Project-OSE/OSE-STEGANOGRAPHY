import wave
from OSE_Tool import *
from OSE_File import *
f_tool=File_Tool()
v_tool=Voice_Tool
n_tool=Name_Detect

class voice_Lsb():
    def hideData(self,text_to_hide,audio_file,output):
        with wave.open(audio_file, "rb") as audio:
            frames = audio.readframes(audio.getnframes())

        # Metni ASCII karakter dizisine dönüştürme
        text_as_bytes = text_to_hide.encode('utf-8')
        text_length = len(text_as_bytes)

        # Metni ses dosyasına gizleme
        if text_length * 8 > len(frames):
            print("Metin çok uzun, gizlenemez.")
            return

        frames = bytearray(frames)
        for i in range(text_length):
            char_byte = text_as_bytes[i]
            for j in range(8):
                frames[i * 8 + j] = (frames[i * 8 + j] & 0xFE) | ((char_byte >> j) & 0x01)
        with wave.open(output, "wb") as output_audio:
            output_audio.setparams(audio.getparams())
            output_audio.writeframes(frames)

        return 

    def showdata(self,audio_file:str,text_length:int):
        with wave.open(audio_file, "rb") as audio:
            frames = audio.readframes(audio.getnframes())

        extracted_bytes = bytearray()
        for i in range(text_length):
            char_byte = 0
            for j in range(8):
                char_byte = char_byte | ((frames[i * 8 + j] & 0x01) << j)
            extracted_bytes.append(char_byte)

    # Gizli metni ASCII'ye dönüştürme
        return extracted_bytes.decode('utf-8')
        