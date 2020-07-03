"""
Idea:
- Use a general adapter class for all minions
- During construction, pass in the minion instance followed by the methods that you want to "adapt"
- Iterate over adapted_methods and for each unique function, we register that function with the general call_me name
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
        """Set attributes normally during initialisation"""
        if not self._initialised:
            super().__setattr__(key, value)
        else:
            """Set attributes on minion after initialisation"""
            setattr(self.minion, key, value)


def main():
    """
    >>> minion_adapters = [
    ...     MinionAdapter(Elf(), call_me='nall_nin'),
    ...     MinionAdapter(Dwarf(), call_me='estver_narho'),
    ...     MinionAdapter(Human(), call_me='ring_mig'),
    ... ]

    >>> for adapter in minion_adapters:
    ...     adapter.call_me()
    Elf says: Calling the Overlord ...
    Dwarf says: Calling the Overlord ...
    Human says: Calling the Overlord ...

    >>> elf_adapter = minion_adapters[0]
    >>> print(f'Name from Adapter: {elf_adapter.name}')
    Name from Adapter: Galadriel
    >>> print(f'Name from Minion: {elf_adapter.minion.name}')
    Name from Minion: Galadriel

    >>> minion_adapters[0].name = 'Elrond'
    >>> print(f'Name from Adapter: {elf_adapter.name}')
    Name from Adapter: Elrond
    >>> print(f'Name from Minion: {elf_adapter.minion.name}')
    Name from Minion: Elrond
    """

if __name__ == "__main__":
    import doctest
    doctest.testmod()
