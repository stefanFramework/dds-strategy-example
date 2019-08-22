from domain.strategy_factory import SortingStrategyFactory

class SortingService:

    def sort(self, elements, selected_strategy):
        # Create the sorting strategy
        strategy = SortingStrategyFactory.create(selected_strategy)

        return strategy.sort(elements)