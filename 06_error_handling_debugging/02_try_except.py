# Concept: Try/Except

# What is it?
# Use try/except to catch and handle errors without crashing the program.

# What are the most important things to know?
# Wrap risky code in try, and handle specific errors with except.

# Syntax & Example:
# try:
    x = 1 / 0
except ZeroDivisionError:
    print('Cannot divide by zero')

# Real-world analogy:
# Like wearing a helmet—if you fall, you don’t get hurt.