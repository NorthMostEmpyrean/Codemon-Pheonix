import os

class Maps:
    default_t_width = 32
    default_t_height = 32
    map_dir = "maps\\"

    def __init__(self, name, map_path):
        #Basic Dimensionality
        self.name = name
        self.TILE_WIDTH = self.default_t_width
        self.TILE_HEIGHT = self.default_t_height

        #Actual Map data 
        self.map_file_name = map_path
        self.data = self.load_map()

    def get_tile_width(self):
        return self.TILE_WIDTH
    
    def get_tile_height(self):
        return self.TILE_HEIGHT
    
    def get_center(self):
        return (self.width//2, self.height//2)

    def load_map(self):

        delim_char = ","

        cwd = os.getcwd()
        path_to_file = os.path.join(cwd, self.map_dir)
        path_to_file = os.path.join(path_to_file, self.map_file_name)
        file_ptr = open (path_to_file, "r", 1)

        #Read the width and height of the map
        dimension = file_ptr.readline()
        dimension = dimension.strip().strip("()").split(delim_char)
        self.width = int(dimension[0])
        self.height = int(dimension[1])

        temp_map_data = {}
        
        # Read the body of the data from the file reading 2 characters for each tile 
        # (the second read is for delimiter character which is , ) 
        new_tile = ""
        row_counter = 0
        for row in file_ptr.readlines():
            tiles = row.strip("'\n").split(delim_char)
            temp_map_data[row_counter] = tiles
            row_counter += 1
        file_ptr.close()  
        return temp_map_data

    def check_collision(self, target_coord):
        pass
