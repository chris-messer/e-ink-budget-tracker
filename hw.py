x_float = 1.0


def strcat_ba(a, b):
    assert type(a) is str, f"Input argument `a` has `type(a)` is {type(a)} rather than `str`"
    assert type(b) is str, f"Input argument `b` has `type(b)` is {type(b)} rather than `str`"

    return b + a

# `strcat_ba_test`: Test cell

# Workaround:  # Python 3.5.2 does not have `random.choices()` (available in 3.6+)
def random_letter():
    from random import choice
    return choice('abcdefghijklmnopqrstuvwxyz')

def random_string(n, fun=random_letter):
    return ''.join([str(fun()) for _ in range(n)])

a = random_string(5)
b = random_string(3)
c = strcat_ba(a, b)
print('strcat_ba("{}", "{}") == "{}"'.format(a, b, c))
assert len(c) == len(a) + len(b), "`c` has the wrong length: {len(c)} rather than {len(a)+len(b)}"
assert c[:len(b)] == b
assert c[-len(a):] == a
print("\n(Passed!)")

def strcat_list(L):
    assert type(L) is list
    l
    L.reverse()
    rL = "".join(L)
    return rL


# `strcat_list_test`: Test cell
n = 3
nL = 6
L = [random_string(n) for _ in range(nL)]
Lc = strcat_list(L)

print('L == {}'.format(L))
print('strcat_list(L) == \'{}\''.format(Lc))
assert all([Lc[i*n:(i+1)*n] == L[nL-i-1] for i, x in zip(range(nL), L)])
print("\n(Passed!)")