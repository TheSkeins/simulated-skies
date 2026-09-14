class TerrainCell:
    def __init__(self, TerrainType:str, Height:int, Temperature:float, Humidity:float, Albedo:int):
        self.TerrainType = TerrainType
        self.Height      = Height
        self.Temperature = Temperature
        self.Humidity    = Humidity
        self.Albedo      = Albedo

    def __str__(self):
        return f"{self.TerrainType} | {self.Height} | {self.Temperature} | {self.Humidity} | {self.Albedo}"