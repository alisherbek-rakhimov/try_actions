# This is a sample Python script.


# Press <no shortcut> to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def printHi(name: str) -> None:
    # Use a breakpoint in the code line below to debug your script.
    print(f"Hi, {name}")  # Press Ctrl+F8 to toggle the breakpoint.
    _id = 2
    a = 2
    b = 3
    if a == 1:
        if b == 4:
            if a < 5:
                if b > 12:
                    if a > -5 and b > -9:
                        if a == b:
                            if a * 2 > b:
                                print("a")
                                print(id)
    try:
        a = b
    except BaseException:
        print("catched")


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    printHi("PyCharm")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

from typing import Dict


def a(x: Dict[str, str]) -> None:
    print(x)
