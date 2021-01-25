class Config:
    __config = {
        "app_title" : "Covoy's Game of Life",
        "tile_size": 16,
        "screen_width": 1080,
        "screen_height": 720,
        "colors": {
            "BLACK": (0, 0, 0),
            "WHITE": (255, 255, 255),
            "GREY": (50, 50, 50)
        },
        "frames_per_second": 60,
        "generations_per_second": 10
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