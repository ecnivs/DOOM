# DOOM 1993
# by Vince Swu

from wad_data import WADData

class DoomEngine:
    def __init__(self, path = "wad/DOOM1.WAD"):
        self.wad_path = path
        self.on_init()

    def on_init(self):
        self.wad_data = WADData(self, map_name='E1M1')


if __name__ == "__main__":
    doom = DoomEngine()
