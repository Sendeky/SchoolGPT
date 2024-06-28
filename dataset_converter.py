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
dat = """You will help me create a fine-tuning dataset for generating text to text prompts;

Prompt: "The British halted the implementation of home rule during WWII but resistance to Indian independence continued; After the war, the war-weary and economically weakened British government worked toward independence."

user_input: "Coming of self rule in India"

Prompt: "Gandhi and Nehru were initially against the idea of a divided and independent India, with Gandhi referring to it as "vivisection."; Communal violence between Hindus and Muslims had already become a major problem in parts of India leading up to partition and independence, fueled by propaganda campaigns and rumors about the consequences of remaining in the "wrong" state."

user_input: "Partition and violence in India during Indian independence movement"

Prompt: "The lack of clear boundaries for the new states and the mass migration of people seeking "safe" territory led to further violence and an estimated 10 million refugees, with between half a million to one million deaths"

user_input:"""


# regex parameters
regexp = r'^\* (.*)$'
regexopt = re.MULTILINE

matches = re.findall(regexp, data, regexopt)        # finds all regex matches

# goes over every match
for match in matches:
    
    # checks if text is longer than 10 characters, otherwise ignores
    if len(match) > 9:
        filtered_results.append(f"You will help me create a fine-tuning dataset for generating text to text prompts: \n user_input: {match} \n Prompt:")

# print(filtered_results)


client = OpenAI(
  organization= SECRETS.organization,
  project=SECRETS.project,
  api_key=SECRETS.key
)

for entry in filtered_results:
    print(entry)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": entry}],
        stream=False,
    )


result = response.choices[0].message.content
print(result)
print(response)
