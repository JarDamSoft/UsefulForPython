#############################################################################
#                   UNPACKING COLLECTIONS OF DATA                           #
#       *args - positional arguments, *kwargs - key word arguments          #
#############################################################################

arguments = [1, 2, 3]
arguments2 = {"arg2": 2, "arg3": 3, "arg1": 1}
arguments3 = {2: "test2", 3: "test3", 1: "test1"}


def func1(arg1, arg2, arg3):
    print(arg1, arg2, arg3)


def func2(arg1=None, arg2=None, arg3=None):
    print(arg1, arg2, arg3)


def test1(name, age, other):
    print(name, age, other)


def test2(*args):
    print(*args)


def test3(**kwargs):
    print(**kwargs)


# ---------------------------------------------------------------------------
# default way to call function with several arguments:
# ---------------------------------------------------------------------------
func1(arguments[0], arguments[1], arguments[2])
func2(arguments2["arg2"], arguments2["arg3"], arguments2["arg1"])

print("\n---------------------------------------------------\n")

# ---------------------------------------------------------------------------
# better/faster way:
# ---------------------------------------------------------------------------
func1(*arguments)
func2(*arguments2)      # printing keys
func2(**arguments2)     # printing values

print("\n---------------------------------------------------\n")

test1(name="John", age=20, other="BlaBla")
test1(*arguments)
test1(**arguments2)
test2("John", 25, "asdas")
test2(*arguments)
# test3(name="John", age=25)
