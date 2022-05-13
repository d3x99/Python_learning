numbers = {
    "0": 'zero',
    "1": 'one',
    "2": 'two',
    "3": 'three',
    "4": 'four',
    "5": 'five',
    "6": 'six',
    "7": 'seven',
    "8": 'eight',
    "9": 'nine'
}
numbers_spelled = ""
phone_number = input('Phone:')
for number in phone_number:
    numbers_spelled += numbers.get(number, "!") + " "
print(numbers_spelled)
