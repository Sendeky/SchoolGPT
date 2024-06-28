import re
from  openai import OpenAI
import SECRETS

filtered_results = []


data = """APWH Chapter 25 Notes
Independence in Asia
India’s partitioned independence
The coming of Self Rule:
* The British halted the implementation of home rule during WWII but resistance to Indian independence continued; After the war, the war-weary and economically weakened British government worked toward independence.
* The issue of Muslim separatism grew in importance as Indian independence became more certain; The Muslim League, led by Muhammad Ali Jinnah, called for a separate Muslim state in August 1946, leading to the Great Calcutta Killing and further fueling communal feelings.
Partition and Violence:
* Gandhi and Nehru were initially against the idea of a divided and independent India, with Gandhi referring to it as "vivisection."; Communal violence between Hindus and Muslims had already become a major problem in parts of India leading up to partition and independence, fueled by propaganda campaigns and rumors about the consequences of remaining in the "wrong" state.
* The lack of clear boundaries for the new states and the mass migration of people seeking "safe" territory led to further violence and an estimated 10 million refugees, with between half a million to one million deaths
* Despite the tragic violence, Indian independence marked a significant turning point for decolonization, inspiring anti-imperial movements throughout Asia and Africa, and Nehru's promotion of nonalignment as a compelling strategy for newly independent nations caught in the Cold War.
Nonalignment:
* Nonalignment was a strategy promoted by India's first president, Nehru, in the Cold War era; Nonalignment aimed to maintain formal neutrality and avoid choosing sides between the United States and the Soviet Union.
* The idea of nonalignment was discussed by leaders of new African and Asian countries at the Bandung Conference in 1955.
* The Nonaligned Movement, which held occasional meetings for member countries to discuss common interests, suffered from a lack of unity and many member states maintained close ties with one of the Cold War superpowers.
Pakistan:
# * H"""

dat = """You will help me create a fine-tuning dataset for generating text to text prompts. I have given you the "Prompt" and need you to generate a "user_input" that could fit the prompt. Provide just the "user_input" part and please number the inputs if there are more than one. Keep it concise and not too complicated:
Prompt: The British halted the implementation of home rule during WWII but resistance to Indian independence continued; After the war, the war-weary and economically weakened British government worked toward independence.
user_input:
Prompt: The issue of Muslim separatism grew in importance as Indian independence became more certain; The Muslim League, led by Muhammad Ali Jinnah, called for a separate Muslim state in August 1946, leading to the Great Calcutta Killing and further fueling communal feelings.
user_input:
Prompt: Gandhi and Nehru were initially against the idea of a divided and independent India, with Gandhi referring to it as "vivisection."; Communal violence between Hindus and Muslims had already become a major problem in parts of India leading up to partition and independence, fueled by propaganda campaigns and rumors about the consequences of remaining in the "wrong" state.
user_input:
Prompt: The lack of clear boundaries for the new states and the mass migration of people seeking "safe" territory led to further violence and an estimated 10 million refugees, with between half a million to one million deaths
user_input:
Prompt: Despite the tragic violence, Indian independence marked a significant turning point for decolonization, inspiring anti-imperial movements throughout Asia and Africa, and Nehru's promotion of nonalignment as a compelling strategy for newly independent nations caught in the Cold War.
user_input:
Prompt: Nonalignment was a strategy promoted by India's first president, Nehru, in the Cold War era; Nonalignment aimed to maintain formal neutrality and avoid choosing sides between the United States and the Soviet Union.
user_input:
Prompt: The idea of nonalignment was discussed by leaders of new African and Asian countries at the Bandung Conference in 1955.
user_input: The Nonaligned Movement, which held occasional meetings for member countries to discuss common interests, suffered from a lack of unity and many member states maintained close ties with one of the Cold War superpowers.
Prompt: Vietnamese anticolonial activists fought against French rule in Indochina, and the Indochinese Communist Party was among the groups fighting to drive out the French.
user_input:
Prompt: Ho Chi Minh, who would become the first president of North Vietnam, returned to Indochina in 1940 to coordinate a resistance movement against the Japanese and worked with U.S. operatives to undermine their common enemy.
user_input:
Prompt: By 1945, Ho and his party issued the Vietnamese Declaration of Independence and proclaimed Vietnam an independent republic, but the French sought to reclaim their imperial possessions and war broke out between the French and the Vietnamese communist forces of the north.
user_input:"""


# regex parameters
regexp = r'^\* (.*)$'
regexopt = re.MULTILINE

matches = re.findall(regexp, data, regexopt)        # finds all regex matches


filtered_results.append('You will help me create a fine-tuning dataset for generating text to text prompts. I have given you the "Prompt" and need you to generate a "user_input" that could fit the prompt. The user_input should be one that a person would enter either as a question or as a topic that would lead to the prompt. The prompts are academic and the user_input should have a slight hint of that too. Provide just the "user_input" part and please number the inputs if there are more than one. Keep it concise and not too complicated: \n') 
# goes over every match
for match in matches:
    
    # checks if text is longer than 10 characters, otherwise ignores
    if len(match) > 9:
        filtered_results.append(f"Prompt: {match}")
        filtered_results.append("\n")
        filtered_results.append("user_input:")
        filtered_results.append("\n")

# print(filtered_results)
filtered_results = ''.join(filtered_results)
print(filtered_results)


client = OpenAI(
  organization= SECRETS.organization,
  project=SECRETS.project,
  api_key=SECRETS.key
)

# for entry in filtered_results:
# print(entry)
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": filtered_results}],
    stream=False,
    temperature=0.4
)


result = response.choices[0].message.content
# print(result)
# print(response)


# result = 1. The Muslim League's call for a separate Muslim state in 1946 heightened tensions and led to communal violence.
# 2. Gandhi and Nehru opposed the idea of a divided India, fearing the consequences of partition.
# 3. The mass migration of people seeking safety during partition resulted in widespread violence and millions of refugees.
# 4. Indian independence inspired anti-imperial movements in Asia and Africa.
# 5. Nonalignment was a strategy to maintain neutrality during the Cold War.
# 6. The Nonaligned Movement faced challenges due to lack of unity among member states.
# 7. Vietnamese anticolonial activists fought against French rule in Indochina.
# 8. Ho Chi Minh coordinated a resistance movement against the Japanese and worked with U.S. operatives.


# regex parameters
regexp2 = r'^\d+\.\s(.+)$'
regexopt2 = re.MULTILINE

matchesss = re.findall(regexp2, result, regexopt2)        # finds all regex matches

print("matches:", matchesss)
