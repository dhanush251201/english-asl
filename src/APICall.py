from openai import OpenAI

# ---------------------------------------------------------- #
# Point to the local server
# ---------------------------------------------------------- #

client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")


def APICall(QUERY : str) -> list:

    # ---------------------------------------------------------- #
    # The prompt used to
    # ---------------------------------------------------------- #

    PROMPT = """
    You are a helper that converts English words into ASL tokens.
    Sample input and output is provided. Ensure to preserve the tense of the sentence and the person if it is first, second or third person. Also covert all words  to the root like saying to say, laying to lay, saving to save, etc.
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

    Example 6:
    Input : I like walking
    Output : i, like, walk

    Example 7:
    Input : I like to watch car race
    Output : i, like, watch, car, race


    Generate only tokens.
    """

    # ---------------------------------------------------------- #
    # User Input is added to the request payload
    # ---------------------------------------------------------- #

    INPUT = f"""input text is " {QUERY} "
    convert this into ASL tokens
    """

    # ---------------------------------------------------------- #
    # The actual call to the LLM server
    # ---------------------------------------------------------- #

    completion = client.chat.completions.create(
    model="local-model", # this field is currently unused
    messages=[
        {"role": "system", "content":PROMPT},
        {"role": "user", "content": INPUT}
    ],
    temperature=0.9,
    stream=False,
    )

    # ---------------------------------------------------------- #
    # Response Processing and returning a list of tokens
    # ---------------------------------------------------------- #

    X = (str(completion.choices[0].message.content)).split(",")
    LIST = [i.strip() for i in X]
    return(LIST)
