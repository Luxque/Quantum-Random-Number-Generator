import os
import circuit, output


if __name__ == '__main__':
    print("Quantum Random Number Generator")
    print("─" * os.get_terminal_size().columns)

    token = input("Token: ")
    mode = input("Mode: ").lower()
    if mode not in ['random', 'password']:
        raise RuntimeError("Invalid mode.")

    if mode == 'random':
        num_random = int(input("Number of Random Numbers: "))
        print("Input complete!")

        result = circuit.execute(token, 1)
        output.print_random(result, num_random)

    else: # mode == 'password'
        len_password = int(input("Length of Passwords: "))
        num_password = int(input("Number of Passwords: "))
        print("Input complete!")

        result = circuit.execute(token, num_password)
        output.print_password(result, num_password, len_password)
    
    print("─" * os.get_terminal_size().columns)

    exit(0)