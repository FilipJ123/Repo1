#Karol Hydel, Kamil Fudali, Filip Jasicki
key_ = 0
def code(txt):
    coded = ""


    for i in range(len(txt)):
        key_ = i+1
        if ord(txt[i]) > 122 - key_:
            coded += chr(ord(txt[i]) + key_ - 26)
        else:
            coded += chr(ord(txt[i]) + key_)
    return coded

def main(args):

    tekst = input()
    print("Zaszyfrowany:\n", code(tekst))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))