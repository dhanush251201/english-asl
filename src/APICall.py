# Example: reuse your existing OpenAI setup
from openai import OpenAI

# Point to the local server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

# INPUT = "I am thirsty, give me hot water"
def APICall(QUERY : str):
    PROMPT = """
    You are a helper that converts English words into ASL tokens. The following is a list of tokens:
    I,Food,hungry,drink,eat,play,run,walk,tree,give,water,hot,cold,night,happy,sick, sad,around, today,give, Thirsty,sky, name, thankYou, good, healthy, morning, today, tonight, tomorrow, yesterday
    Sample input and output is provided. Ensure to preserve the tense of the sentence and the person if it is first, second or third person
    The output format is "token1, token2, token3...."

    Example 1:
    input : I am hungry
    Output : I, Hungry

    Example 2:
    input : it is cold tonight
    Output : Today, Night, Cold

    Example 3:
    Input : did you complete your work?
    Output : You, Work, Done

    Example 4:
    Input : It is healthy to drink hot water in the morning"
    Output : drink, water, morning, healthy

    Example 5:
    Input : water the tree tomorrow morning and eat food
    Output : water, tree, Tomorrow, morning, eat, food

    Generate only tokens.
    """

    INPUT=f"""input text is " {QUERY} "
    convert this into ASL tokens
    """

    completion = client.chat.completions.create(
    model="local-model", # this field is currently unused
    messages=[
        {"role": "system", "content":PROMPT},
        {"role": "user", "content": INPUT}
    ],
    temperature=0.9,
    stream=False,
    )

    # print(completion.choices[0].message)

    X = (str(completion.choices[0].message.content)).split(",")
    LIST = [i.strip() for i in X]
    return(LIST)


# print(APICall(INPUT, client))
