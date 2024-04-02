class Pack:
    def __init__(self, name, number, cost) -> None:
        self.name = name
        self.number = number
        self.cost = cost
        self.commons = []
        self.rares = []
        self.super_rares = []
        self.ultra_rares = []
