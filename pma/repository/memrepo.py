from pma.domain.stock import Stock


class MemRepo:
    def __init__(self, data):
        self.data = data

    def list(self, filters=None):

        result = [Stock.from_dict(i) for i in self.data]

        if filters is None:
            return result

        if 'code__eq' in filters:
            result = [s for s in result if s.code == filters['code__eq']]

        if 'price__eq' in filters:
            result = [s for s in result if s.price == float(filters['price__eq'])]

        if 'price__lt' in filters:
            result = [s for s in result if s.price < float(filters['price__lt'])]

        if 'price__gt' in filters:
            result = [s for s in result if s.price > float(filters['price__gt'])]

        return result
