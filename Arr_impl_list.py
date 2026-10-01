# ============================================================
#          ARRAY IMPLEMENTATION USING PYTHON LIST
#                    MENU-DRIVEN PROGRAM
# ============================================================


def display_array(arr):
    """Display all elements of the array."""
    if not arr:
        print("\nArray is empty.")
    else:
        print("\nArray:", arr)


def insert_element(arr):
    """Insert an element at a specific index."""
    value = int(input("Enter the element to insert: "))
    index = int(input("Enter the index: "))

    if 0 <= index <= len(arr):
        arr.insert(index, value)
        print(f"{value} inserted successfully at index {index}.")
    else:
        print("Invalid index!")


def delete_element(arr):
    """Delete an element by value."""
    if not arr:
        print("\nArray is empty.")
        return

    value = int(input("Enter the element to delete: "))

    if value in arr:
        arr.remove(value)
        print(f"{value} deleted successfully.")
    else:
        print(f"{value} not found in the array.")


def search_element(arr):
    """Search for an element and display its index."""
    if not arr:
        print("\nArray is empty.")
        return

    value = int(input("Enter the element to search: "))

    index = -1

    for i in range(len(arr)):
        if arr[i] == value:
            index = i
            break

    if index != -1:
        print(f"{value} found at index {index}.")
    else:
        print(f"{value} not found in the array.")


def update_element(arr):
    """Update an element at a specific index."""
    if not arr:
        print("\nArray is empty.")
        return

    index = int(input("Enter the index to update: "))

    if 0 <= index < len(arr):
        value = int(input("Enter the new value: "))

        old_value = arr[index]
        arr[index] = value

        print(
            f"Element {old_value} at index {index} "
            f"updated to {value}."
        )
    else:
        print("Invalid index!")


# ============================================================
#                       MAIN PROGRAM
# ============================================================

arr = []
n=int(input("Enter the number of elements in the array :"))
for i in range(n):
    element=int(input(f"Enter the element  {i+1} :"))
    arr.append(element)

while True:

    print("\n" + "=" * 45)
    print("        ARRAY IMPLEMENTATION MENU")
    print("=" * 45)

    print("1. Display Array")
    print("2. Insert Element")
    print("3. Delete Element")
    print("4. Search Element")
    print("5. Update Element")
    print("6. Exit")

    print("=" * 45)

    choice = int(input("Enter your choice: "))

    if choice == 1:
        display_array(arr)

    elif choice == 2:
        insert_element(arr)

    elif choice == 3:
        delete_element(arr)

    elif choice == 4:
        search_element(arr)

    elif choice == 5:
        update_element(arr)

    elif choice == 6:
        print("\nProgram terminated successfully.")
        break

    else:
        print("\nInvalid choice! Please enter a number between 1 and 6.")