def process_message(message):
    index = message.find("=")  # "=" işaretinin konumunu bul
    if index != -1:  # Eğer "=" işareti bulunduysa
        number_str = message[index + 1:]  # "=" işaretinden sonrasını al
        if number_str.isdigit():  # Eğer sayısal bir ifadeyse
            number_len = len(number_str)
            modified_message = message[:-number_len]  # Sayısal ifadeyi mesajdan sil
            return int(number_str), modified_message
        else:
            print("Sayısal ifade bulunamadı.")
            return None, message
    else:
        print("'=' işareti bulunamadı.")
        return None, message

# Fonksiyonun kullanımı
message = "012abcdefgişas452asdd=108"
number, modified_message = process_message(message)
print("Alınan sayı:", number)
print("Değiştirilmiş mesaj:", modified_message)