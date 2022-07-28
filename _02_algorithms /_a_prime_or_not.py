"""
Write code that can tell if a number is prime.
A prime number is a number that is only divisible by 1 and itself.
"""
from tkinter import messagebox, simpledialog, Tk


if __name__ == '__main__':
    window=Tk()
    window.withdraw()
    # TODO)
    #  1. Ask the user for a number
    #  2. Use a for loop, if statement, and modulo to find if the number
    #     is prime.
    #  3. If the number is divisible by any number other than 1 or itself,
    #     the number is not prime.
    q1 = simpledialog.askinteger(title='number', prompt="give me a number and i will tell you if it is prime")
    count=0
    for i in range(2, q1):
        ansc = (q1)%(i)
        print(ansc)
        if( q1 % i == 0):
            messagebox.showinfo('',"that is not a prime number")
            break
        else:
            count += 1
    print(count)
    if count == q1-2:
        messagebox.showinfo('',"that is a prime number")


