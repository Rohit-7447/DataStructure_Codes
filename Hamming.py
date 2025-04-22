def generate_hamming_7_4(data_bits):
    hamming = [0] * 7

    # Assign data bits (positions 3, 5, 6, 7 in 1-based index)
    hamming[2] = int(data_bits[0])  # d1
    hamming[4] = int(data_bits[1])  # d2
    hamming[5] = int(data_bits[2])  # d3
    hamming[6] = int(data_bits[3])  # d4

    # Calculate parity bits
    hamming[0] = hamming[2] ^ hamming[4] ^ hamming[6]  # p1
    hamming[1] = hamming[2] ^ hamming[5] ^ hamming[6]  # p2
    hamming[3] = hamming[4] ^ hamming[5] ^ hamming[6]  # p4

    return ''.join(str(bit) for bit in hamming)


def detect_and_correct_7_4(received):
    bits = list(map(int, received))

    # Recalculate parity checks
    c1 = bits[0] ^ bits[2] ^ bits[4] ^ bits[6]
    c2 = bits[1] ^ bits[2] ^ bits[5] ^ bits[6]
    c4 = bits[3] ^ bits[4] ^ bits[5] ^ bits[6]

    error_pos = c1 * 1 + c2 * 2 + c4 * 4

    if error_pos:
        print(f"Error detected at position: {error_pos}")
        bits[error_pos - 1] ^= 1
    else:
        print("No error detected.")

    # Extract original 4 data bits (positions 3, 5, 6, 7)
    data = f"{bits[2]}{bits[4]}{bits[5]}{bits[6]}"
    corrected_code = ''.join(map(str, bits))

    return data, corrected_code


def main():
    print("\nSENDER'S SIDE\n")
    char = input("Enter a character to encode: ")
    ascii_val = ord(char)
    binary = format(ascii_val, '07b')  # 7-bit ASCII
    print(f"Binary Representation of '{char}': {binary}")

    # Split into two 4-bit blocks
    block1 = binary[:4]
    block2 = binary[4:] + '0'  # Pad with 0 to make 4 bits

    # Generate Hamming(7,4) code for both blocks
    encoded1 = generate_hamming_7_4(block1)
    encoded2 = generate_hamming_7_4(block2)

    final_encoded = encoded1 + encoded2
    print(f"Encoded Data (14 bits): {final_encoded}")

    print("\nERROR INTRODUCTION\n")
    error_bit = int(input("Enter error position (1-14) or 0 for no error: "))
    received = list(final_encoded)

    print("\nRECEIVER'S SIDE\n")
    if error_bit:
        received[error_bit - 1] = '1' if received[error_bit - 1] == '0' else '0'

    received = ''.join(received)
    print(f"Received Data: {received}")

    # Split back into 2 blocks
    received1 = received[:7]
    received2 = received[7:]

    data1, corrected1 = detect_and_correct_7_4(received1)
    data2, corrected2 = detect_and_correct_7_4(received2)

    full_binary = data1 + data2[:3]  # Only take first 3 bits from second block
    decoded_char = chr(int(full_binary, 2))

    print(f"\nCorrected Hamming Code Block 1: {corrected1}")
    print(f"Corrected Hamming Code Block 2: {corrected2}")
    print(f"Recovered Binary: {full_binary}")
    print(f"Decoded Character: {decoded_char}")


if __name__ == "__main__":
    main()



# Hamming Code (Another Implementation)
def calculate_parity_bits(data_bits, r):
    n = len(data_bits) + r
    hamming_code = ['0'] * n

    j = 0
    for i in range(1, n+1):
        if i == 2**j:
            j += 1
        else:
            hamming_code[i-1] = data_bits.pop(0)

    for i in range(r):
        pos = 2**i
        parity = 0
        for j in range(1, n+1):
            if j & pos and j != pos:
                parity ^= int(hamming_code[j-1])
        hamming_code[pos-1] = str(parity)

    return hamming_code

def detect_error(received_code):
    n = len(received_code)
    r = 0
    while (2**r) < n + 1:
        r += 1

    error_position = 0
    for i in range(r):
        pos = 2**i
        parity = 0
        for j in range(1, n+1):
            if j & pos:
                parity ^= int(received_code[j-1])
        if parity != 0:
            error_position += pos

    return error_position

if __name__ == "__main__":
    data = input("Enter the binary data bits (e.g., 1 0 1 1): ")
    data_bits = list(map(str, data.strip().split()))
    
    m = len(data_bits)
    r = 0
    while (2**r) < (m + r + 1):
        r += 1

    encoded = calculate_parity_bits(data_bits[:], r)
    print("Hamming Code (with parity bits):", ''.join(encoded))

    # Introducing an error manually
    received_input = input("Enter the received code (or press Enter to use the same): ")
    if received_input.strip():
        received_code = list(received_input.strip())
    else:
        received_code = encoded.copy()

    error_pos = detect_error(received_code)
    if error_pos == 0:
        print("No error detected.")
    else:
        print(f" Error detected at bit position: {error_pos}")
        print("Original bit at position", error_pos, ":", received_code[error_pos - 1])
        # Correcting the error
        received_code[error_pos - 1] = '1' if received_code[error_pos - 1] == '0' else '0'
        print("Corrected Code:", ''.join(received_code))


#hamming Code method 2 
# # Hamming Code
# import random

# def hamming_encode(data):
#     p1 = data[0] ^ data[1] ^ data[3]
#     p2 = data[0] ^ data[2] ^ data[3]
#     p4 = data[1] ^ data[2] ^ data[3]
#     encoded = [p1, p2, data[0], p4, data[1], data[2], data[3]]
#     return encoded, (p1, p2, p4)

# def hamming_correct(received):
#     s1 = received[0] ^ received[2] ^ received[4] ^ received[6]
#     s2 = received[1] ^ received[2] ^ received[5] ^ received[6]
#     s4 = received[3] ^ received[4] ^ received[5] ^ received[6]
#     print(f"Syndrome bits: s1 = {s1}, s2 = {s2}, s4 = {s4}")
#     error_pos = s1 * 1 + s2 * 2 + s4 * 4
#     if error_pos:
#         print(f"Error detected at position {error_pos}. Correcting...")
#         received[error_pos - 1] ^= 1
#     else:
#         print("No error detected.")
#     return received[2], received[4], received[5], received[6]

# if __name__ == "__main__":
#     char = input("Enter a character: ")
#     ascii_value = ord(char)
#     binary_data = format(ascii_value, '08b')
#     print(f"\nCharacter: '{char}'")
#     print(f"ASCII Value: {ascii_value}")
#     print(f"Binary Representation: {binary_data}")

#     data_part1 = [int(b) for b in binary_data[:4]]
#     data_part2 = [int(b) for b in binary_data[4:]]

#     encoded_part1, parity_bits1 = hamming_encode(data_part1)
#     encoded_part2, parity_bits2 = hamming_encode(data_part2)

#     print("\nFirst part encoding (4 data bits + 3 parity bits):")
#     print(f"Data: {''.join(map(str,data_part1))}")
#     print(f"Parity bits: {''.join(map(str,parity_bits1))}")
#     print(f"Hamminng Code (7 bits): {''.join(map(str, encoded_part1))}")

#     print("\nSecond part encoding (4 data bits + 3 parity bits):")
#     print(f"Data: {data_part2}")
#     print(f"Parity bits: {parity_bits2}")
#     print(f"Encoded (7 bits): {''.join(map(str, encoded_part2))}")

#     encoded_message = encoded_part1 + encoded_part2
#     print(f"\nFinal Encoded Message (14 bits): {''.join(map(str, encoded_message))}")

#     error_pos = random.randint(1,14)
#     if error_pos != 0:
#         encoded_message[error_pos - 1] ^= 1
#         print(f"\nError introduced at position {error_pos}. Modified encoded message: {''.join(map(str, encoded_message))}")
#     else:
#         print("\nNo error introduced.")

#     print("\nCorrecting first part of the encoded message...")
#     corrected_data1 = hamming_correct(encoded_message[:7])
#     print("\nCorrecting second part of the encoded message...")
#     corrected_data2 = hamming_correct(encoded_message[7:])

#     corrected_message = ''.join(map(str, corrected_data1 + corrected_data2))
#     corrected_ascii = int(corrected_message, 2)
#     corrected_char = chr(corrected_ascii)

#     print(f"\nCorrected 8-bit binary data: {corrected_message}")
#     print(f"Corrected ASCII value: {corrected_ascii}")
#     print(f"Corrected character: '{corrected_char}'")

