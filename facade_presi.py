"""
Idea: One call to rule them all.
"""

class Elf(object):
    name = 'Galadriel'

    def nall_nin(self):
        print('Elf says: Calling the Overlord ...')

class Dwarf(object):

    def estver_narho(self):
        print('Dwarf says: Calling the Overlord ...')

class Human(object):

    def ring_mig(self):
        print('Human says: Calling the Overlord ...')

class MinionAdapter(object):
    _initialised = False

    def __init__(self, minion, **adapted_methods):
        self.minion = minion

        for key, value in adapted_methods.items():
            func = getattr(self.minion, value)
            self.__setattr__(key, func)

        self._initialised = True

    def __getattr__(self, attr):
        """Attributes not in Adapter are delegated to the minion"""
        return getattr(self.minion, attr)

    def __setattr__(self, key, value):
        if not self._initialised:
            super().__setattr__(key, value)
        else:
            setattr(self.minion, key, value)

class MinionFacade:
    minion_adapters = None

    @classmethod
    def create_minions(cls):
        print('Creating minions ...')
        cls.minion_adapters = [
            MinionAdapter(Elf(), call_me='nall_nin'),
            MinionAdapter(Dwarf(), call_me='estver_narho'),
            MinionAdapter(Human(), call_me='ring_mig')
        ]

    @classmethod
    def summon_minions(cls):
        print('Summoning minions ...')
        for adapter in cls.minion_adapters:
            adapter.call_me()

def main():
    """
    >>> MinionFacade.create_minions()
    Creating minions ...

    >>> MinionFacade.summon_minions()
    Summoning minions ...
    Elf says: Calling the Overlord ...
    Dwarf says: Calling the Overlord ...
    Human says: Calling the Overlord ...
    """

if __name__ == "__main__":
    import doctest
    doctest.testmod()
