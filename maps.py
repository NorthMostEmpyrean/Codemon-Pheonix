class Maps:
    default_t_width = 32
    default_t_height = 32

    def __init__(self, name, size):
        self.name = name
        self.width = size[0]
        self.height = size[1]
        self.TILE_WIDTH = default_t_width
        self.TILE_HEIGHT = default_height

    def check_collision(self, target_coord):
        pass
