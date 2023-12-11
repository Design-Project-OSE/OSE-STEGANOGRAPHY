import wave

# Metni ses dosyasına gizleme fonksiyonu
def hide_text_in_audio(audio_file, text_to_hide):
    with wave.open(audio_file, "rb") as audio:
        frames = audio.readframes(audio.getnframes())

        # Metni ASCII karakter dizisine dönüştürme
        text_as_bytes = text_to_hide.encode('utf-8')
        text_length = len(text_as_bytes)

        # Metni ses dosyasına gizleme
        if text_length * 8 > len(frames):
            print("Metin çok uzun, gizlenemez.")
            return

        frames = bytearray(frames)
        for i in range(text_length):
            char_byte = text_as_bytes[i]
            for j in range(8):
                frames[i * 8 + j] = (frames[i * 8 + j] & 0xFE) | ((char_byte >> j) & 0x01)

    # Gizlenmiş ses dosyasını kaydetme
    output_file = "hidden_audio.wav"
    with wave.open(output_file, "wb") as output_audio:
        output_audio.setparams(audio.getparams())
        output_audio.writeframes(frames)
    print(f"Metin '{text_to_hide}' ses dosyasına gizlendi. Dosya adı: {output_file}")

# Ses dosyasından metni çıkarma fonksiyonu
def extract_text_from_audio(audio_file, text_length):
    with wave.open(audio_file, "rb") as audio:
        frames = audio.readframes(audio.getnframes())

        extracted_bytes = bytearray()
        for i in range(text_length):
            char_byte = 0
            for j in range(8):
                char_byte = char_byte | ((frames[i * 8 + j] & 0x01) << j)
            extracted_bytes.append(char_byte)

    # Gizli metni ASCII'ye dönüştürme
    extracted_text = extracted_bytes.decode('utf-8')
    print(f"Gizli metin: '{extracted_text}'")

# Örnek kullanım
audio_file_path = "hidden_audio.wav"
text_to_hide = "Sex in my life in cesfsfsdfsfsfsfsfsfsfsfkjkhjkhjkhjk"

# Metni ses dosyasına gizleme


# Ses dosyasından metni çıkarma
text_length = len(text_to_hide)
extract_text_from_audio("hidden_audio.wav", text_length)
