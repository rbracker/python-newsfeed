def decode(message_file):
    # Read the lines from the input file
    with open(message_file, "r") as f:
        lines = f.readlines()

    # Initialize an empty dictionary to store the message words
    message_dict = {}

    # Process each line
    for line in lines:
        number, word = line.split()
        message_dict[int(number)] = word

    # Create a list of pyramid numbers
    pyramid_numbers = []
    i = 1
    while i <= len(message_dict):
        pyramid_numbers.append(i)
        i += len(pyramid_numbers) + 1

    # Use the pyramid numbers to select the corresponding words
    message_words = [message_dict[number] for number in pyramid_numbers]

    # Join the message words with spaces and return the result
    return " ".join(message_words)

# Example usage
decoded_message = decode("coding_qual_input.txt")
print(decoded_message)