import problem_17_supplementary

class CreateDict:

    def __init__(self, dict_with_letters: dict):
        self.temp_numbers_dict = {}
        self.letters_dict = dict_with_letters
        self.numbers_dict = self.convert_to_numbers_dict()

    def convert_to_numbers_dict(self):
        for key, value in self.letters_dict.items():
            concentrate_value = ""
            value = value.split()
            for word in value:
                concentrate_value += word

            self.temp_numbers_dict[key] = len(concentrate_value)
        return self.temp_numbers_dict


class Number:

    def __init__(self, number):
        self.str_number = str(number)
        # print("the string is", self.str_number)

        if len(self.str_number) == 3:
            self.hundreds_digit = self.str_number[0]
            self.tens_digit = self.str_number[1]
            self.unity_digit = self.str_number[2]
            # print("the hundred digit is", self.hundreds_digit)
        elif len(self.str_number) == 2:
            self.tens_digit = self.str_number[0]
            self.unity_digit = self.str_number[1]
            # print("the tens digit is", self.tens_digit)
        else:
            self.unity_digit = self.str_number[0]
            # print("the unity digit is", self.unity_digit)
            # print("---------------------------------------")

        # self.unity_digit = self.str_number[0]
        # if len(self.str_number) > 1:
        #     self.tens_digit = self.str_number[1]
        # if len(self.str_number) > 2:
        #     self.hundreds_digit = self.str_number[2]
        self.letters_count_in_number = self.count_number_digits()
        # print("the added count", self.letters_count_in_number)

    def count_number_digits(self):
        temp_count = 0
        # for 1000
        if len(self.str_number) == 4:
            temp_count += len("onethousand")
        # for 100,200,300 ...
        elif len(self.str_number) == 3:
            if self.tens_digit == '0' and self.unity_digit == '0':
                temp_count += hundred_dict.numbers_dict[self.hundreds_digit]-3
            # for #10, #11, #12 ...
            elif self.tens_digit == '1':
                temp_count += hundred_dict.numbers_dict[self.hundreds_digit]
                temp_count += afterones_dict.numbers_dict[self.unity_digit]
            # for #20, #30, #40 ...
            elif self.tens_digit != '0' and self.unity_digit == '0':
                temp_count += hundred_dict.numbers_dict[self.hundreds_digit]
                temp_count += tens_dict.numbers_dict[self.tens_digit]
            # for #2#, #3#, #4# ...
            elif self.tens_digit != '0' and self.unity_digit != '0':
                temp_count += hundred_dict.numbers_dict[self.hundreds_digit]
                temp_count += tens_dict.numbers_dict[self.tens_digit]
                temp_count += unit_dict.numbers_dict[self.unity_digit]
            elif self.tens_digit == '0':
                temp_count += hundred_dict.numbers_dict[self.hundreds_digit]
                temp_count += unit_dict.numbers_dict[self.unity_digit]
        elif len(self.str_number) == 2:
            # print(self.tens_digit)
            # for 10, 11 ,12
            if self.tens_digit == '1':
                temp_count += afterones_dict.numbers_dict[self.unity_digit]
            # for 10, 11 ,12
            else:
                if self.unity_digit == '0':
                    temp_count += tens_dict.numbers_dict[self.tens_digit]
                else:
                    temp_count += tens_dict.numbers_dict[self.tens_digit]
                    temp_count += unit_dict.numbers_dict[self.unity_digit]
        else:
            temp_count += unit_dict.numbers_dict[self.unity_digit]





        #
        #
        #
        # # this is not good logic
        # if self.tens_digit == 1:
        #     temp_count += afterones_dict.numbers_dict[self.unity_digit]
        # else:
        #     temp_count += unit_dict.numbers_dict[self.unity_digit]
        #     temp_count += tens_dict.numbers_dict[self.tens_digit]
        # temp_count += hundred_dict.numbers_dict[self.hundreds_digit]

        return temp_count


class Counter:

    def __init__(self):
        self.sum_of_letter_count = 0

    def increase_counter(self, number_to_add):
        self.sum_of_letter_count += number_to_add
        # print("the sum so far", self.sum_of_letter_count)


unit_dict = CreateDict(problem_17_supplementary.UNITY_DICT)
print(unit_dict.numbers_dict)
afterones_dict = CreateDict(problem_17_supplementary.AFTERONES_DICT)
print(afterones_dict.numbers_dict)
tens_dict = CreateDict(problem_17_supplementary.TENS_DICT)
print(tens_dict.numbers_dict)
hundred_dict = CreateDict(problem_17_supplementary.HUNDREDS_DICT)
print(hundred_dict.numbers_dict)


def main(max_num):
    my_counter = Counter()
    for looped_number in range(1, max_num+1):
        number_instance = Number(looped_number)
        my_counter.increase_counter(number_instance.letters_count_in_number)
        # print("---------------------------------------------")
    res = my_counter.sum_of_letter_count
    print(res)
    return res

    # one_to_nine = (0, 3, 3, 5, 4, 4, 3, 5, 5, 4) # 1 to 9
    # ten_to_ninety = (0, 3, 6, 6, 5, 5, 5, 7, 6, 6) # 10 to 90
    # eleven_to_nineteen = (0, 6, 6, 8, 8, 7, 7, 9, 8, 8) # 11 to 19
    # spacial = (7, 10, 11) # hundred, hundred and, one thousand
    #
    # sum_1_to_99 = (sum(one_to_nine)*9 + ten_to_ninety[1] + sum(eleven_to_nineteen) + sum(ten_to_ninety[2:])*10)*10
    # sum_100_to_900 = spacial[0]*9 + spacial[1]*99*9 + sum(one_to_nine)*100
    #
    # total = sum_1_to_99 + sum_100_to_900 + spacial[2]
    #
    # print("the total is", total)


if __name__ == "__main__":
    main(1000)