while True:
    file_name = input("File name: ")
    try:
        with open (file_name, "r") as file:
            file_data = file.read()
        print(file_data)
        break
    except FileNotFoundError:
        print("File not found.")
    except Exception:
        print("Something went wrong, let's try again:")