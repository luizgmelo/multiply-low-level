# Multiplicacao 9 x 3 = 27
# Em binario   1001 x 0011 = 0001 1011
# Sum          1001 + 0011 = 1100 

M = [0, 0, 1, 1] # Multiplicando 3
Q = [1, 0, 0, 1] # Multiplicador 9

def multiply(n1, n2):
    n = len(n2) # multiplier
    result = [0] * n

    for i in range(n - 1, -1, -1):
        carry = 0

        bit3 = n2[n - 1]

        if bit3 == 1:
            for i in range(n - 1, -1, -1):
                bit1 = n1[i]
                bit2 = result[i]

                # Full Adder
                sum_bits = bit1 + bit2 + carry
                result[i] = sum_bits % 2
                carry = sum_bits // 2

        # shift right
        n2.pop() # discart bit
        shift_result_to_n2 = result.pop()
        n2.insert(0, shift_result_to_n2)
        # shift carry to result 
        result.insert(0, carry)

    return result + n2

if __name__ == "__main__":
    print(f"{M} x {Q} =", end=' ')
    result = multiply(M, Q)
    print(result)
