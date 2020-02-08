"""
MDST Workshop 1 - Python Basics Starter Code
"""

# Add any imports you need here:
import random
import sys
import base64

def part1(num):
    """
    Ask the user for a number. Depending on whether the number is even or odd,
    print out an appropriate (i.e. "even" or "odd") message to the user.
    """
    type_num = "odd"
    
    if num % 2 == 0:
        type_num = "even"
    
    print("Your number is", type_num)
    

def part2():
    """
    Generate a random number between 1 and 9 (including 1 and 9). Ask the user
    to guess the number, then tell them whether they guessed too low, too high,
    or exactly right.
    (Hint: remember to use the user input lessons from the very first
    exercise).
    Keep the game going until the user types "exit".
    [ try checking the random module in python on google. Concepts: Infinite
    loops, if, else, loops and user/input].
    """
    
    while 1:
        rando = random.randint(0,9)
        
        user_input = input("Guess a number [0,9]")
        
        if user_input == "exit":
            return
        if int(user_input) == rando:
            print("exactly right")
        if int(user_input) < rando:
            print("too low")
        if int(user_input) > rando:
            print("too high")


def part3(string):
    """
    Ask the user for a string and print out whether this string is a palindrome
    or not. (A palindrome is a string that reads the same forwards and
    backwards.)
    """

    i = 0
    j = len(string) - 1
    while i < j:
        if(string[i] != string[j]):
            print("Not a palindrome")
            return
        i += 1
        j -= 1
    
    print("Is a palindrome")
            
def part4a(filename, username, password):
    """
    Encrypt your username and password using base64 module
    Store your encrypted username on the first line and your encrypted password
    on the second line.
    """
    enc_user = base64.b64encode(username.encode('utf-8'))
    enc_password = base64.b64encode(password.encode('utf-8'))
    
    with open(filename, "wb") as fh:
        fh.write(enc_user)
        fh.write(b'\n')
        fh.write(enc_password)
    
def part4b(filename, password=None):
    """
    Create a function to read the file with your login information.
    Print out the decrypted username and password.
    If a password is specified, update the file with the new password.
    """
    with open(filename, "rb") as fh:
        enc_user = fh.readline()
        enc_password = fh.readline()
        
        username = base64.b64decode(enc_user).decode('utf-8')
        password_old = base64.b64decode(enc_password).decode('utf-8') 
        
        print(username)
        print(password_old)
        
    if password != None:
        part4a(filename, username, password)
        
if __name__ == "__main__":
    part1(3)  # odd!
    part1(4)  # even!
    part2()
    part3("ratrace")  # False
    part3("racecar")  # True
    part4a("secret.txt", "naitian", "p4ssw0rd")
    part4b("secret.txt")
    part4b("secret.txt", password="p4ssw0rd!")
    part4b("secret.txt")
