def evenorodd(x):
    if x % 2 == 0:
        return True
    else:
        return False


if __name__ == "__main__":

    a = int(input("Enter a Number: "))
    res = evenorodd(a)
    if res == True:
        print("The number is Even")
    else:
        print("The number is Odd")
