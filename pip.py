
from tkinter import*
import requests
import random
Cor = 0
Incor = 0

print()

window = Tk()
window.geometry("720x960")
def getQuiz():
    global a, b, c, d, e, f
    response = requests.get(f"https://opentdb.com/api.php?amount=1&type=multiple")
    if response.status_code != 200:
        return None
    
    data = response.json()
    result = data["results"][0]

    question = result["question"]
    correct = result["correct_answer"]
    incorrect = result["incorrect_answers"]

    choices = [correct, incorrect[0], incorrect[1], incorrect[2]]
    a = random.choice(choices)
    choices.remove(a)
    b = random.choice(choices)
    choices.remove(b)
    c = random.choice(choices)
    choices.remove(c)
    d = random.choice(choices)
    choices.remove(d)
    choices = [correct, incorrect[0], incorrect[1], incorrect[2]]
    e = question
    f = correct

    return question, correct, incorrect

     
question, correct, incorrect = getQuiz()

print("Question →", question)
print("Correct Answer →", correct)
print("Incorrect Answers →", incorrect)


def load():
    question_label.config(text=e)
    answer_button1.config(text=a)
    answer_button2.config(text=b)
    answer_button3.config(text=c)
    answer_button4.config(text=d)


def check(choice):
    global Cor, Incor
    if choice == f:
        Check.config(text="Correct!")
        Cor += 1

    elif choice != f:
        Check.config(text=f"Incorrect! The answer was {f}")
        Incor += 1
        
    Record.config(text=f"Correct: {Cor}   Incorrect: {Incor}")
    getQuiz()
    load()
    
        





question_label = Label(window, text=question, wraplength=350, font=("Arial", 16))
question_label.pack(pady=20)

answer_button1 = Button(
    window,
    text=a,
    font=("Arial", 14),
    width=20,
    height=2,
    command= lambda x = a: check(x)
)
answer_button1.pack(pady=20)



answer_button2 = Button(
    window,
    text=b,
    font=("Arial", 14),
    width=20,
    height=2,
    command= lambda x = b: check(x)
)
answer_button2.pack(pady=20)



answer_button3 = Button(
    window,
    text=c,
    font=("Arial", 14),
    width=20,
    height=2,
    command= lambda x = c: check(x)
)
answer_button3.pack(pady=20)



answer_button4 = Button(
    window,
    text=d,
    font=("Arial", 14),
    width=20,
    height=2,
    command= lambda x = d: check(x)
)
answer_button4.pack(pady=20)



Check = Label(window, text="", wraplength=350, font=("Arial", 16))
Check.pack(pady=20)

Record = Label(window, text=f"Correct: {Cor}   Incorrect: {Incor}", wraplength=350, font=("Arial", 16))
Record.pack(pady=20)


window.resizable(False, False)
window.mainloop()














""" 
from tkinter import*
import requests


window = Tk()
window.geometry("720x960") #Dimensions
def getPoke(poke):
     response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{poke.lower()}") #Dictionary the resposne pulls from
     if response.status_code != 200: #Status code, check if valid
        return None
     
     data = response.json() #Opens file
     return {
          "Name": data["name"],
          "Height": data["height"],
          "Weight": data["weight"],
          "Types": [t["type"]["name"] for t in data["types"]]
     }

def findPokemon():
    poke_name = entry.get()
    pokemon = getPoke(poke_name)
    if pokemon:
        result_text = "" #Clears output
        for key, value in pokemon.items():
            if isinstance(value, list):
                value = ", ".join(value)  # convert list to string
            result_text += f"{key} → {value}\n" #Makes it look cooler
        output_label.config(text=result_text) #configures output text
    else:
        output_label.config(text="Pokémon not found!") #configures output text


label = Label(window, text="Enter Pokémon Name:", font=("Arial", 18)) #labels textbox
label.pack(pady=10)

entry = Entry(window, font=("Arial", 16), width=20) #textbox 
entry.pack(pady=5) 

button = Button(window, text="Search", font=("Arial", 16), command=findPokemon) #button
button.pack(pady=10) 

output_label = Label(window, text="", font=("Arial", 30), justify=LEFT) #Output
output_label.pack(pady=20)

window.resizable(False, False) #No Resize



window.mainloop() #To start application

 """