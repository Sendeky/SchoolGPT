import re
from  openai import OpenAI
import SECRETS
from convert_training_csv import convert_training_csv


# Read the text file
with open('./data/notes1.txt', 'r') as file:
    data = file.read()

# Extract sentences after asterisks
pattern = r'^\* (.+)$'
matches = re.findall(pattern, data, re.MULTILINE)

# Initialize the single string with the custom sentence
custom_sentence = 'You are an assistant that makes up user_inputs for every given prompt. You will help me create a fine-tuning dataset for generating text to text prompts. I have given you mutliple "Prompts" and you need to generate a "user_input" for each that could fit the "Prompts". The user_input should be one that a person would enter either as a question or as a topic that would lead to the prompt. The prompts are academic and the user_input should have a slight hint of that too. PLEASE TRY to come up with a "user_input" for every prompt, it is okay if they are not perfect, we are all just doing our best here. PLEASE MAKE A "user_input: " FOR EVERY "Prompt". Come up with a "user_input" for every numbered "Prompt" and number the "user_input" according to the "Prompt". Provide just the "user_input" part and please number the inputs if there are more than one. Keep it concise and not too complicated: \n Heres an example to help you: \n Prompt: British halted the implementation of home rule during WWII but resistance to Indian independence continued; After the war, the war-weary and economically weakened British government worked toward independence \n user_input: "How did World War II impact British policies on Indian home rule?"\n '

formatted_text = custom_sentence

# Format the sentences and add to the single string
counter = 1
for match in matches:
    formatted_text += f"{counter}. Prompt: {match}\n"
    formatted_text += f"{counter}. user_input:\n"
    counter += 1

# Print the final single string
print(formatted_text)


client = OpenAI(
  organization= SECRETS.organization,
  api_key=SECRETS.key
)


response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": formatted_text}],
    stream=False,
    temperature=0.1
)

print("response: ", response)
print("content: ", response.choices[0].message.content)
print("tokens: ", response.usage)                                                                                                                              

result = response.choices[0].message.content


# regex parameters
regexp2 = r'"([^"]+)"'      # matches everything inside double quotes
regexopt2 = re.MULTILINE

matchesss = re.findall(regexp2, result, regexopt2)        # finds all regex matches

print("matches:", matchesss)

"""
new_arr = []

for match in matches:
    for match2 in matchesss:
        new_arr.append(match)
        new_arr.append(match2)

print('new_arr:', new_arr)

# convert the chatgpt array into a trainable csv
convert_training_csv(new_arr)
"""