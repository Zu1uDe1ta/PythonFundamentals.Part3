
print("Choose a language? A. Spanish B. Portuguese C. Italian")
chosen_language = input()

def language_input(chosen_language):
    if chosen_language == "A":
        print("Cual es tu nombre?")
    elif chosen_language == "B":
        print("Qual e o seu nome?")
    elif chosen_language == "C":
        print("Come ti chiami?")
    else:
        print("Error")
language_input(chosen_language)

name = str(input())

def language_greeting(chosen_language):
    if chosen_language == "A":
        print("Hola " + name)
    elif chosen_language == "B":
        print("Ola " + name)
    elif chosen_language == "C":
        print("Ciao " + name)
language_greeting(chosen_language)
