
import soundfile as sf
from OSE_Tool import*
name_detect=Name_Detect()

class Convert_Media():

    def cnv_mp3_wav(self,patch):
        music_patch="Project_Tools\\"
        wav_name=name_detect.file_name_controller(music_patch,'wavfile','.wav')
        data,samplerate=sf.read(patch)
        sf.write(wav_name,data,samplerate)
        return 

    def cnv_wav_mp3(self,wav_patch,save_patch):
        wav_open=AudioSegment.from_wav(wav_patch)
        mp3_file.export(save_patch,format='mp3')
        return

