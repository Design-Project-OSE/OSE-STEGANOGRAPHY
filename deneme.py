




loc_dir="C:/Users/sinan/OneDrive - erciyes.edu.tr/Masaüstü/Design Project/OSE PROJECT/Project-OSE/Project_Voice/ver0.mp3"
index_start=loc_dir.rfind("/")
index_final=loc_dir.rfind(".mp3")
music_name=loc_dir[index_start+1:index_final]
print(music_name)
