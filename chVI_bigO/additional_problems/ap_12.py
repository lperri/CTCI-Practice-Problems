from typing import List, Any


class ArrayIntersection:
    """
    Compute the intersection (the number of elements in common) of two arrays
        - Assume neither array has duplicates
        - Sort one array (array b) then iterate through array a, checking (via binary search)
        if each value is in array b
    """
    def __init__(self, array_a: List[Any], array_b: List[Any]):
        self.array_a = array_a
        self.array_b = sorted(array_b)
        self.intersection = set()
        # we want to call this method automatically
        self.findIntersection()

    def binarySearchArrayB(self, element: Any, floor: int = None, ceiling: int = None) -> bool:
        # critical that you use "is None" as opposed to ("if not (floor and ceiling)")
        # (i.e. checking if falsey) because once ceiling = 0, not ceiling = True
        # => and floor and ceiling get reset => max recurssion depth exceeded
        if floor is None and ceiling is None:
            floor, ceiling = 0, len(self.array_b) - 1

        # critical that we check that ceiling < floor as opposed to ("if ceiling <= floor")
        # because if element is the first element in both lists, ceiling must = floor for it to be found
        # i.e. the convergence of floor and ceiling is necessary in some cases, but crossing each other is bad
        if ceiling < floor or not self.array_b:
            return False

        # use floor division to handle odd/even length arrays
        mid = (ceiling + floor) // 2

        if self.array_b[mid] == element:
            self.intersection.add(element)
            return True
        elif self.array_b[mid] < element:
            # critical that we actually return here instead of just calling the method
            return self.binarySearchArrayB(element, floor=(mid + 1), ceiling=ceiling)
        else:
            # critical that we actually return here instead of just calling the method
            return self.binarySearchArrayB(element, floor=floor, ceiling=(mid - 1))

    def findIntersection(self) -> set:
        for element in self.array_a:
            self.binarySearchArrayB(element)
        if len(self.intersection) == 0:
            return f'There is no intersection between {self.array_a} and {self.array_b}'
        return self.intersection


if __name__ == "__main__":
    test_array_a, test_array_b = [39, 23, 1, 4], [23, 28]
    print(ArrayIntersection(test_array_a, test_array_b).findIntersection())

# len(array_a) = a, len(array_b) = b
# first sort array_b => O(blogb) -- comparison-based sorting alg runtime
# runtime of binarySearchArrayB method is O(logb) because we are cutting the problem space in half each iteration
# runtime of findIntersection is O(a)*O(logb)
# total runtime = O( blogb + alogb )