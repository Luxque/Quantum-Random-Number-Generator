import os, math, secrets
import circuit


if __name__ == '__main__':
    print("Quantum Random Number Generator")
    print("─" * os.get_terminal_size().columns)

    token = input("Token: ")
    num_shots = int(input("Shots: "))
    print("Input complete!")

    result = circuit.execute(token, num_shots)
    bit_str_dict = result[0].data.meas.get_counts()
    
    width = math.floor(math.log10(num_shots-1)) + 1
    index = 0

    while len(bit_str_dict) > 0:
        bit_str = secrets.choice(list(bit_str_dict.keys()))
        if bit_str_dict[bit_str] <= 1:
            del bit_str_dict[bit_str]
        else:
            bit_str_dict[bit_str] -= 1
            
        bit_str_int = int(bit_str, 2)
        print(f"#{index:0{width}d}: {bit_str_int}")

        index += 1
    
    print("─" * os.get_terminal_size().columns)