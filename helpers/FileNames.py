import os

A = os.listdir('/Users/dhanush/Documents/D/college/sem8/project/Videos')

VIDEOS = [i[:-4] for i in A]

print(", ".join(VIDEOS))
print(len(VIDEOS))
