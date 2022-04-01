
class CreditCard:
    
        def __init__(self, number):
            self.number = number

        def isValid(self, number):
            sum = self.sumOfDoubleEvenPlace(number) + self.sumOfOddPlace(number)
            if (sum % 10 == 0):
                return True
            else:
                return False

        def sumOfDoubleEvenPlace(self, number):
            rev_number = number[::-1]
            counter = 1
            sum = 0
            for i in rev_number:
                if counter % 2 == 0:
                    sum += self.getDigitNumber(i)
                counter += 1
            return sum

        def getDigitNumber(self, number):
            int_number = int(number)
            result = int_number * 2
            str_result = str(result)
            if (len(str_result) > 1):
                return int(str_result[0]) + int(str_result[1])
            else:
                return result

        def sumOfOddPlace(self, number):
            rev_number = number[::-1]
            counter = 1
            sum = 0
            for i in rev_number:
                if counter % 2 != 0:
                    sum += int(i)
                counter += 1
            return sum

        def prefixMatched(self, number, d):
            if d[0] == number[0]:
                return True
            else:
                return False

        def getSize(self, d):
            return len(d)

        def getPrefix(self, number, k):
            return number[0:k]

card1 = CreditCard('34567889')
print(card1.isValid('4388576018402626'))
print(card1.prefixMatched('4388576018402626', '4388'))
print(card1.getPrefix('4388576018402626', 3))
print(card1.getSize('4388'))
card2 = CreditCard('2345688099')
print(card2.isValid('4388576018410707'))
print(card2.prefixMatched('4388576018410707', '5388'))
print(card2.getPrefix('4388576018410707', 5))
print(card2.getSize('5388'))

