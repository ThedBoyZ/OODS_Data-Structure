def insert(arr, n):
    if n <= 1:
        return

    # Sort first n-1 elements
    insert(arr, n - 1)

    # Insert the last element into the sorted array
    last = arr[n - 1]
    j = n - 2

    while (j >= 0 and arr[j] > last):
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = last

    # Print the current step
    if arr[n:] != []:
        print(f"insert {last} at index {j + 1} : {arr[:n]} {arr[n:]}")
    else:
        print(f"insert {last} at index {j + 1} : {arr[:n]}")
        
def insertion_sort_recursive(arr):
    insert(arr, len(arr))

def main():
    # Take input as a list
    l = [int(x) for x in input("Enter Input : ").split()]

    # Call the insertion sort function
    insertion_sort_recursive(l)

    # Print the sorted list
    print("sorted")
    print(l)

if __name__ == "__main__":
    main()
