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

        positive = ['y', 'yes', 'true']
        negative = ['n', 'no', 'false']

        digits = input("Digits? [Y/N]: ").lower()
        if digits not in positive and digits not in negative:
            raise RuntimeError("Invalid option.")
        ascii = input("ASCII Letters? [Y/N]: ").lower()
        if ascii not in positive and ascii not in negative:
            raise RuntimeError("Invalid option.")
        punc = input("Punctuations? [Y/N]: ").lower()
        if punc not in positive and punc not in negative:
            raise RuntimeError("Invalid option.")
        
        settings = (True if digits in positive else False, 
                    True if ascii in positive else False, 
                    True if punc in positive else False)
        if True not in settings:
            raise RuntimeError("No passwords can be generated with these settings.")

        print("Input complete!")

        result = circuit.execute(token, num_password)
        output.print_password(result, num_password, len_password, settings)
    
    print("─" * os.get_terminal_size().columns)

    exit(0)