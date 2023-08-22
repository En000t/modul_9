def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Invalid input"
    return wrapper

contacts = {}

@input_error
def add_contact(command):
    _, name, phone = command.split()
    contacts[name] = phone
    return f"Added {name} with phone number {phone}"

@input_error
def change_contact(command):
    _, name, phone = command.split()
    contacts[name] = phone
    return f"Changed phone number for {name} to {phone}"

@input_error
def show_phone(command):
    _, name = command.split()
    return f"Phone number for {name}: {contacts[name]}"

def show_all_contacts():
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def main():
    while True:
        user_input = input("Enter a command: ").lower()
        if user_input == "good bye" or user_input == "close" or user_input == "exit":
            print("Good bye!")
            break
        elif user_input == "hello":
            print("How can I help you?")
        elif user_input.startswith("add"):
            response = add_contact(user_input)
            print(response)
        elif user_input.startswith("change"):
            response = change_contact(user_input)
            print(response)
        elif user_input.startswith("phone"):
            response = show_phone(user_input)
            print(response)
        elif user_input == "show all":
            all_contacts = show_all_contacts()
            print("All contacts:\n" + all_contacts)
        else:
            print("Unknown command")

if __name__ == "__main__":
    main()
