class MorphologicalFSM:
    def __init__(self):
        self.states = ['start', 'consonant', 'vowel', 'sibilant', 'end']
        self.initial_state = 'start'
        self.current_state = self.initial_state
        self.transitions = {
            'start': {
                'consonant': 'consonant',
                'vowel': 'vowel',
                'sibilant': 'sibilant'
            },
            'consonant': 'end',
            'vowel': 'end',
            'sibilant': 'end'
        }

    def reset(self):
        self.current_state = self.initial_state

    def get_plural(self, noun):
        self.reset()
        last_char = noun[-1]
        if last_char in 'bcdfghjklmnpqrtvwxyz':
            self.current_state = self.transitions['start']['consonant']
        elif last_char in 'aeiou':
            self.current_state = self.transitions['start']['vowel']
        elif last_char in 'sxz' or noun[-2:] in ['sh', 'ch']:
            self.current_state = self.transitions['start']['sibilant']

        if self.current_state == 'consonant':
            return noun + 's'
        elif self.current_state == 'vowel':
            return noun + 's'
        elif self.current_state == 'sibilant':
            return noun + 'es'
        else:
            return noun

fsm = MorphologicalFSM()
test_nouns = [
    "cat",     
    "dog",     
    "bus",     
    "box",     
    "church",  
    "buzz",    
    "hero",    
    "kangaroo" 
]
for noun in test_nouns:
    plural_form = fsm.get_plural(noun)
    print(f"Singular: {noun}, Plural: {plural_form}")
