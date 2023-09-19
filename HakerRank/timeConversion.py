def timeConversion(s):
    am = 'AM' in s
    pm = 'PM' in s

    if am and s[:2] == '12':
        nova_hora = '00' + s[2:-2]
    elif am:
        nova_hora = s[:-2]
    elif pm and s[:2] == '12':
        nova_hora = '12' + s[2:-2]
    else:
        nova_hora = str(int(s[:2]) + 12) + s[2:-2]
    return nova_hora


print(timeConversion('11:05:45PM'))

# print(hora[-2:])
# print(hora[:-2])
# print(hora[:2])
# print('00'+hora[2:-2])
