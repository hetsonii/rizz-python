# rizz-python

Transpiler to glow up your python code.

### Usage 

```
usage: rizz.py [-h] [-r] [-c CODE]

Python Code Rizzler

options:
  -h, --help       show this help message and exit
  -r, --run        Execute the generated code
  -c, --code CODE  Python code to glow up (default: print("Hello, World!"))
```

### Examples

```sh
# Print the obfuscated code output
python3 rizz.py -c "print('skibidi')"

# Run the obfuscated code output
python3 rizz.py -c "print('skibidi')" -r
```

```sh
# Run calculator on mac
python3 rizz.py -c "import os;os.system('open -a Calculator')" -r
```
