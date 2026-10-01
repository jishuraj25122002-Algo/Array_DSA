# ============================================================
#          ARRAY IMPLEMENTATION USING NUMPY
#                 MENU-DRIVEN PROGRAM
# ============================================================

import numpy as np


# ------------------------------------------------------------
# Display Array
# ------------------------------------------------------------

def display_array(arr):
    """Display all elements of the array."""

    if arr.size == 0:
        print("\nArray is empty.")
    else:
        print("\nArray:", arr)


# ------------------------------------------------------------
# Insert Element
# ------------------------------------------------------------

def insert_element(arr):
    """Insert an element at a specific index."""

    value = int(input("Enter the element to insert: "))
    index = int(input("Enter the index: "))

    if 0 <= index <= arr.size:

        arr = np.insert(arr, index, value)

        print(f"{value} inserted successfully at index {index}.")

    else:

        print("Invalid index!")

    return arr


# ------------------------------------------------------------
# Delete Element
# ------------------------------------------------------------

def delete_element(arr):
    """Delete the first occurrence of an element."""

    if arr.size == 0:
        print("\nArray is empty.")
        return arr

    value = int(input("Enter the element to delete: "))

    positions = np.where(arr == value)[0]

    if positions.size > 0:

        index = positions[0]

        arr = np.delete(arr, index)

        print(f"{value} deleted successfully.")

    else:

        print(f"{value} not found in the array.")

    return arr


# ------------------------------------------------------------
# Search Element
# ------------------------------------------------------------

def search_element(arr):
    """Search an element using linear search."""

    if arr.size == 0:
        print("\nArray is empty.")
        return

    value = int(input("Enter the element to search: "))

    positions = np.where(arr == value)[0]

    if positions.size > 0:

        print(f"{value} found at index {positions[0]}.")

    else:

        print(f"{value} not found in the array.")


# ------------------------------------------------------------
# Update Element
# ------------------------------------------------------------

def update_element(arr):
    """Update an element at a specific index."""

    if arr.size == 0:
        print("\nArray is empty.")
        return arr

    index = int(input("Enter the index to update: "))

    if 0 <= index < arr.size:

        new_value = int(input("Enter the new value: "))

        old_value = arr[index]

        arr[index] = new_value

        print(
            f"Element {old_value} at index {index} "
            f"updated to {new_value}."
        )

    else:

        print("Invalid index!")

    return arr


# ============================================================
#                    MAIN PROGRAM
# ============================================================

print("=" * 55)
print("         ARRAY IMPLEMENTATION USING NUMPY")
print("=" * 55)


# ------------------------------------------------------------
# Take Array Input from User
# ------------------------------------------------------------

n = int(input("Enter the number of elements: "))

elements = []

print(f"\nEnter {n} integer elements:")

for i in range(n):

    value = int(input(f"Enter element {i + 1}: "))

    elements.append(value)


# Convert Python list into NumPy array
arr = np.array(elements, dtype=int)


print("\nArray created successfully!")
print("Array:", arr)


# ============================================================
#                    MENU-DRIVEN PROGRAM
# ============================================================

while True:

    print("\n" + "=" * 55)
    print("                    ARRAY MENU")
    print("=" * 55)

    print("1. Display Array")
    print("2. Insert Element")
    print("3. Delete Element")
    print("4. Search Element")
    print("5. Update Element")
    print("6. Exit")

    print("=" * 55)

    choice = int(input("Enter your choice: "))


    # --------------------------------------------------------
    # Display
    # --------------------------------------------------------

    if choice == 1:

        display_array(arr)


    # --------------------------------------------------------
    # Insert
    # --------------------------------------------------------

    elif choice == 2:

        arr = insert_element(arr)


    # --------------------------------------------------------
    # Delete
    # --------------------------------------------------------

    elif choice == 3:

        arr = delete_element(arr)


    # --------------------------------------------------------
    # Search
    # --------------------------------------------------------

    elif choice == 4:

        search_element(arr)


    # --------------------------------------------------------
    # Update
    # --------------------------------------------------------

    elif choice == 5:

        arr = update_element(arr)


    # --------------------------------------------------------
    # Exit
    # --------------------------------------------------------

    elif choice == 6:

        print("\nProgram terminated successfully.")
        break


    # --------------------------------------------------------
    # Invalid Choice
    # --------------------------------------------------------

    else:

        print("\nInvalid choice!")
        print("Please enter a number between 1 and 6.")
