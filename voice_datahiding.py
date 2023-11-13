import wave
import os

# Şu anki çalışma dizinini al
current_directory = os.getcwd()

# Ses dosyasının yolunu birleştir
path_to_audio = os.path.join(current_directory,"Project_Voice", "song.wav")


# Ses dosyasını 'rb' read binary modunda açar
song = wave.open(path_to_audio, mode='rb')


# Ses dosyası frame'lerden oluşur . song.getnframes ile alınan frameler readframe ile okunur ,
# Listeye dönüştürüldükten sonra frame_bytes adlı bytearray'e atanır.
frame_bytes = bytearray(list(song.readframes(song.getnframes())))

# Gizlenmek istenen text mesajı string adlı değişkene atanır.
string = 'Peter Parker is the Spiderman!' #textbox'dan alacak

# Bu kod satırı, gizlenen metin mesajının ses dosyasına eklenmeden önce boyutunu ayarlamak için kullanılır. 
# Bu işlem, gizlenecek metin mesajının ses dosyasına sığmasını sağlar. Daha detaylı bilgi için aşağıyı oku.
'''
# len(frame_bytes) = ses dosyasinin kaç bayttan oluştuğu bilgisini döndürür.
# len(string)*8*8  = gizlenmek istenen mesajin bit cinsinden boyutu
# (len(frame_bytes) - (len(string) * 8 * 8)) / 8  -> ses dosyasi boyutu - gizlenmek istenen mesajin boyutu = kalan boşluk miktari (bayt cinsinden)
# utf-8 formati 1 karakteri 1 bayt ile ifade ettiğinden kalan boşluklar random bir karakter ile doldurulur(buradaki karakter #)
'''
string = string + int((len(frame_bytes) - (len(string) * 8 * 8)) / 8) * '#'

# gizlenmek istenen mesaj bit array'e dönüştürülür. Daha detaylı bilgi için aşağıyı oku.
'''
ord(i)       : i' karakterinin ascii tam sayi karsiliğini döndürür .
bin(ord(i))  : ikili sayiya çevirir. -> örneğin 0b1000001 (0b sayinin binary oldugunu gösterir.)
lstrip('0b') : 0b notasyonunu kaldirir.
rjust(8, '0'): ikilik sayi 8 bite tamamlanir (bosluk varsa sonunda 0 eklenir.)
.join(...)   : karakterleri birlestirir -> 0110100100101010010101010000110100 gibi..
map(...)     : dizeye çevirir -> [0,1,1,0,1,0,0,1....] gibi...
'''
bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8, '0') for i in string])))


# Ses dosyasındaki her bir byte'ın en düşük anlamlı (LSB) biti, metin mesajının bitlerine sırasıyla yerleştirilir.
'''
(frame_bytes[i] & 254) : ses dosyasinin her bayti 254 (11111110) maskesiyle and'lenir.Bu sayede sadece son bit 0 olur,diğerleri neyse ayni kalir
(frame_bytes[i] & 254) | bit : çikan sonuc bit ile or'lanir bu sayede gizli mesaj gömülmüş olur.
daha sonra değiştirilmiş baytlar frame_modified adli yeni bytes veri tipinde tutulur.
extra bilgi : bytes ile byte_array'in farki bytes immutable (değiştirilemez) , bytearray mutable (değiştirilebilir) olmasidir.
'''
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



# -- GİZLENMİŞ METNİ ÇIKARMA --

# Şu anki çalışma dizinini alır
current_directory = os.getcwd()

# Ses dosyasının yolunu birleştirir
path_to_audio = os.path.join(current_directory, "Project_Voice", "song.wav") # song.wav dosyası eklenecek . Şuan dizinde yok.

# Ses dosyasını 'rb' read binary modunda açar
song = wave.open(path_to_audio, mode='rb')

# Bytearray'e dönüstürülür.
frame_bytes = bytearray(list(song.readframes(song.getnframes())))

# Her bir baytin lsb biti ayiklanir.
# Metni gömerken 255 ile and'lemiştik . Bu işlemin tersini yapıyoruz.
extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]

# Bytearray'i tekrar string ifadeye dönüştürür. 
'''
for i in range(0, len(extracted), 8): Bu döngü, extracted listesindeki bitleri 8'li gruplar halinde işlemek için kullanilir.
Her döngü adiminda i, 0'dan başlayarak 8'er 8'er artar. Bu, her 8 bitlik grup için bir işlem yapilmasini sağlar.

extracted[i:i+8]: Bu ifade, extracted listesindeki bitlerin 8'li gruplarini seçer. 
"".join(map(str, extracted[i:i+8])): Her 8 bitlik grup, bir dizeye dönüştürülür ve bu dizedeki bitler birleştirilir
int(..., 2): Dize olarak temsil edilen ikili (binary) sayi, ondalik (decimal) bir sayiya dönüştürülür.
chr(...): Dönüştürülen ondalik sayi, ASCII karakter koduna dönüştürülür.

"".join(...): Elde edilen karakterler, bir dize haline getirilir.
Her bir döngü adiminda elde edilen karakterler, metin mesajinin parçalarini oluşturur.
'''
string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))
# Metnin sonuna eklediğimiz gereksiz karakteri (#) atar.
decoded = string.split("###")[0]

# Gizli bilgi çıkarılmış text'i basar.
print("Sucessfully decoded: " + decoded)
song.close()
