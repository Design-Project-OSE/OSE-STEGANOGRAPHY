
import soundfile as sf
from OSE_Tool import*
name_detect=Name_Detect()

class Convert_Media():

    def cnv_mp3_wav(self,patch,name):
        music_patch="Project_Tools\\"
        wav_name=name_detect.file_name_controller(music_patch,name,'wav')
        data,samplerate=sf.read(patch)
        sf.write(wav_name,data,samplerate)
        return wav_name

