def insertion_sort_desc(arr):
    print("Starting insertion sort in descending order...")
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        print(f"\nInserting element {key} at index {i}")
    print("\nSorting complete.")


if __name__ == "__main__":
    arr = [5, 2, 9, 1, 5, 6]
    print("Original array:", arr)
    insertion_sort_desc(arr)
    print("\nSorted array (descending):", arr)