def credit_count(age, income):
    try:
        risk = int(income) / int(age)
        return risk
    except ValueError:
        return 'Invalid value'
    except ZeroDivisionError:
        return 'Age cannot be 0'


age = input('age: ')
income = input('income: ')
print(credit_count(age, income))
