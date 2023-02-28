def my_function(p,l):
    "Funcion untuk menghitung luas"
    print(p*l)

my_function(2,6)

print('----------------------------------')

def print_me(str):
    "This prints a passed string into this function"
    print(str)
    return;

print_me("Funcion untuk menghitung luas")
print_me("Again Funcion untuk menghitung luas")

print('----------------------------------')

def change_print_me(my_print):
    my_print = "This prints a passed string into this function"
    print("Values inside :",my_print)
    return;

my_print = "Funcion untuk menghitung luas"
change_print_me(my_print)
print("Values outside : ",my_print)

print('----------------------------------')

def printme(str):
    "This prints a passed string into this function"
    print(str)
    return;

printme(str="Funcion untuk menghitung luas")

print('----------------------------------')

def printinfo(name, age = 20):
    "This prints a passed info into this function"
    print("Name : ",name)
    print("Age : ",age)
    return;

printinfo(name="Intan Amelia")
printinfo(name="Intan Amelia", age = 21)

print('----------------------------------')

def print_info(arg1, *vartuple):
    print("Output : ")
    print(arg1)
    for var in vartuple:
        print(var)
    return;

print_info(10)
print_info(20,30,60,70,"intan")

print('----------------------------------')

sum = lambda arg1, arg2: arg1 + arg2;

def sum(arg1, arg2):
    arg1 + arg2

print("Value of Total : ", sum(10,20))
print("Value of Total : ", sum(30,20))

print('----------------------------------')

def sum_1(arg1, arg2):
    total = arg1 + arg2
    total2 = total + arg1
    print("Inside the function : ", total)
    return total2;

total = sum_1(10, 10)
print("Outside the function : ", total)

print('----------------------------------')

total = 0;

def sum_2(arg1, arg2):
    total = arg1 + arg2
    print("Inside the function : ", total)
    return total;

sum_2(10, 20);
print("Outside the function : ", total)