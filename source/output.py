import secrets
import util


def output_random(results: list, num_random: int, minimum: int, maximum: int) -> str:
    variance = maximum - minimum + 1
    bit_str_dict = results[0][0].data.meas.get_counts()

    width = util.calc_width(num_random)
    count = 1
    output_str = ''

    for _ in range(num_random):
        bit_str = secrets.choice(list(bit_str_dict.keys()))
        if bit_str_dict[bit_str] <= 1:
            del bit_str_dict[bit_str]
        else:
            bit_str_dict[bit_str] -= 1
            
        bit_str_int = int(bit_str, 2) % variance + minimum
        output_str += f"#{count:0{width}d}: {bit_str_int}\n"

        count += 1
    
    return output_str


def output_password(results: list, num_password: int, len_password: int, settings: tuple) -> str:
    import string

    characters = ''
    if settings[0]:
        characters += string.digits
    if settings[1]:
        characters += string.ascii_letters
    if settings[2]:
        characters += string.punctuation
    
    width = util.calc_width(num_password)
    count = 1
    output_str = ''

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
            output_str += f"#{count:0{width}d}: {password}\n"

            count += 1

    return output_str


if __name__ == '__main__':
    raise RuntimeError("Please use 'main.py' to run.")