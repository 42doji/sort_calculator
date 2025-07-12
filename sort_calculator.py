
def swap(arr, src_idx, dest_idx):
    arr[src_idx], arr[dest_idx] = arr[dest_idx], arr[src_idx]

def sort_nums(arr):
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i]:
                swap(arr, i, j)
    return arr

def input_handler():
    _inputs = input("Enter Number (1 5 32 -1..): ").split()
    try:
        _inputs = list(map(float, _inputs))
    except TypeError:
        print("Invalid input.")
    return _inputs

def main():
    _inputs = input_handler()
    print(sort_nums(_inputs))

if __name__ == "__main__":
    main()
