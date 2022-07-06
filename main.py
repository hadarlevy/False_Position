# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math
def f(x): return x**4+x**3-3*x**2
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


def FalsePosition(x0, x1):
    return (x0*f(x1)-x1*f(x0))/(f(x1)-f(x0))


x0 = 1
x1 = 2
maxi = 100
e = 0.0001
print("Method of False Position\n")
for i in range(maxi):
    x2 = FalsePosition(x0, x1)
    if f(x0)*f(x2) < 0:
        test = True
        print(f"Iteration {i+1}: \nInitial interval is ({round(x0,6)},{round(x1,6)}) \nx{i} = {round(x0,6)}, f(x{i}) = {round(f(x0),6)}\t x{i+1} = {round(x1,6)}, f(x{i+1}) = {round(f(x1),6)}\tx{i+2} = {round(x2,6)}, f(x{i+2}) = {round(f(x2),6)}")
        if abs(x1-x2) < e:
            print(
                f"Since |x{i+1}-x{i+2}| = {abs(round(x1-x2,6))}<{e}, we have reached the stopping condition \n")
            break
        else:
            pass
        x1 = x2
        print(
            f"Since f(x{i})*f(x{i+2}) = {round(f(x0)*f(x2),6)}<0, New interval is ({round(x0,6)},{round(x1,6)}) \n")
        if abs(f(x2)) < e:
            print(
                f"Since |f({round(x2,6)})| = {abs(round(f(x2),6))}<{e}, we have reached the stopping condition \n")
            break
        else:
            pass
    elif f(x1) * f(x2) < 0:
        test = True
        print(
            f"Iteration {i + 1}: \nInitial interval is ({round(x0, 6)},{round(x1, 6)}) \nx{i} = {round(x0, 6)}, f(x{i}) = {round(f(x0), 6)}\tx{i + 1} = {round(x1, 6)}, f(x{i + 1}) = {round(f(x1), 6)}\t x{i + 2} = {round(x2, 6)}, f(x{i + 2}) = {round(f(x2), 6)}")
        if abs(x2 - x0) < e:
            print(
                f"Since |x{i + 2}-x{i}| = {abs(round(x2 - x0, 6))}<{e}, we have reached the stopping condition \n")
            break
        else:
            pass
        x0 = x2
        print(
            f"Since f(x{i+1})*f(x{i+2}) = {round(f(x1)*f(x2),6)}<0, New interval is ({round(x0,6)},{round(x1,6)}) \n")
        if abs(f(x2)) < e:
            print(
                f"Since |f({round(x2, 6)})| = {abs(round(f(x2), 6))}<{e}, we have reached the stopping condition \n")
            break
        else:
            pass
else:
    test = False
    print("No root in the interval")
if test == True:
    print(
        f"The value of the root is {round(x2,6)} and the number of iterations required is {i+1}")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
