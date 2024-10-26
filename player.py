class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __init__(self, pos):
        self.x = pos[0]
        self.y = pos[1]

    def __str__(self):
        return f"player@{self.x}({self.y})"

    def set_x(self, new_x):
        self.x = new_x
    def get_x(self):
        return self.x

    def set_y(self, new_y):
        self.y = new_y
    def get_y(self):
        return self.y

    def get_player_pos(self):
        return (self.x, self.y)

    def get_player_sprite_size(self):
        return (32, 32)

    
        

