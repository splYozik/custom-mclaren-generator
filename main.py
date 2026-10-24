import os

LCG_A = 1664525
LCG_C = 1013904223
LCG_M = 2**32 # 4 294 967 295

def get_chaos_os() -> int:
    '''
    Generates a 32-bit integer from OS entropy

    os.urandom(1) give from OS 1 random byte.
    This byte is chaos of PC (disk, etc)

    int.from_bytes(....., byteorder="big") give new byte = int digit
    1 byte = 8 bit
    '''
    return int.from_bytes(os.urandom(4), byteorder="big")

def get_lcg(seed: int) -> int:
    '''
    Generator of method LCG:
    X_n+1 = (A * X_n + C) % M
    A = 
    C =
    M = modul
    seed (X_n) = now digit seed
    '''
    return (LCG_A * seed + LCG_C) % LCG_M

def main() -> None:
    '''
    Init table of 100 elaments, give 50 from get_chaos_os(),
    write in table new elements of LCG.
    Modifies a dynamic decimal mask for obfuscation (LVL_1 :) )
    '''
    # Start chaos from OS
    seed = get_chaos_os()

    # Init and generator elements
    table = []
    for _ in range(100):
        seed = get_lcg(seed) # New/start seed
        table.append(seed) # Save

    # Generate and output 50 numbers
    for i in range(1, 51):
        
        idx = get_chaos_os() % 100  # Select a random table index
        give_number = table[idx] # Fetch the 32-bite element from table

        
        # Delete 1-3 old bit
        # Chaos OC create digit of random length
        length = (get_chaos_os() % 10) + 1 # Lenght from 1 to 10 digits
        modul = 10 ** length # 10, 100, 1000 ...... 10000 etc
        number = give_number % modul # Cut digit on limit

        
        print(f"число {i}: {number}")
        seed = get_lcg(seed) # New element!
        table[idx] = seed


if __name__ == "__main__":
    main()