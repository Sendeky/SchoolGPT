# function to convert the chatgpt prompt output to a training csv
import csv


def convert_training_csv(input_arr: list):
    # array that holds prompts and user inputs that we feed to csv
    prompts_user_inputs = []

    # Iterate through new_arr by 2 to put prompts and user_inputs into array
    for i in range(0, len(input_arr), 2):
        prompt = input_arr[i]
        user_input = input_arr[i + 1]
        prompts_user_inputs.append([prompt, user_input])

    # Define the CSV file path
    csv_file_path = 'prompts_user_inputs.csv'

    # Write data to the CSV file
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Prompt', 'User Input'])  # Write the header row
        writer.writerows(prompts_user_inputs)  # Write the data rows

    print(f'Data has been written to {csv_file_path}')