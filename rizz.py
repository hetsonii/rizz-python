import sys
import argparse

def init_code():
    """Returns the initial code for the compiler"""
    code = """_=+([]==[]);"""
    for i in range(2, 9 + 1):
        code += f"{'_'*i}={'_'*(i-1)}+_;"
    return code

def get_binary_factors(n):
    """Returns a list of factors of a given number in binary form"""
    return [index for index, bit in enumerate(bin(n)[:1:-1]) if bit == "1"]

def codegen(factors):
    """Generates code for a given list of factors"""
    char_code = ""
    for index, factor in enumerate(factors):
        char_code += "_" if factor == 0 else f"__**{'_'*factor}"
        if index < len(factors) - 1:
            char_code += "+"
    return char_code

def wrap_exec(encoded_string_len, encoded_python_string):
    """Wraps code in exec()"""
    return f"""exec((('%'+'c̶'[[]>[]])*({encoded_string_len}))%({','.join(encoded_python_string)}))"""

def main():
    parser = argparse.ArgumentParser(description='Python Code Rizzler')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-c', '--code', type=str, default='print("Hello, World!")',
                        help='Python code to glow up (default: print("Hello, World!"))')
    group.add_argument('-i', '--input', type=str, help='Python file to obfuscate')

    parser.add_argument('-r', '--run', action='store_true', help='Execute the generated code')
    parser.add_argument('-o', '--output', type=str, help='Save the obfuscated code to a file')
    
    args = parser.parse_args()

    if args.input:
        with open(args.input, 'r', encoding='utf-8') as f:
            code_to_obfuscate = f.read()
    else:
        code_to_obfuscate = args.code

    # Generate obfuscated code
    encoded_python_string = [codegen(get_binary_factors(ord(char))) for char in code_to_obfuscate]
    encoded_string_len = codegen(get_binary_factors(len(code_to_obfuscate)))

    generated_code = init_code()
    generated_code += wrap_exec(encoded_string_len, encoded_python_string)
    
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(generated_code)
        print(f"Obfuscated code saved to {args.output}")
    else:
        print(generated_code)
    
    if args.run:
        exec(generated_code)

if __name__ == "__main__":
    main()
