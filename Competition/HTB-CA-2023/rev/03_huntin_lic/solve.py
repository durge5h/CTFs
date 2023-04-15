param_1 = ''
param_2 =  'G{zawR}wUz}r\x7f222\x13'#'G{zawR}wUz}r'
param_3 = 0x11
param_4 = 0x13
rev_me = '0wTdr0wss4P'

def xor(param_1, param_2, param_3, param_4):
    result = ''
    for i in range(param_3):
        if i < len(param_2):
            result += chr(ord(param_2[i]) ^ param_4)
        else:
            result += '\x00'
    return result

result = xor(param_1, param_2, param_3, param_4)
print("\nPassword2 : ",rev_me[::-1])
print("Password3 : ",result)
