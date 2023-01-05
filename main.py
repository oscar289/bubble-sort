def bubble_sort(lst):
    # Set swap to True to start the while loop
    swap = True

    # Continue looping as long as swap is True
    while swap:
        # Set swap to False to begin the loop
        swap = False

        # Loop through the list
        for i in range(len(lst) - 1):
            # If the current element is greater than the next element, swap them
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                # Set swap to True to indicate that a swap has occurred
                swap = True
    return lst

print(bubble_sort([1, 9, 3, 7, 1, 5]))