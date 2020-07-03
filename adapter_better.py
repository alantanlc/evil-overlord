"""
Idea:
- Create an adapter for each minion
- Implement the same call_me function that calls the respective function  of each minion
- Now we can iterate over minions and call using the same call_me function

Problem:
- They all look quite the same
- Need to create a new adapter for each new minion type 
"""

class Elf(object):
    def nall_nin(self):
        print('Elf says: Calling the Overlord ...')

class Dwarf(object):
    def estver_narho(self):
        print('Dwarf says: Calling the Overlord ...')

class Human(object):
    def ring_mig(self):
        print('Human says: Calling the Overlord ...')

class ElfAdapter(object):
    def __init__(self, elf):
        self.elf = elf

    def call_me(self):
        self.elf.nall_nin()

class DwarfAdapter(object):
    def __init__(self, dwarf):
        self.dwarf = dwarf

    def call_me(self):
        self.dwarf.estver_narho()

class HumanAdapter(object):
    def __init__(self, human):
        self.human = human

    def call_me(self):
        self.human.ring_mig()

def main():
    """
    >>> minions = [ElfAdapter(Elf()), DwarfAdapter(Dwarf()), HumanAdapter(Human())]
    >>> for minion in minions:
    ...    minion.call_me()
    Elf says: Calling the Overlord ...
    Dwarf says: Calling the Overlord ...
    Human says: Calling the Overlord ...
    """

if __name__ == "__main__":
    import doctest
    doctest.testmod()
