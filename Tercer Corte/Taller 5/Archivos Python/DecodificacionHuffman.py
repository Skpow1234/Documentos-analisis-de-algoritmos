# Recibe el diccionario y una cadena de bits
def decode(dic, bitstr):
    res = [{"j": "1001111", "e": "101", "h": "10010000", "\u00e9": "01100011", "end": "0110000001", "m": "011001", "y": "111001", "g": "100101", "\u00ed": "10011100", "o": "0100", "p": "11000", " ": "000", "\n": "011000101", "u": "1101", "\u00bf": "011000010", ".": "011000100", "q": "11101", "s": "0101", "v": "10011101", "a": "0010", "t": "11001", "\u00f3": "0110000000", "l": "1111", "d": "00111", "i": "00110", ",": "100110", "?": "011000011", "r": "1000", "b": "1001001", "n": "0111", "z": "1110001", "\u00e1": "011000001", "f": "1110000", "\u00fa": "10010001", "c": "01101"}]
    length = bitstr.bit_length() - 1
    # El primer caracter debe ser 1, o hay un error
    if bitstr >> length != 1:
        raise ("Corrupt file!")
    done = False
    # Iteramos hasta llegar al final
    while length > 0 and not done:
        shift = length - 1
        # Incrementamos de un bit en un bit
        while True:
            num = bitstr >> shift
            # Quitamos el 1 inicial y el 0b de formato
            bitnum = bin(num)[3:]
            if bitnum not in dic:
                shift -= 1
                continue
            char = dic[bitnum]
            if char == 'end':
                done = True
                break
            res.append(char)
            bitstr = bitstr - ((num - 1) << shift)
            length = shift
    return ''.join(res)
    