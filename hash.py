def init_hash_tables():
    table1 = [chr(i) for i in range(65, 91)]
    table2 = ["P", "Q", "A", "F", "K", "I", "L", "Z", "Y", "X", "W", "B", "U",
              "E", "J", "N", "C", "M", "T", "H", "V", "R", "S", "O", "G", "D"]
    table3 = [ord(letter) - 64 for letter in table2]

    return table1, table2, table3

def salting():
    import random
    charnum = random.randint(10, 20) # Random length for salt
    salt = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=charnum))
    return salt


def create_hash():

    table1, table2, table3 = init_hash_tables()
    salt = salting()
    MOD = 10 ** 9 + 7

    map1 = {table1[i]: table2[i] for i in range(26)}
    map2 = {table2[i]: table3[i] for i in range(26)}
    map3 = {table3[i]: table1[i] for i in range(26)}

    input_str = input("Enter a string: ").upper()
    input_str += salt

    first_hash_12 = [map1[ch] for ch in input_str if ch in map1]

    second_hash_23 = [map2[ch] for ch in first_hash_12]
    num_second_hash_23 = int("".join(map(str, second_hash_23)))

    index_map = {letter: i for i, letter in enumerate(table1)}

    third_hash_13 = [table3[index_map[ch]] for ch in first_hash_12]
    num_third_hash_13 = int("".join(map(str, third_hash_13)))

    fourth_hash = (num_second_hash_23 + num_third_hash_13)
    fourth_hash_str = str(fourth_hash)

    mixed = 0

    for a, b in zip(second_hash_23, third_hash_13):
        combined = a * 53 + b   # combine both paths
        mixed = (mixed * 31 + combined) % MOD

    fourth_hash_str = str(mixed).zfill(10)
    fifth_hash = []

    for idx, digit in enumerate(fourth_hash_str):

        if idx % 4 == 0:
            digit_int = int(digit)
            if digit_int in map3:
                fifth_hash.append(map3[digit_int])
            else:

                fifth_hash.append(digit)
        else:
            fifth_hash.append(digit)

    final_hash = "".join(fifth_hash)

    print("salt: ", salt)
    print("First hash (1 → 2): ", first_hash_12)
    print("Second hash (2 → 3): ", num_second_hash_23)
    print("Third hash (1 → 3): ", num_third_hash_13)
    print("Fourth hash : ", fourth_hash)
    print("Final hash : ", final_hash)


create_hash()