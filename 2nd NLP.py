class FiniteStateAutomaton:
    def __init__(self):
        self.states = ['start', 's1', 's2']
        self.accepting_state = 's2'
        self.initial_state = 'start'
        self.current_state = self.initial_state
        self.transition_table = {
            'start': {'a': 's1'},
            's1': {'b': 's2'},
            's2': {'a': 's1', 'b': 'start'},
        }

    def reset(self):
        self.current_state = self.initial_state

    def process_symbol(self, symbol):
        if symbol in self.transition_table[self.current_state]:
            self.current_state = self.transition_table[self.current_state][symbol]
        else:
            self.current_state = self.initial_state

    def accepts(self, input_string):
        self.reset()
        for symbol in input_string:
            self.process_symbol(symbol)
        return self.current_state == self.accepting_state
fsa = FiniteStateAutomaton()
test_strings = [
    "ab",
    "aab",
    "baab",
    "aabb",
    "babab",
    "aaaaab",
    "abab",
    "bba"
]
for string in test_strings:
    result = fsa.accepts(string)
    print(f"String '{string}': {'Accepted' if result else 'Rejected'}")
