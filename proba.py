def analyze_password_probabilities(file_path):
    password_counts = {}
    total_count = 0

    # Read passwords and count frequencies
    with open(file_path, 'r') as file:
        for line in file:
            password = line.strip()
            if password:
                password_counts[password] = password_counts.get(password, 0) + 1
                total_count += 1

    # Find the key with the maximum value (most repetitions)
    max_key = max(password_counts, key=password_counts.get)

    # Get the count of this key (number of repetitions)
    max_count = password_counts[max_key]

    print(f"The most frequent password is '{max_key}' and it appears {max_count} times.")
    print("The probability over the set is", max_count / total_count)

    # Dictionary to hold the frequency of each count
    frequency_of_counts = {}

    # Counting the frequency of each count
    for count in password_counts.values():
        if count in frequency_of_counts:
            frequency_of_counts[count] += 1
        else:
            frequency_of_counts[count] = 1

    # Finding the passwords that appear exactly twice
    # passwords_appear_twice = [password for password, count in password_counts.items() if count == 2]

    # Number of passwords that appear exactly twice
    num_passwords_twice = frequency_of_counts.get(2, 0)
    print(num_passwords_twice)

    # Calculate and print probabilities
    # for password, count in password_counts.items():
    #     probability = count / total_count
        # print(f"Password: {password}, Probability: {probability:.10f}")


# Example usage
file_path = 'generated_passwords.txt'  # Replace with your file path
analyze_password_probabilities(file_path)

