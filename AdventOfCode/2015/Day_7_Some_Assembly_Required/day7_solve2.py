import functools

# Sample instructions
# instructions = [
#     "123 -> x",
#     "456 -> y",
#     "x AND y -> d",
#     "x OR y -> e",
#     "x LSHIFT 2 -> f",
#     "y RSHIFT 2 -> g",
#     "NOT x -> h",
#     "NOT y -> i"
# ]

# Parsing the instructions
wires = {}

with open('input.txt', 'r') as f:
    instructions = f.readlines()  # Note: Use readlines() to read all lines into a list
    for instruction in instructions:
        instruction = instruction.strip()
        parts = instruction.split(" ")
        if "AND" in instruction:
            wires[parts[-1]] = ('AND', parts[0], parts[2])
        elif "OR" in instruction:
            wires[parts[-1]] = ('OR', parts[0], parts[2])
        elif "LSHIFT" in instruction:
            wires[parts[-1]] = ('LSHIFT', parts[0], parts[2])
        elif "RSHIFT" in instruction:
            wires[parts[-1]] = ('RSHIFT', parts[0], parts[2])
        elif "NOT" in instruction:
            wires[parts[-1]] = ('NOT', parts[1])
        else:
            wires[parts[-1]] = ('ASSIGN', parts[0])

# Cache to store evaluated values
@functools.lru_cache(maxsize=None)
def get_value(wire):
    if wire.isdigit():
        return int(wire)
    
    if wire not in wires:
        raise ValueError(f"Wire '{wire}' is not defined in the instructions")
    
    op = wires[wire]
    if op[0] == "AND":
        result = get_value(op[1]) & get_value(op[2])
    elif op[0] == "OR":
        result = get_value(op[1]) | get_value(op[2])
    elif op[0] == "LSHIFT":
        result = get_value(op[1]) << int(op[2])
    elif op[0] == "RSHIFT":
        result = get_value(op[1]) >> int(op[2])
    elif op[0] == "NOT":
        result = ~get_value(op[1]) & 0xFFFF  # Ensure 16-bit value
    elif op[0] == "ASSIGN":
        result = get_value(op[1])
    
    return result

# Example: Get the value of wire 'a'
try:
    print(get_value('a'))  # Output depends on the provided instructions
except RecursionError:
    print("RecursionError: maximum recursion depth exceeded. There might be an undefined or circular dependency.")
except ValueError as e:
    print(e)
