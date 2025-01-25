import my_cryptography
import argparse

def parse_cmd_args():
    """This function parses the inputs for when the tool is used directly from the command line.
        It has the following options:
        -h, --help            show this help message and exit

        (REQUIRED one or the other)
        -e, -en, --encrypt    Encryption of the message or file will take place     
        -d, -de, --decrypt    Decryption of the message or file will take place     

        (REQUIRED)
        -a ALGO, --algo ALGO, --algorithm ALGO: !Defaults to Scytale as of 2025-01-24
                        Selected encryption/decryption algorithm

        -r RADIUS, --radius RADIUS: !Defaults to 5 as of 2025-01-24
                        Size of the radius for the Scytale Cypher

        -i INPUT, --input INPUT: !Default to "Endycrypt - encryption and decryption tool"
                        The input to be encrypted/dectypted. Can be string,   
                        '.txt' file name or file path

        -o OUTPUT, --output OUTPUT
                        Prints out by default but can be a '.txt' file name   
                        or file path"""

    parser = argparse.ArgumentParser(description="Encrypt and decrypt messages and files", epilog="")
    en_or_de = parser.add_mutually_exclusive_group(required=True)
    en_or_de.add_argument("-e", "-en", "--encrypt", action="store_true", help="Encryption of the message or file will take place")
    en_or_de.add_argument("-d", "-de", "--decrypt", action="store_true", help="Decryption of the message or file will take place")

    parser.add_argument("-a", "--algo", "--algorithm", help= "Selected encryption/decryption algorithm", default="scytale")
    parser.add_argument("-r", "--radius", type=int, help= "Size of the radius for the Scytale Cypher", default=5)

    parser.add_argument("-i", "--input", help= "The input to be encrypted/dectypted. Can be string, '.txt' file name or file path", default='Endecrypt - encryption and decryption tool')
    parser.add_argument("-o", "--output", help= "Prints out by default but can be a '.txt' file name or file path", default=None)

    args = parser.parse_args()
    args_dict = vars(args)
    validate_cmd_input_file(args_dict["input"])
    validate_cmd_output_file(args_dict["output"])

    return args_dict

def validate_cmd_input_file(input_arg: str):
    try:
        if input_arg[:-4] != '.txt':
            raise argparse.ArgumentError(f'{args_dict["output"]} does not have a valid file termination')
    finally:
        return True

def validate_cmd_output_file(output_arg: str):
    """This function validates the name of the output file set in the command line using the -o flag
    
        Arguments:
            output_arg: str - name of the file, comes from parser
        
        Returns:
            True: bool - validataion either passes and returns True or fails and raises an Error.
    """
    try:
        if output_arg[:-4] != '.txt':
            raise argparse.ArgumentError(f'{args_dict["output"]} does not have a valid file termination')
    finally:
        return True

def validate_cmd_algo():
    return True

def main():
    try:
        args = parse_cmd_args()
    except Exception as e:
        print(f'An unexpected error occured: {e}')

    #for key, value in args.items():
        #print(f'{key} = {value}')

    if args["encrypt"]:
        encoder = my_cryptography.Encoder()
    #print(hasattr(encoder, args["algo"]))

if __name__ == "__main__":
    main()