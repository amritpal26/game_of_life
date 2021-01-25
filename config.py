from itertools import cycle

class Config:
    __config = {
        "app_title" : "Covoy's Game of Life",
        "tile_sizes": [8, 16, 32],
        "tile_size": 8,

         # make sure the dimensions of screen are multiples of all the tile_sizes.
        "screen_width": 1088,
        "screen_height": 736,

        "frames_per_second": 60,
        "generations_per_second": 10,

        "font": 'courier new',
        "font_size": 15,
        "colors": {
            "BLACK": (0, 0, 0),
            "WHITE": (255, 255, 255),
            "GREY": (50, 50, 50),
            "RED": (255, 0, 0)
        },
    }

    __setters = ["tile_size"]

    @staticmethod
    def get_config(name):
        return Config.__config[name]

    @staticmethod
    def set_config(name, value):
        if name in Config.__setters:
            Config.__config[name] = value
        else:
            raise NameError("Name not accepted in set() method")