import json
import random

#Quiz:
def save_Quiz(content):
    with open("Quiz.json","w") as f :
        json.dump(content,f)
def load_Quiz():
    try:
        with open("Quiz.json","r") as f :
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
    
#score:
def save_score(s):
    with open("score_quiz.json","w") as f:
        json.dump(s,f)
def load_score():
    try:
        with open("score_quiz.json","r") as f:
            return json.load(f) 
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return [] 

class Quiz:
    def __init__(self,question,options,answer):
        self.question=question
        self.options=options
        self.answer=answer
        
    def add_question(self):
        Quizes=load_Quiz()
        Quizes.append({"Question":self.question,"Options":self.options,"Answer":self.answer})
        save_Quiz(Quizes)
        return ("Quiz added successfully")
    
def start_Quiz():
    Quizes=load_Quiz()
    random.shuffle(Quizes)
    if not Quizes :
        print("No Question found")
    else:
        score=0
        for i,quiz in enumerate(Quizes,start=1):
            print(f"\nQuestion {i}: {quiz['Question']}?")
            for index,option in enumerate(quiz["Options"],start=1):
                print(f"{index}.{option.strip()}")
            choice=int(input("Enter option number:"))
            ans=quiz["Options"][choice-1]
            if quiz["Answer"].lower().strip() == ans.lower().strip():
                print("correct answer !")
                score+=1
            else:
                print (f"Wrong answer! Correct answer: {quiz['Answer']}")

        scores=load_score()
        scores.append({"score":score,"Total":len(Quizes),"percentage": round((score/len(Quizes))*100, 2)})
        save_score(scores)
        print (f"Your score is {score} out of {len(Quizes)}")
    

def show_score_history():
    return load_score()

def show_all_questions():
    return load_Quiz()

def delete_Question(qsn):
    Quizes=load_Quiz()

    new_quiz=[]
    for quiz in Quizes:
        if quiz["Question"].lower().strip()!=qsn.lower().strip() :
            new_quiz.append(quiz)

    if len(new_quiz)==len(Quizes):
        return "Question not found"

    
    save_Quiz(new_quiz)
    return "Question deleted successfully"
    

def menu():
    while True:
        print("------Quiz menu-----")
        print("1.Add Question")
        print("2.Start Quiz")
        print("3.show score")
        print("4.Show all Question")
        print("5.delete Question")
        print("6.Exit")

        try:
            choice=int(input("Enter your preference:"))
        except ValueError:
            print("Invalid choice")
            continue
        if choice==1 :
            try:
                q=input("Enter Question:")
                ops=input("Enter options:").split(",")
                ans=input("Enter answer:")
                qu_iz=Quiz(q,ops,ans)
                print(qu_iz.add_question())
            except ValueError:
                print("Something went wrong , please try again")
        elif choice==2:
            start_Quiz()
        elif choice==3:
            print(show_score_history())
        elif choice==4 :
            print(show_all_questions())
        elif choice==5 :
            qsn=input("Enter the Question you want to delete:")
            print(delete_Question(qsn))
        elif choice==6 :
            print("Thank You")
            break
        else:
            print("You have entered a invalid choice")

menu()




    
