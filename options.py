import pygame

class Options:
    options = {
        "sound": True,
        "music": False,
        "fullscreen": False,
        "vsync": False
    }

    def getValue(self, elem):
        return self.options[elem]

    def setValue(self, elem, value):
        self.options[elem] = value

class Sounds(Options):
    musicPlaying = False
    currentSound = 0
    volume = 0.3

    def playSound(self, path):
        if Options.getValue(self, "sound"):
            self.currentSound = pygame.mixer.Sound(path)
            pygame.mixer.Sound.play(self.currentSound)
            self.currentSound.set_volume(self.volume)

    def playMusic(self, path, loop, restart = False):
        if Options.getValue(self, "music"):
            if restart and self.musicPlaying:
                self.stopMusic()
            if restart or not self.musicPlaying:
                if loop:
                    pygame.mixer.music.load(path)
                    pygame.mixer.music.set_volume(self.volume)
                    pygame.mixer.music.play(-1)
                else:
                    pygame.mixer.music.load(path)
                    pygame.mixer.music.set_volume(self.volume)
                    pygame.mixer.music.play()
            self.musicPlaying = True

    def stopMusic(self):
        self.musicPlaying = False
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()

    def changeVolume(self, volume):
        if volume >= 0.1 and volume <= 1.0:
            if pygame.mixer.get_busy():
                self.volume = volume
                self.currentSound.set_volume(self.volume)
