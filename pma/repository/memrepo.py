from pma.domain.stock import Stock

class MemRepo:
    def __init__(self, data):
        self.data = data

    def list(self):
        return [Stock.from_dict(i) for i in self.data]
