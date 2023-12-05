from stegano import lsb

class image_Lsb():
    def hideData(self,filename,message):
        return lsb.hide(str(filename), message,encoding="UTF-8",auto_convert_rgb=True) # lsb.hide() fonksiyonu, mesajı resim dosyasına gizler. Mesaj gizlenen resim secret değişkeninde atılır


    def showData(self,filename):
        return lsb.reveal(filename,encoding="UTF-8") # lsb.reveal() fonksiyonu, gizlenmiş mesajı resim dosyasından çıkarır.
