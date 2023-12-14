def process_message(message):
    index = message.find("==")  # "=="" işaretinin konumunu bul
    if index != -1:  # Eğer "=="" işareti bulunduysa
        number_str = message[index + 2:]  # Sayısal ifadenin bulunduğu kısmı al
        number = int(number_str)  # Sayısal ifadeyi integer'a dönüştür
        modified_message = message.replace(number_str, "")  # Sayısal ifadeyi mesajdan sil
        return number, modified_message
    else:
        return None, message  # "=="" işareti bulunamazsa aynı mesajı döndür

# Fonksiyonun kullanımı
message = "012abcdefgişas452asdd==108"
number, modified_message = process_message(message)
print("Alınan sayı:", number)
print("Değiştirilmiş mesaj:", modified_message)