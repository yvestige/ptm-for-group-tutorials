def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)
    except FileNotFoundError:
        print("File not found.")


def write_file(filename):
    content = input("Enter content to write to the file: ")
    with open(filename, 'w') as file:
        file.write(content)
    print("Content successfully written to the file.")


def append_file(filename):
    content = input("Enter content to append to the file: ")
    with open(filename, 'a') as file:
        file.write(content)
    print("Content successfully appended to the file.")


def main():
    filename = input("Enter filename to work with: ")

    while True:
        print("\nMenu:")
        print("1. Read file")
        print("2. Write to file")
        print("3. Append to file")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            read_file(filename)
        elif choice == '2':
            write_file(filename)
        elif choice == '3':
            append_file(filename)
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
