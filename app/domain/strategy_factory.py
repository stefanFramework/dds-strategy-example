from domain.strategy import  AscendentSortingStrategy, DescendentSortingStrategy

class StrategyFactory:
    @staticmethod
    def create(strategy_identifier):
        pass

class SortingStrategyFactory(StrategyFactory):
    @staticmethod
    def create(strategy_identifier):
        if strategy_identifier == AscendentSortingStrategy.get_identifier():
            return AscendentSortingStrategy()

        if strategy_identifier == DescendentSortingStrategy.get_identifier():
            return DescendentSortingStrategy()

        raise Exception('Invalid Sorting Strategy')

