# Experiments using Python arrays and vectors
# Officially called as Lists in Python

def array_test():
    ar = [3, 2, 4, 5]

    # Popping and Appending
    ar.pop()
    ar.pop(1)           # Using Index of the element
    ar.append(6)

    print(ar)

    # index of given value
    print("Index of 4: ", ar.index(4))

    # remove the first occurrence of item with given value
    ar.remove(4)
    print("Removed 4: ", ar)

    # reverses an array
    ar.reverse()
    print("reversed: ", ar)

    # returns a sorted array, the original array is un-touched
    print("sorted return: ", sorted(ar))

    # sorts the array in place
    ar.sort()
    print("Array sorted in place: ", ar)

    # Find the length of the array
    print("Length of the array: ", len(ar))

    # Checking if an element is present inside the list
    print("Checking if the number 9 is present :", 9 in ar)

def main():
    array_test()


# The condition if __name__ == ‘__main__’ is used in a Python program to execute the code inside the if statement
# only when the program is executed directly by the Python interpreter. When the code in the file is imported as a
# module the code inside the if statement is not executed.

if __name__ == "__main__":
    main()