class World:
    def __init__(self, width:int=100, height:int=100):
        self.StoredWorld = self.initalization(width, height)

    #Constuct Base World with the terrain and weather builders
    def initalization(self, width, height):
        world_array = []
        for _ in range(height):
            for _ in range(width):
                pass

    def __str__(self):
        pass