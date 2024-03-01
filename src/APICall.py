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
    You will be given an English sentence. You must convert it into tokens.
    The following are a few examples of how to do the same.
    Example 1
    input : "How are you"
    output : "How, are, you"
    Example 2
    input : "I am hungry"
    output : "I, hungry"
    Example 3
    input : "Water the plants"
    output : "water, plant"
    Example 4
    input : "I am feeling hot"
    output : "I, feel, hot"
    Example 5
    input : "Invite your friends to the party"
    output : "invite, friend, to, party"
    Example 6
    input : "Can I have mushroom and pumpkin soup"
    output : "I, want, mushroom, pumpkin, soup"
    Example 7
    input : "Let us plan for a movie tonight"
    output : "Let, us, plan, for, a, movie, tonight"
    Example 8
    input : "Would you like a coffee"
    output "how, about, a, coffee"
    Example 9
    input : "Plan your day ahead for better result"
    output : "Plan, your, day, ahead, for, better, result"
    Example 10
    input : "Car race is my favourite sport"
    output : "I, love, car, race"
    Using the above examples as reference, for any given user input generate the ASL Tokens ONLY.
    """

    # ---------------------------------------------------------- #
    # User Input is added to the request payload
    # ---------------------------------------------------------- #

    # ---------------------------------------------------------- #
    # The actual call to the LLM server
    # ---------------------------------------------------------- #

    completion = client.chat.completions.create(
    model="local-model", # this field is currently unused
    messages=[
        {"role": "system", "content":PROMPT},
        {"role": "user", "content": QUERY}
    ],
    temperature=0.1,
    stream=False,
    )

    # ---------------------------------------------------------- #
    # Response Processing and returning a list of tokens
    # ---------------------------------------------------------- #

    X = (str(completion.choices[0].message.content)).split(",")
    LIST = [i.strip() for i in X]
    return(LIST)
