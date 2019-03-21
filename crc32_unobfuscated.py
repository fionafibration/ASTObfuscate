# Make an example function that checks to see
# if the flag's CRC is equal to a specified value
# Flag is b'FLAG_CAPTURE_CVX\x86'


def flag_check(buf, *, ast_no_obfuscate=None):
    if not buf.startswith('FLAG_CAPTURE_'):
        return False
    crc = 0
    crc = crc ^ 0xffffffff

    crc_array = []

    for entry in range(256):
        l = entry
        for i in range(8):
            if l & 1:
                l = l ^ 0x1db710640
            l = l >> 1
        crc_array.append(l)

    for char in buf:
        crc = (crc >> 8) ^ crc_array[(crc & 0xff) ^ char]

    return crc ^ 0xffffffff == 0xDEADBEEF

