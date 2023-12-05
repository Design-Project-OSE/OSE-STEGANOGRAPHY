import pygame
from pygame import mixer

class player():
    def voice_play(self,loc_music):#Müzik Play butonu ile çalışacak fonksiyon
        pygame.mixer.init()
        mixer.music.load(loc_music)
        mixer.music.play()
        return

    def voice_stop(self):#Müzik Stop butonu ile çalışacak fonksiyon
        mixer.music.stop(),
        pygame.quit()
        return

    def voice_pause(self):#Müzik Pause ile çalışacak fonksiyon
        mixer.music.pause()
        return

    def voice_resume(self):#Müzik Resume butonu ile çalışacak fonksiyon
        mixer.music.unpause()
        return