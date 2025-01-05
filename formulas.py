class SortingAlgorithms:
    @staticmethod
    def bubble_sort(list_data, bubble_list, sorting_order):
        # Optimized bubble sort
        n = len(list_data)
        for i in range(n):
            swapped = False
            for x in range(n - 1):
                compare_formula = (getattr(list_data[x], bubble_list) > getattr(list_data[x + 1], bubble_list)) \
                                    if sorting_order == 'ascending' else \
                                    (getattr(list_data[x], bubble_list) < getattr(list_data[x + 1], bubble_list))

                if compare_formula:
                    list_data[x], list_data[x + 1] = list_data[x + 1], list_data[x]
                    swapped = True

            if not swapped:
                break

        return list_data

    @staticmethod
    def quick_sort(list_data, bubble_list, sorting_order):
        # Quick sort
        if len(list_data) <= 1:
            return list_data
        else:
            middle = len(list_data) // 2
            pivot = getattr(list_data[middle], bubble_list)
            left = [s for s in list_data[:middle] if getattr(s, bubble_list) < pivot]
            right = [s for s in list_data[middle + 1:] if getattr(s, bubble_list) >= pivot]

            if sorting_order == 'ascending':
                return SortingAlgorithms.quick_sort(left, bubble_list, sorting_order) + [list_data[middle]] + SortingAlgorithms.quick_sort(right, bubble_list, sorting_order)
            elif sorting_order == 'descending':
                return SortingAlgorithms.quick_sort(right, bubble_list, sorting_order) + [list_data[middle]] + SortingAlgorithms.quick_sort(left, bubble_list, sorting_order)


class SearchingAlgorithms:
    @staticmethod
    def linear_search(list_data, bubble_list, value):
        # Linear search
        for i, item in enumerate(list_data):
            if getattr(item, bubble_list) == value:
                return i
        return -1

    @staticmethod
    def binary_search(list_data, bubble_list, value):
        # Binary search
        low, high = 0, len(list_data) - 1
        while low <= high:
            middle = (low + high) // 2
            middle_value = getattr(list_data[middle], bubble_list)

            if middle_value == value:
                return middle
            elif middle_value < value:
                low = middle + 1
            else:
                high = middle - 1

        return -1

