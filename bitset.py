class Bitset:
    def __init__(self, val=0):
        self._val = val

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise ValueError('descriptive error message')

        return bool(self._val & (1 << key))

    def __setitem__(self, key, value):
        if not (isinstance(key, int) and isinstance(value, bool)):
            raise ValueError('descriptive error message')

        if value:
            self._val |= (1 << key)
        else:
            self._val &= ~(1 << key)

    def __not__(self):
        return Bitset(~self._val)

    def __int__(self):
        return self._val

    # def __str__(self):
    #     return


b = Bitset()

b[10] = True
b[5] = True

b[5] = False

print(int(b))
