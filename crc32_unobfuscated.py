# Make an example function that checks to see
# if the flag's CRC is equal to a specified value
# Flag is b'FLAG_CAPTURE_CVX\x86'

# Uses obfuscation techniques from dirac_point_function.py
# And bitwise_obfuscation.py

def flag_check(buf, *, ast_no_obfuscate=None):
    if not buf.startswith(bytes('FLAG_CAPTURE_', encoding='utf-8')):
        return False

    init = 0xffffffff

    arr = []

    for entry in range(256):
        l = entry
        for i in range(8):
            if l & 1:
                l = ~(l & 0x1db710640) & ~(~l & ~0x1db710640)
            l = l >> 1
        arr.append(l)

    for char in buf:
        init = (init >> 8) ^ arr[(~((~(~(init & 0xff) & ~(init & 0xff)))) & char) | (((~(~(init & 0xff) & ~(init & 0xff)))) & ~char)]

    init = init ^ 0xffffffff

    return ((((init ^ 2706522384) + 1) & (~(init ^ 2706522384)) | 1081813890) + (
            ~(((init ^ 2706522384) + 1) & (~(init ^ 2706522384))) & 1065669757)) ^ 4293732728 == 1234567

