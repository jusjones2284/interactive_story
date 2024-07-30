# with open("story.txt", "r") as f:
#     for line in f.readlines():
#         print(line)
    
start_of_word = -1
words = set()
target_start = "<"
target_end = ">"   
    
with open("story.txt", "r") as f: 
    story = f.read()
    
for i, char in enumerate(story):
    if char == target_start:
        start_of_word = 1
    
    if char == target_end and start_of_word != -1:
        word = story[start_of_word: i + 1]
        words.add(word)
        start_of_word = -1

answers = {}

for word in words:
    answers = input("Enter a word for " + word + ": ")
    answers[word] = answers
    

for word in words:
    story = story.replace(word, answers[word])
        

        

    