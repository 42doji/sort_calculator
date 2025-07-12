
def swap(arr, src_idx, dest_idx):
    arr[src_idx], arr[dest_idx] = arr[dest_idx], arr[src_idx]

def sort_nums(arr):
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i]:
                swap(arr, i, j)
    return arr

def input_handler():
    try:
        _inputs = input("Enter Numbers: ").split()
        _inputs = list(map(float, _inputs))
    except ValueError:
        print("Invalid input.")
        return
    return _inputs

def print_sorted(nums):
    res = "Sorted: "
    for num in nums:
        res += str(num) + " "
    print(res)

def main():
    while 42:
        _inputs = []
        while not _inputs:
            _inputs = input_handler()
        print_sorted(sort_nums(_inputs))


if __name__ == "__main__":
    main()
