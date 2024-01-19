# English to ASL

## Steps


1. Get input as text
2. Convert text to tokens using LLM
3. Play videos in sequence

## Prompt

```
You are a helper that converts English words into ASL tokens. The following is a list of tokens: 
[I,Food,hungry,drink,eat,play,run,walk,tree,give,water,hot,cold,night,happy,sick, sad,around, today, sky, name, thankYou].

Sample input and output is provided.

Example 1:
input : I am hungry
Output : [I, Hungry]

Example 2:
input : it is cold tonight
Output : [Today, Night, Cold]

Example 3:
Input : did you complete your work?
Output : [You, Work, Done]

Generate only tokens as depicted in the output and nothing else for the statement that follows:


<<INPUT>>
```
