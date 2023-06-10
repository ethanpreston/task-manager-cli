import subprocess


def get_user_input_with_vim():
    # Create a temporary file to store the user's input
    temp_file = '/tmp/user_input.txt'

    # Open the file in vim for the user to enter text
    subprocess.call(['vim', temp_file])

    # Read the contents of the file once vim is closed
    with open(temp_file, 'r') as file:
        user_input = file.read()

    # Remove the temporary file
    subprocess.call(['rm', temp_file])

    return user_input.strip()
