# Multiplicacao 9 x 3 = 27
# Em binario   1001 x 0011 = 0001 1011
# Sum          1001 + 0011 = 1100 

M = [0]*60 + [1, 0, 1, 1] # Multiplicand 3 (64 bits)
Q = [0]*28 + [0, 1, 0, 1] # Multiplier 9 (32 bits)
N = 32 # Bits

def multiply(multiplicand, multiplier):
    product = [0]*64 # Product (64 bits)

    for i in range(N - 1, -1, -1):
        lsb_multiplier = multiplier[N - 1]

        if lsb_multiplier == 1:
            product = addition(product, multiplicand)

        # shift left
        multiplicand.pop(0)
        multiplicand.append(0)

        # shift right
        multiplier.pop()
        multiplier.insert(0, 0)


    return product

def addition(product, multiplicand):
    carry = 0

    for i in range(N + 32 - 1, -1, -1):
        bit1 = multiplicand[i]
        bit2 = product[i]

        # Full Adder
        sum_bits = bit1 + bit2 + carry
        product[i] = sum_bits % 2
        carry = sum_bits // 2

    return product


if __name__ == "__main__":
    result = multiply(M, Q)
    print(result)
