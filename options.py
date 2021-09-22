class Options:
    options = {
        "sound": True,
        "music": False,
        "fullscreen": False,
        "vsync": False
    }

    def getValue(self, elem):
        if self.options[elem]:
            return self.options[elem]

    def setValue(self, elem, value):
        if self.options[elem]:
            self.options[elem] = value