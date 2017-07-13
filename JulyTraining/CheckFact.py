__author__ = 'prasadmodi'
def fact(num):
    if(num == 0):
        return 1
    return num * fact(num-1)        # Factorial formula n*(n-1)

if __name__ == '__main__':
    print("Factorial of number", fact(5))


