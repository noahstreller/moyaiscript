file_path = './script.moyaiscript'

with open(file_path, 'r', encoding='utf-8') as file:
    moyaiscript = file.read()
    print(f"\nrunning {file_path}")
    print("------------------------\n\n")

def parse(code):
    lines = code.split('\n')
    output = ""
    
    for line in lines:
        line = line.strip()
        if line:
            num_moyai = line.count('🗿')
            utf8_char = chr(num_moyai)
            output += utf8_char

    return output

result = parse(moyaiscript)
exec(result)