#madlibs generator

with open("story.txt",'r') as f:
    story=f.read()

words=set()
word_start='['
word_end=']'
words_idx=-1

for i,char in enumerate(story):
    if char==word_start:
        words_idx=i

    if char==word_end and words_idx!=-1:
        word=story[words_idx:i+1]
        words.add(word)
        words_idx=-1
        
answers={} # key, value
for word in words:
    ans=input("enter your "+word+"term: ")
    answers[word]=ans
for word in words:
    story=story.replace(word,answers[word])
print(story)
    
    