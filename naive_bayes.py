import math

with open("nice_messages.txt", "r") as file:
    training_array_of_nice_messages = [line.strip() for line in file.readlines()]

with open("mean_messages.txt", "r") as file:
    training_array_of_mean_messages = [line.strip() for line in file.readlines()]

map_of_frequency_of_words_in_nice_messages = {}

for message in training_array_of_nice_messages:
    for word in message.lower().replace("!", "").replace(".", "").split():
        map_of_frequency_of_words_in_nice_messages[word] = map_of_frequency_of_words_in_nice_messages.get(word, 0) + 1

map_of_frequency_of_words_in_mean_messages = {}

for message in training_array_of_mean_messages:
    for word in message.lower().replace("!", "").replace(".", "").split():
        map_of_frequency_of_words_in_mean_messages[word] = map_of_frequency_of_words_in_mean_messages.get(word, 0) + 1


prior_probability_of_nice_message = len(training_array_of_nice_messages) / (len(training_array_of_nice_messages) + len(training_array_of_mean_messages))
prior_probability_of_mean_message = len(training_array_of_mean_messages) / (len(training_array_of_nice_messages) + len(training_array_of_mean_messages))
total_number_of_nice_nice_words = sum(map_of_frequency_of_words_in_nice_messages.values())
total_number_of_mean_words = sum(map_of_frequency_of_words_in_mean_messages.values())

def is_message_nice(message):
    """
    This function takes a message as input and returns True if the message is nice, and False if it is mean.
    """

    words = message.lower().replace("!", "").replace(".", "").split()

    probability_of_nice_message = 1
    probability_of_mean_message = 1

    for word in words:
        probability_of_nice_message *= (map_of_frequency_of_words_in_nice_messages.get(word, 0) + 1) / total_number_of_nice_nice_words
        probability_of_mean_message *= (map_of_frequency_of_words_in_mean_messages.get(word, 0) + 1) / total_number_of_mean_words
    
    probability_of_nice_message *= prior_probability_of_nice_message
    probability_of_mean_message *= prior_probability_of_mean_message

    # print(f"Probability of nice message: {probability_of_nice_message}")
    # print(f"Probability of mean message: {probability_of_mean_message}")

    if probability_of_nice_message > probability_of_mean_message:
        return True
    else:
        return False
    
if __name__ == "__main__":

    print("Testing the model with test_nice_messages.txt")
    with open("test_nice_messages.txt", "r") as file:
        test_messages = [line.strip() for line in file.readlines()]
    percent_correct = 0
    for i in range(len(test_messages)):
        message = test_messages[i]
        result = is_message_nice(message)
        if result == True:
            # print(f"Correct!")
            percent_correct += 1
        # else:
        #     print(f"Incorrect!")
    percent_correct = percent_correct / len(test_messages) * 100
    rounded_percent_correct = round(percent_correct, 2)
    print(f"Percent correct: {rounded_percent_correct}%")

    print("Testing the model with test_mean_messages.txt")
    with open("test_mean_messages.txt", "r") as file:
        test_messages = [line.strip() for line in file.readlines()]
    percent_correct = 0
    for i in range(len(test_messages)):
        message = test_messages[i]
        result = is_message_nice(message)
        if result == False:
            # print(f"Correct!")
            percent_correct += 1
        # else:
            # print(f"Incorrect!")
    percent_correct = percent_correct / len(test_messages) * 100
    rounded_percent_correct = round(percent_correct, 2)
    print(f"Percent correct: {rounded_percent_correct}%")