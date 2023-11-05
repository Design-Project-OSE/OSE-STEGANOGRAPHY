import wave
import os
from tkinter import*  
import tkinter as tk
from tkinter import  filedialog
from pygame import mixer
from PIL import Image, ImageTk



root = tk.Tk()
root.title("deneme")
root.geometry("920x670+290+85")
root.configure(bg='#0f1a2b')
root.resizable(False, False)

mixer.init()

playlist = tk.Listbox(root)
playlist.pack(fill="both", expand=True)  # Liste kutusunu dolgu ile doldurup genişletin

#dosya açım işlemleri
def open_folder():
    path=filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs=os.listdir(path)
        for song in songs:
            if song.endswith(".wav"):
                playlist.insert(END,song)
        
def open_folder_button_click():
    open_folder()
    
# mesajı gömme butonu


# Müzik çalma fonksiyonu
def play_song():
    music_name=playlist.get(ACTIVE)
    print(music_name[0:-4])
    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()
    

# Play Button
play_image = Image.open("play_icon.png")
play_image = play_image.resize((30, 30), Image.ANTIALIAS)
play_icon = ImageTk.PhotoImage(play_image)
play_button = tk.Button(root, image=play_icon, bg="#FFFFFF", bd=0 , command=play_song)
play_button.place(x=400, y=500)

# Stop Button
stop_image = Image.open("stop_icon.png")
stop_image = stop_image.resize((30, 30), Image.ANTIALIAS)
stop_icon = ImageTk.PhotoImage(stop_image)
stop_button = tk.Button(root, image=stop_icon, bg="#FFFFFF", bd=0,command=mixer.music.stop)
stop_button.place(x=450, y=500)

# Open Folder Butonu
tk.Button(root, text="Open Folder", width=10, height=1, font=("arial", 10, "bold"), fg="white", bg="#21b3de", command=open_folder_button_click).place(x=50, y=212)

# textbox
text_box = tk.Text(root, height=10, width=40)
text_box.pack()
text_box.place(x=350, y=150)

# Mesajı göm butonu
tk.Button(root, text="Mesajı Göm", width=10, height=1, font=("arial", 10, "bold"), fg="white", bg="#21b3de").place(x=350, y=350)


root.mainloop()

# Şu anki çalışma dizinini al
current_directory = os.getcwd()
# Alt klasör adını belirle
subfolder = "Project_Voice"
# Ses dosyasının yolunu birleştir
path_to_audio = os.path.join(current_directory, subfolder, "song.wav")
# Ses dosyasını aç
song = wave.open(path_to_audio, mode='rb')
# Read frames and convert to byte array
frame_bytes = bytearray(list(song.readframes(song.getnframes())))

# The "secret" text message
string = 'Peter Parker is the Spiderman!' #textbox'dan alacak
# Append dummy data to fill out rest of the bytes. Receiver shall detect and remove these characters.
string = string + int((len(frame_bytes) - (len(string) * 8 * 8)) / 8) * '#'
# Convert text to bit array
bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8, '0') for i in string])))

# Replace LSB of each byte of the audio data by one bit from the text bit array
for i, bit in enumerate(bits):
    frame_bytes[i] = (frame_bytes[i] & 254) | bit
# Get the modified bytes
frame_modified = bytes(frame_bytes)

# Yeni ses dosyasını "Project_Voice" alt klasörüne kaydet
output_path = os.path.join(current_directory, subfolder, "song_embedded.wav")
with wave.open(output_path, 'wb') as fd:
    fd.setparams(song.getparams())
    fd.writeframes(frame_modified)
song.close()





# Use wave package (native to Python) for reading the received audio file
import wave
song = wave.open("song_embedded.wav", mode='rb')
# Convert audio to byte array
frame_bytes = bytearray(list(song.readframes(song.getnframes())))

# Extract the LSB of each byte
extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
# Convert byte array back to string
string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))
# Cut off at the filler characters
decoded = string.split("###")[0]

# Print the extracted text
print("Sucessfully decoded: "+decoded)
song.close()

# Yeni ses dosyasını "Project_Voice" alt klasörüne kaydet
output_path = os.path.join(current_directory, subfolder, "song_embedded.wav")
with wave.open(output_path, 'wb') as fd:
    fd.setparams(song.getparams())
    fd.writeframes(frame_modified)
song.close()

# Write bytes to a new wave audio file
with wave.open('song_embedded.wav', 'wb') as fd:
    fd.setparams(song.getparams())
    fd.writeframes(frame_modified)

bunun yerine yukardakini yaz