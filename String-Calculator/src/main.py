import re

def add(input: str = None) -> str:
    if input == "":
        return "0"
    elif len(input) == 1:
        return input
    else:
        if input.find(",\n") != -1:
            return "Number expected but '\n' found"
        
        input_parts = re.split(",|\n", input)
        result = 0

        for part in input_parts:
            try:
                result += int(part)
            except:
                return "Number expected but EOF found."

        return str(result)
