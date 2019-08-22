class SortingStrategy:
    @staticmethod
    def get_identifier():
        raise NotImplementedError()

    def sort(self, elements):
        raise NotImplementedError()

class AscendentSortingStrategy(SortingStrategy):
    @staticmethod
    def get_identifier():
        return 'sorting-asc'

    def sort(self, elements):
        return sorted(elements, reverse=False)

class DescendentSortingStrategy(SortingStrategy):
    @staticmethod
    def get_identifier():
        return 'sorting-desc'

    def sort(self, elements):
        return sorted(elements, reverse=True)