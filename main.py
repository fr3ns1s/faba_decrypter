def rotate_bits(byte, rotation):
    return ((byte >> rotation) | (byte << (8 - rotation))) & 0xFF

def process_file(input_file, output_file, key, rotation):

    try:
        with open(input_file, 'rb') as infile, open(output_file, 'wb') as outfile:
            data = infile.read()
            key_len = len(key)

            processed_data = bytes(
                rotate_bits(data[i], rotation) ^ key[i % key_len] for i in range(len(data))
            )

            outfile.write(processed_data)

        print(f"File elaborato con successo! Output salvato in: {output_file}")
    except Exception as e:
        print(f"Errore durante l'elaborazione del file: {e}")

key = [0x06, 0xA0, 0x23, 0x04]
rotation = 3
input_file = "CP01.MKI"
output_file = "CP01.mp3"

process_file(input_file, output_file, key, rotation)
