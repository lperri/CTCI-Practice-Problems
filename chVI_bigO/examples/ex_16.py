# powers of 2 from 1 through n (inclusive)

def print_powers_of_two(n: int) -> int:
    if n < 1:
        return 0
    elif n == 1:
        print(1)
        return 1
    else:
        prev = print_powers_of_two(n / 2)
        curr = prev * 2
        print(curr)
        return curr

# compute current value based on previous (*2)
# Time complexity O(logn) b/c log(n) = how many times we need to divide n by 2 to get 1
# Space complexity O(logn) b/c there are max logn recursive calls on the callstack
