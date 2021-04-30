import sys

def hamming_distance(n1, n2):
    xor_n = n1 ^ n2
    distance = 0
    while(xor_n > 0):
        if xor_n & 1 == 1:
            distance = distance + 1
        xor_n >>= 1
    return distance

if __name__ == "__main__":
    n1 = sys.argv[1]
    n2 = sys.argv[2]
    print(f"A distancia de Hamming entre os números {n1} e {n2} é: " + str(hamming_distance(int(n1), int(n2))))
    
