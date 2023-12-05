import wave


class voice_Lsb():
    def hideData(self,infile:str,message:str,outfile:str):
        song=wave.open(patch,mode='rb')
        frame_bytes=bytearray(list(song.readframes(song.getnframes())))

        message=message+int((len(frame_bytes)-(len(message)*8*8))/8)*'#'
        bits=list(map(int,''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in message])))

        for i ,bit in enumerate(bits):
            frame_bytes[i]=(frame_bytes[i]&254)|bit
        frame_modified=bytes(frame_bytes)
        save_file=wave.open(outfile,mode='wb')
        save_file.setparams(audio.setparams)
        save_file.writeframes(frame_modified)

        save_file.close()
        song.close()

        