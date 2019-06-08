

customer_list = [['3'],['4'],['2'],['6'], ['1', 'female', 'Dutch', 'Gülseren', 'Willigenburg', 'Dingspelstraat 28', '9461 JE', 'Gieten', 'GulserenWilligenburg@teleworm.us', 'Ressoare', '06-92433659'],['0', 'male', 'Dutch', 'Daan', 'Nekeman', 'Straat 1', '9461 JE', 'Gieten', 'GulserenWilligenburg@teleworm.us','Ressoare', '06-92433659']]


def check_number(number):
    for person in customer_list:
        if person[0] == str(number):
            print("True")
            return True



def generateNumber():
    Number = 0
    while check_number(Number):
        Number = Number + 1
    else:
        print("nummer origin")
        print(Number)
        return Number



generateNumber()