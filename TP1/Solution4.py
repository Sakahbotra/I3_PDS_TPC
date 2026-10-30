#Part B -- A Safe convert

def safe_int(text):
    "Turn text into an int; return None when it is not a number."
    text = text.strip()     #remove spaces
    if text.lstrip('-').isdigit():      #"42" or "-42" or "
        return int(text)
    #try and except are methods to handle errors in Python. The code inside the try block is executed, and if an error occurs, the code inside the except block is executed instead of crashing the program
    try:
        return int(float(text))  #"3.9" -> 3
    except ValueError:
        return None     #"abc", "", "12a" -> None

    for sample in ["42", " -8 ", "3.9", "abc", ""]:
        print(repr(sample), "->", safe_int(sample))     #repr() is a function that keeps everything in the string as the original
        