# write a program to convert integer to roman value using class
# print number->symbols eg 1=I,4=IV,40->XL,50->L,90->XC,100->C,500->D,900->CM,1000->M
class IntToRoman:
    def convert(self, num):
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        roman_num = ''
        i = 0
        while num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num


while True:
    n = eval(input("Enter no:"))
    print(IntToRoman().convert(n))
