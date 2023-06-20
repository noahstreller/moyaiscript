def codeToMoai(code):
    final = ""
    for letter in code:
        count = ord(letter)
        while count > 0:
            final += "🗿"
            count -= 1
        final += ";\n"
    return final

def saveToFilePrompt(script):
    savePrompt = input("\nenter y or n: ")

    if savePrompt == "y":
        saveToFile(script)
    elif savePrompt == "n":
        return
    else:
        print("\n\nplease enter y for yes or n for no")
        saveToFilePrompt(script)

def saveToFile(script):
    file_path = './script.moyaiscript'
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(script)
        print('Successfully saved the script')
    except Exception as e:
        print(f'An error occurred while saving the script: {e}.')


file_path = './input.py'
try:
    with open(file_path, 'r', encoding='utf-8') as file:
        code = file.read()
    output = codeToMoai(code)
    print(output)
    print("-----------")
    print("Do you want to save this to script.moyaiscript?")
    saveToFilePrompt(output)


except Exception as e:
    print(e)
    print("Please create a file called input.py in this directory")

