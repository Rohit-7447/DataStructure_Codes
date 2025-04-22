def xor_lists(list1, list2):
    return [a ^ b for a, b in zip(list1, list2)]

def crc(grp, divisor, i, dividend):
    while i < len(dividend):
        if grp[0] == 0:
            temp_divisor = [0] * len(divisor)
        else:
            temp_divisor = divisor

        result = xor_lists(grp, temp_divisor)
        result.pop(0)
        result.append(dividend[i])
        grp = result
        i += 1

    # Final XOR after all bits added
    if grp[0] == 0:
        temp_divisor = [0] * len(divisor)
    else:
        temp_divisor = divisor

    result = xor_lists(grp, temp_divisor)
    result.pop(0)
    return result

def check_crc(received_codeword, divisor):
    grp = received_codeword[:len(divisor)]
    remainder = crc(grp, divisor, len(divisor), received_codeword)
    return remainder

if __name__ == "__main__":
    dividend_input = input("Enter the dividend bits (e.g., 1 0 1 1): ")
    divisor_input = input("Enter the divisor bits (e.g., 1 0 1): ")

    # Parse inputs as lists of integers
    dividend = list(map(int, dividend_input.strip().split()))
    divisor = list(map(int, divisor_input.strip().split()))

    x = len(divisor)

    # Adding (x-1) zeros to the dividend
    appended_dividend = dividend + [0] * (x - 1)

    # Remainder :
    grp = appended_dividend[:x]
    remainder = crc(grp, divisor, x, appended_dividend)

    # final codeword (data + remainder)
    codeword = dividend + remainder

    print("Remainder:", remainder)
    print("Final Codeword (Data + Remainder):", codeword)

    # Check received codeword
    codeword_r = input("Enter the received codeword bits (e.g., 1 0 1 1 0 1): ")
    received_codeword = list(map(int, codeword_r.strip().split()))

    received_remainder = check_crc(received_codeword, divisor)
    if all(bit == 0 for bit in received_remainder):
        print("No Error Detected: The received codeword is valid.")
    else:
        print("Error Detected: The received codeword is corrupted.")
