print("Welcome to the File Read & Write Program!")

# file name
input_file = input("Please enter the name of the file you want to read: ")
output_file = "modified_" + input_file  # New file to save modified content

try:
    # Open and read the file
    with open(input_file, "r", encoding="utf-8") as f:
        content = f.readlines()
    print(f"Successfully read '{input_file}'!")

    # convert all text to uppercase
    modified_content = [line.upper() for line in content]

    # Write the modified content to a new file
    with open(output_file, "w", encoding="utf-8") as f:
        f.writelines(modified_content)
    print(f"Modified content has been saved to '{output_file}'.")

except FileNotFoundError:
    print(f"Oops! The file '{input_file}' does not exist. Please check the name and try again.")
except PermissionError:
    print(f"Sorry, you don't have permission to read '{input_file}'.")
except Exception as e:
    print(f"Something went wrong: {e}")

print("Program finished. Thank you for using it!")