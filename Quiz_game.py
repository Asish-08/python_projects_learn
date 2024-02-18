print("hello , welcome to the quiz")
print("want to play the quiz?")
play=input()
if play.lower()!='yes':
    quit()
else:
    score=0
    print("what is the date of independence in India?")
    q1=input()
    if q1!='15/08/1947':
        print('wrong')
    else:
        score=+1
    print("who is the father of the nation?")
    q2=input()
    if q2.lower()!='mahatma gandhi':
        print('wrong')
    else:
        score=score+1
    print("who is the first prime minister of India?")
    q3=input()
    if q3.lower()!="jawaharlal nehru":
        print('wrong')
    else:
        score=score+1
    print("your score is :", score)
    print("End of the quiz!")
    print("you got ", (score/3)*100,"percentage")