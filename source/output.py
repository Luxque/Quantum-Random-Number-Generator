import secrets
import util


def print_random(results: list, num_random: int, minimum: int, maximum: int) -> None:
    width = util.calc_width(num_random)
    variance = maximum - minimum + 1
    bit_str_dict = results[0][0].data.meas.get_counts()

    index = 0
    for _ in range(num_random):
        bit_str = secrets.choice(list(bit_str_dict.keys()))
        if bit_str_dict[bit_str] <= 1:
            del bit_str_dict[bit_str]
        else:
            bit_str_dict[bit_str] -= 1
            
        bit_str_int = int(bit_str, 2) % variance + minimum
        print(f"#{index:0{width}d}: {bit_str_int}")

        index += 1
    
    return


def print_password(results: list, num_password: int, len_password: int, settings: tuple) -> None:
    import string

    width = util.calc_width(num_password)

    characters = ''
    if settings[0]:
        characters += string.digits
    if settings[1]:
        characters += string.ascii_letters
    if settings[2]:
        characters += string.punctuation
    
    index = 0
    for result in results:
        for i in range(len(result)):
            bit_str_dict = result[i].data.meas.get_counts()
            password = ''

            for _ in range(len_password):
                bit_str = secrets.choice(list(bit_str_dict.keys()))
                if bit_str_dict[bit_str] <= 1:
                    del bit_str_dict[bit_str]
                else:
                    bit_str_dict[bit_str] -= 1

                bit_str_int = int(bit_str, 2)
                password += characters[bit_str_int % len(characters)]
            
            password = util.scramble_str(password)
            print(f"#{index:0{width}d}: {password}")

            index += 1
    
    return


if __name__ == '__main__':
    raise RuntimeError("Please use 'main.py' to run.")