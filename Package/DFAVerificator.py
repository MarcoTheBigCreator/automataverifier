class DFA:
    def __init__(self, states, alphabet, transitions, start_state, final_state):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.final_state = final_state

    def is_valid_transition(self, state, character):
        if (state, character) in self.transitions.keys():
            return True
        return False

    def is_correct(self, string):
        current_state = self.start_state
        for character in string:
            if self.is_valid_transition(current_state, character):
                current_state = self.transitions[(current_state, character)]
            else:
                return False
        if current_state in self.final_state:
            return True
        return False
