import os
import util, circuit, output


if __name__ == '__main__':
    print("Quantum Random Number Generator")
    print("─" * os.get_terminal_size().columns)

    output_str = ''
    repeat = True

    while repeat:
        filename = input("Save File Name (Empty String == No Save): ")
        token = input("Token: ")
        mode = input("Mode [Random/Password]: ").lower()
        if mode not in ['random', 'r', 'password', 'p']:
            raise RuntimeError("Invalid mode.")

        if mode in ['random', 'r']:
            num_random = int(input("Number of Random Numbers (MAX == 100,000): "))

            if not 0 < num_random <= 100_000:
                raise RuntimeError("Limit exceeded.")

            minimum = int(input("Minimum: "))
            maximum = int(input("Maximum: "))

            if minimum > maximum:
                raise RuntimeError("Invalid min/max.")

            min_number_qubits = util.calc_min_number_qubits(minimum, maximum)

            print("─" * os.get_terminal_size().columns)
            print("Input complete!")

            result = circuit.execute(token, min_number_qubits, 1)

            print("─" * os.get_terminal_size().columns)

            output_str += output.output_random(result, num_random, minimum, maximum)

        else: # mode == 'password'
            len_password = int(input("Length of Passwords (MAX == 100,000): "))

            if not 0 < len_password <= 100_000:
                raise RuntimeError("Limit exceeded.")

            num_password = int(input("Number of Passwords: "))

            digits = util.positive_negative(input("Digits? [Y/N]: ").lower())
            ascii = util.positive_negative(input("ASCII Letters? [Y/N]: ").lower())
            punc = util.positive_negative(input("Punctuations? [Y/N]: ").lower())
            
            settings = (digits, ascii, punc)
            if True not in settings:
                raise RuntimeError("No passwords can be generated with these settings.")

            print("─" * os.get_terminal_size().columns)
            print("Input complete!")

            result = circuit.execute(token, 127, num_password)
            
            print("─" * os.get_terminal_size().columns)

            output_str += output.output_password(result, num_password, len_password, settings)

        print(output_str, end='')
        if (filename != ''):
            with open(filename, 'w') as file:
                file.write(output_str)

        repeat = util.positive_negative(input("Repeat [Y/N]: ").lower())

    print("─" * os.get_terminal_size().columns)

    exit(0)