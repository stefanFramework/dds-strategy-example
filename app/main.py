import sys

from domain.service import SortingService

def validate_input():
    # Fail if there isn't the correct number of arguments
    if len(sys.argv) < 3:
        raise Exception('Invalid number of arguments')

def get_elements():
    # Create a list of elements to be sorted
    return list(sys.argv[1].split(','))

def get_strategy():
    return sys.argv[2]

def sort(elements, selected_strategy):
    service = SortingService()
    return service.sort(elements, selected_strategy)

def main():
    try:
        # Check if all arguments are appropiate
        validate_input()

        # Get the elements to sort
        elements = get_elements()

        # Get the sorting strategy selected by the user
        selected_strategy = get_strategy()

        # Perform the selected sort operation
        result = sort(elements, selected_strategy)

        print(str(result))

    except Exception as ex:
        print('ERROR: ' + str(ex))

if __name__ == '__main__':
    main()