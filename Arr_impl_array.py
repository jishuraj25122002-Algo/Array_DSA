
# ============================================================
#       ARRAY IMPLEMENTATION USING array()
#              FULLY USER-INPUT PROGRAM
# ============================================================

from array import array


# ------------------------------------------------------------
# Display Array
# ------------------------------------------------------------

def display_array(arr):
    """Display all elements of the array."""

    if len(arr) == 0:
        print("\nArray is empty.")
    else:
        print("\nArray:", arr.tolist())


# ------------------------------------------------------------
# Insert Element
# ------------------------------------------------------------

def insert_element(arr):
    """Insert an element at a specific index."""

    value = int(input("Enter the element to insert: "))
    index = int(input("Enter the index: "))

    if 0 <= index <= len(arr):
        arr.insert(index, value)
        print(f"{value} inserted successfully at index {index}.")
    else:
        print("Invalid index!")


# ------------------------------------------------------------
# Delete Element
# ------------------------------------------------------------

def delete_element(arr):
    """Delete the first occurrence of an element."""

    if len(arr) == 0:
        print("\nArray is empty.")
        return

    value = int(input("Enter the element to delete: "))

    if value in arr:
        arr.remove(value)
        print(f"{value} deleted successfully.")
    else:
        print(f"{value} not found in the array.")


# ------------------------------------------------------------
# Search Element
# ------------------------------------------------------------

def search_element(arr):
    """Search an element using linear search."""

    if len(arr) == 0:
        print("\nArray is empty.")
        return

    value = int(input("Enter the element to search: "))

    for i in range(len(arr)):

        if arr[i] == value:
            print(f"{value} found at index {i}.")
            return

    print(f"{value} not found in the array.")


# ------------------------------------------------------------
# Update Element
# ------------------------------------------------------------

def update_element(arr):
    """Update an element at a specific index."""

    if len(arr) == 0:
        print("\nArray is empty.")
        return

    index = int(input("Enter the index to update: "))

    if 0 <= index < len(arr):

        new_value = int(input("Enter the new value: "))

        old_value = arr[index]

        arr[index] = new_value

        print(
            f"Element {old_value} at index {index} "
            f"updated to {new_value}."
        )

    else:
        print("Invalid index!")


# ============================================================
#                    MAIN PROGRAM
# ============================================================

print("=" * 55)
print("       ARRAY IMPLEMENTATION USING array()")
print("=" * 55)


# ------------------------------------------------------------
# Take Array Input from User
# ------------------------------------------------------------

n = int(input("Enter the number of elements: "))

arr = array('i')

print(f"Enter {n} integer elements:")

for i in range(n):

    value = int(input(f"Enter element {i + 1}: "))

    arr.append(value)


print("\nArray created successfully!")
print("Array:", arr.tolist())


# ============================================================
#                    MENU-DRIVEN PROGRAM
# ============================================================

while True:

    print("\n" + "=" * 55)
    print("                  ARRAY MENU")
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

        insert_element(arr)


    # --------------------------------------------------------
    # Delete
    # --------------------------------------------------------

    elif choice == 3:

        delete_element(arr)


    # --------------------------------------------------------
    # Search
    # --------------------------------------------------------

    elif choice == 4:

        search_element(arr)


    # --------------------------------------------------------
    # Update
    # --------------------------------------------------------

    elif choice == 5:

        update_element(arr)


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
