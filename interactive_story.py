# with open("story.txt", "r") as f:
#     for line in f.readlines():
#         print(line)
    
start_of_word = -1

target_start = "<"
target_end = ">"   
    
with open("story.txt", "r") as f: 
    story = f.read()
    
print(story[1:5])
for i, char in enumerate(story):
    if char == target_start:
        start_of_word = 1
        

        

    