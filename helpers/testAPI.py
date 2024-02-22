import requests

url = "http://localhost:1234/v1/chat/completions"
headers = {
    "Content-Type": "application/json"
}

PROMPT = """
You are a helper that converts English words into ASL tokens. The following is a list of tokens: 
[I,Food,hungry,drink,eat,play,run,walk,tree,give,water,hot,cold,night,happy,sick, sad,around, today, sky, name, thankYou, good, healthy, morning, today, tonight, tomorrow, yesterday].

Sample input and output is provided.

The output format is "[output]"

Example 1:
input : I am hungry
Output : [I, Hungry]

Example 2:
input : it is cold tonight
Output : [Today, Night, Cold]

Example 3:
Input : did you complete your work?
Output : [You, Work, Done]

Example 4:
Input : It is healthy to drink hot water in the morning"
Output : [drink, water, morning, healthy]

Example 5: 
Input : water the tree tomorrow morning and eat food
Output : [water, tree, Tomorrow ,morning, eat, food ]

Generate only tokens.
"""

INPUT="Eat food and thank you"

data = {
    "messages": [
        {"role": "system", "content": PROMPT},
        {"role": "user", "content": "The input to be processed is : " + INPUT}
    ],
    "temperature": 0.85,
    "max_tokens": -1,
    "stream": False
}

response = requests.post(url, headers=headers, json=data)

print(response.text)
