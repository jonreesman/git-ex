def fib():
    fibonacci = [0, 1] # Start with the first two numbers in the sequence

    for i in range(2, 200): # Loop from the third number up to the 100th number
        next_number = fibonacci[i-1] + fibonacci[i-2] # Calculate the next number in the sequence
        fibonacci.append(next_number) # Add the next number to the list

    print(fibonacci)
    print("Hello Rickie")

if __name__ == "__main__":
    fib()