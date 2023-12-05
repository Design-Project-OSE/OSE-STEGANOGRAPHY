import random
import string
from pydub import AudioSegment

mp3_file_path = "Project_Voice\\Chopin.mp3"
wav_save_folder = "Project_Voice\\Chopin.wav"
letters = string.ascii_lowercase
file_name = ''.join(random.choice(letters) for _ in range(10))
file_name = file_name + '.wav'



wav_file = AudioSegment.from_mp3(mp3_file_path)
wav_file.export(wav_save_folder, format='wav')