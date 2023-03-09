import Package.DFAVerificator as DFA
import os
import time


def main():
    time.sleep(.5)
    option = int(input("What is the DFA you want use (1, 2, 3, 4, 5, 6, 7, or 8(exit)) ?\n DFA: "))
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
        os.system("cls")
        DFA5()
        return
    elif option == 6:
        os.system("cls")
        DFA6()
    elif option == 7:
        os.system("cls")
        DFA7()
    elif option == 8:
        return
    else:
        os.system("cls")
        main()


def DFA1():
    states = {1, 2, 3, 4, 5, 6}
    alphabet = {'0', '1'}
    transitions = {
        (1, '0'): 2,
        (2, '0'): 2, (2, '1'): 3,
        (3, '0'): 3, (3, '1'): 4,
        (4, '0'): 5,
        (5, '0'): 5, (5, '1'): 6,
    }
    start_state = 1
    final_state = {6}
    word_to_check = input("Write the word you want to verify for Automata 1: \n word: ")
    dfa = DFA.DFA(states, alphabet, transitions, start_state, final_state)
    if dfa.is_correct(word_to_check):
        print(word_to_check + " is correct.")
    else:
        print(word_to_check + " is not correct.")

    answer = input("Want to try it again with the same automata? (yes, no)\n answer: ")
    if answer == 'yes':
        os.system("cls")
        DFA1()
    elif answer == 'no':
        os.system("cls")
        main()
    else:
        return


def DFA2():
    states = {1, 2, 3, 4}
    alphabet = {'0', '1', ' '}
    transitions = {
        (1, '0'): 1, (1, '1'): 2,
        (2, '0'): 2, (2, '1'): 3, (2, ' '): 1,
        (3, '0'): 4, (3, '1'): 3
    }
    start_state = 1
    final_state = {4}
    word_to_check = input("Write the word you want to verify for Automata 2 (use space for empty string): \n word: ")
    dfa = DFA.DFA(states, alphabet, transitions, start_state, final_state)
    if dfa.is_correct(word_to_check):
        print(word_to_check + " is correct.")
    else:
        print(word_to_check + " is not correct.")

    answer = input("Want to try it again with the same automata? (yes, no)\n answer: ")
    if answer == 'yes':
        os.system("cls")
        DFA2()
    elif answer == 'no':
        os.system("cls")
        main()
    else:
        return


def DFA3():
    states = {1, 2, 3}
    alphabet = {'a', 'b', ' '}
    transitions = {
        (1, 'a'): 2, (1, ' '): 3,
        (2, 'a'): 2, (2, 'b'): 3,
        (3, ' '): 1
    }
    start_state = 1
    final_state = {3}
    word_to_check = input("Write the word you want to verify for Automata 3 (use space for empty string): \n word: ")
    dfa = DFA.DFA(states, alphabet, transitions, start_state, final_state)
    if dfa.is_correct(word_to_check):
        print(word_to_check + " is correct.")
    else:
        print(word_to_check + " is not correct.")

    answer = input("Want to try it again with the same automata? (yes, no)\n answer: ")
    if answer == 'yes':
        os.system("cls")
        DFA3()
    elif answer == 'no':
        os.system("cls")
        main()
    else:
        return


def DFA4():
    states = {1, 2, 3, 4, 5, 6}
    alphabet = {'a', 'b', ' '}
    transitions = {
        (1, 'a'): 2, (1, ' '): 3,
        (2, 'a'): 2, (2, 'b'): 3,
        (3, 'a'): 4, (3, ' '): 1,
        (4, 'b'): 5,
        (5, 'b'): 6
    }
    start_state = 1
    final_state = {6}
    word_to_check = input("Write the word you want to verify for Automata 4 (use space for empty string): \n word: ")
    dfa = DFA.DFA(states, alphabet, transitions, start_state, final_state)
    if dfa.is_correct(word_to_check):
        print(word_to_check + " is correct.")
    else:
        print(word_to_check + " is not correct.")

    answer = input("Want to try it again with the same automata? (yes, no)\n answer: ")
    if answer == 'yes':
        os.system("cls")
        DFA4()
    elif answer == 'no':
        os.system("cls")
        main()
    else:
        return


def DFA5():
    states = {1, 2, 3}
    alphabet = {'1', ' '}
    transitions = {
        (1, '1'): 2, (1, ' '): 3,
        (2, '1'): 3,
        (3, ' '): 1
    }
    start_state = 1
    final_state = {3}
    word_to_check = input("Write the word you want to verify for Automata 5 (use space for empty string): \n word: ")
    dfa = DFA.DFA(states, alphabet, transitions, start_state, final_state)
    if dfa.is_correct(word_to_check):
        print(word_to_check + " is correct.")
    else:
        print(word_to_check + " is not correct.")

    answer = input("Want to try it again with the same automata? (yes, no)\n answer: ")
    if answer == 'yes':
        os.system("cls")
        DFA5()
    elif answer == 'no':
        os.system("cls")
        main()
    else:
        return


def DFA6():
    states = {1, 2, 3, 4, 5, 6, 7}
    alphabet = {'a', 'b', ' '}
    transitions = {
        (1, 'a'): 2,
        (2, 'a'): 3,
        (3, 'b'): 4, (3, ' '): 1,
        (4, 'b'): 5,
        (5, 'b'): 6, (5, ' '): 3,
        (6, 'a'): 7, (6, ' '): 5,
    }
    start_state = 1
    final_state = {7}
    word_to_check = input("Write the word you want to verify for Automata 6 (use space for empty string): \n word: ")
    dfa = DFA.DFA(states, alphabet, transitions, start_state, final_state)
    if dfa.is_correct(word_to_check):
        print(word_to_check + " is correct.")
    else:
        print(word_to_check + " is not correct.")

    answer = input("Want to try it again with the same automata? (yes, no)\n answer: ")
    if answer == 'yes':
        os.system("cls")
        DFA6()
    elif answer == 'no':
        os.system("cls")
        main()
    else:
        return


def DFA7():
    states = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
    alphabet = {'a', 'b', ' '}
    transitions = {
        (1, 'a'): 2,
        (2, 'a'): 3,
        (3, 'a'): 4, (3, ' '): 2,
        (4, 'b'): 5,
        (5, 'b'): 6, (5, ' '): 4,
        (6, 'a'): 7,
        (7, 'b'): 8, (7, ' '): 6,
        (8, 'b'): 9,
        (9, 'b'): 10, (9, ' '): 1,
        (10, 'b'): 11,
        (11, 'a'): 11, (11, ' '): 10,
    }
    start_state = 1
    final_state = {11}
    word_to_check = input("Write the word you want to verify for Automata 7 (use space for empty string): \n word: ")
    dfa = DFA.DFA(states, alphabet, transitions, start_state, final_state)
    if dfa.is_correct(word_to_check):
        print(word_to_check + " is correct.")
    else:
        print(word_to_check + " is not correct.")

    answer = input("Want to try it again with the same automata? (yes, no)\n answer: ")
    if answer == 'yes':
        os.system("cls")
        DFA7()
    elif answer == 'no':
        os.system("cls")
        main()
    else:
        return


print("Deterministic Finite Automatas Verifier")
print("------------------------------------------------------------------")
main()
