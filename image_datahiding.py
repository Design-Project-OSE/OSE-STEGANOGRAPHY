from stegano import lsb
import CTkMessagebox as messagebox
class DataHiding():
    count = 1

    def hideData(filename):
        try:
            message = text1.get(1.0, END) # kullanıcının girdiği mesajı message değişkenine atıyor
            global secret
            secret = lsb.hide(str(fileName), message) # lsb.hide() fonksiyonu, mesajı resim dosyasına gizler. Mesaj gizlenen resim secret değişkeninde atılır
        except:
            messagebox.showwarning("!WARNING!", "Please choose an image and write your message what you want to hide. After then click the Hide button")

    def showData(filename):
        try:
            hiddenData = lsb.reveal(fileName) # lsb.reveal() fonksiyonu, gizlenmiş mesajı resim dosyasından çıkarır.
            text1.delete(1.0, END)
            text1.insert(END, hiddenData) # çıkarılan gizlenmiş mesaj ilgili alana eklenir.
        except:
            messagebox.showwarning("!WARNING!", "Please choose an image")
        
    def saveData():
        try:
            # mevcut dizinde o dosya isminyle aynı başka bir dosya varsa dosya adını değiştirmek için
            if not os.path.exists("hidden ({})".format(DataHiding.count)):
                secret.save("hidden ({}).png".format(DataHiding.count)) # bilginin gizlendiği secret değişkeni belirtilen isimde ve png formatında bir resim olarak kaydedilir
            DataHiding.count += 1
        except:
            messagebox.showwarning("!WARNING!", "Please choose an image and write your message")