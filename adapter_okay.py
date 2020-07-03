"""
Idea:
- All minions have the same function but with different names to call the Overlord.
- Iterate over each minion, check for its type, and call the appropriate function accordingly 

Problem:
- Growing hard coded if else statement over time to accommodate new minion types
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

def main():
    """
    >>> minions = [Elf(), Dwarf(), Human()]

    >>> for minion in minions:
    ...     if isinstance(minion, Elf):
    ...         minion.nall_nin()
    ...     elif isinstance(minion, Dwarf):
    ...         minion.estver_narho()
    ...     else:
    ...         minion.ring_mig()
    Elf says: Calling the Overlord ...
    Dwarf says: Calling the Overlord ...
    Human says: Calling the Overlord ...
    """

if __name__ == "__main__":
    import doctest
    doctest.testmod()
