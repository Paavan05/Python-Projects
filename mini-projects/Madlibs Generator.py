with open("story.txt","r") as f:
    story = f.read()
    
words = set()
target_start = "<"
target_end = ">"

start_of_word = -1

for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i
        
    if char == target_end and start_of_word != -1:
        words.add(story[start_of_word : i + 1])
        start_of_word == -1
    
answers = {}

for word in words:
    answer = input("enter a word for " + word + ": ")
    answers[word] = answer
    
for word in words:
    story = story.replace(word, answers[word])

print(story)