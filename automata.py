import Package.DFAVerificator as DFA
import os
import time


def main():
    os.system("cls")
    time.sleep(.5)
    option = int(input("What is the DFA you want use (1, 2, 3, 4, 5(exit)) ?\n"))
    if option == 1:
        os.system("cls")
        DFA1()
    elif option == 2:
        os.system("cls")
        DFA2()
    elif option == 3:
        os.system("cls")
        DFA3()
    elif option == 4:
        os.system("cls")
        DFA4()
    elif option == 5:
        return
    else:
        main()


def DFA1():
    states = {0, 1, 2, 3}
    alphabet = {'a', 'b', 'c'}
    transitions = {
        (0, 'a'): 1, (0, 'b'): 2, (0, 'c'): 3,
        (1, 'a'): 2, (1, 'b'): 3, (1, 'c'): 1,
        (2, 'a'): 3, (2, 'b'): 1, (2, 'c'): 3,
        (3, 'a'): 3, (3, 'b'): 3, (3, 'c'): 3,
    }
    start_state = 0
    final_state = {3}
    word_to_check = input("Write the word you want to verify for Automata 1: \n")
    dfa = DFA.DFA(states, alphabet, transitions, start_state, final_state)
    if dfa.is_correct(word_to_check):
        print(word_to_check + " is correct.")
    else:
        print(word_to_check + " is not correct.")

    answer = input("Want to try it again with the same automata? (yes, no)\n")
    if answer == 'yes':
        os.system("cls")
        DFA1()
    elif answer == 'no':
        main()
    else:
        return


def DFA2():
    states = {0, 3, 4, 6, 8}
    alphabet = {'a', 'b', 'c'}
    transitions = {
        (0, 'a'): 4, (0, 'b'): 3, (0, 'c'): 3,
        (3, 'a'): 3, (3, 'b'): 3, (3, 'c'): 3,
        (4, 'a'): 4, (4, 'b'): 8, (4, 'c'): 3,
        (6, 'a'): 3, (6, 'b'): 8, (6, 'c'): 3,
        (8, 'a'): 3, (8, 'b'): 6, (8, 'c'): 3,
    }
    start_state = 0
    final_state = {3, 4, 6, 8}
    word_to_check = input("Write the word you want to verify for Automata 2: \n")
    dfa = DFA.DFA(states, alphabet, transitions, start_state, final_state)
    if dfa.is_correct(word_to_check):
        print(word_to_check + " is correct.")
    else:
        print(word_to_check + " is not correct.")

    answer = input("Want to try it again with the same automata? (yes, no)\n")
    if answer == 'yes':
        os.system("cls")
        DFA2()
    elif answer == 'no':
        main()
    else:
        return


def DFA3():
    states = {0, 7, 8, 4}
    alphabet = {'a', 'b', 'c'}
    transitions = {
        (0, 'a'): 7,
        (7, 'a'): 7, (7, 'b'): 8,
        (8, 'b'): 8, (8, 'c'): 4,
        (4, 'b'): 8
    }
    start_state = 0
    final_state = {7, 8}
    word_to_check = input("Write the word you want to verify for Automata 3: \n")
    dfa = DFA.DFA(states, alphabet, transitions, start_state, final_state)
    if dfa.is_correct(word_to_check):
        print(word_to_check + " is correct.")
    else:
        print(word_to_check + " is not correct.")

    answer = input("Want to try it again with the same automata? (yes, no)\n")
    if answer == 'yes':
        os.system("cls")
        DFA3()
    elif answer == 'no':
        main()
    else:
        return


def DFA4():
    states = {0, 10}
    alphabet = {'c', 'f'}
    transitions = {
        (0, 'f'): 10,
        (10, 'c'): 0
    }
    start_state = 0
    final_state = {10}
    word_to_check = input("Write the word you want to verify for Automata 4: \n")
    dfa = DFA.DFA(states, alphabet, transitions, start_state, final_state)
    if dfa.is_correct(word_to_check):
        print(word_to_check + " is correct.")
    else:
        print(word_to_check + " is not correct.")

    answer = input("Want to try it again with the same automata? (yes, no)\n")
    if answer == 'yes':
        os.system("cls")
        DFA4()
    elif answer == 'no':
        main()
    else:
        return


print("Deterministic Finite Automatas Verifier")
print("------------------------------------------------------------------")
main()
