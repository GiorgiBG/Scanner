import pwnedpasswords
from zxcvbn import zxcvbn


class PasswordCheck():
    def __init__(self, paswd):
        self.paswd = paswd
        self.report = []

    def append_report(self):
        with open("password_report.txt", "a") as pas_check_report:
            pas_check_report.write(self.check_breaches())
            pas_check_report.write(self.suggestion())
            pas_check_report.write(self.point_evaluation())
    def check_breaches(self):
        result = pwnedpasswords.check(self.paswd)

        return f"password : {self.paswd} \n" \
               f"breaches : {result} \n"

    def point_evaluation(self):

        capital_letters_amount = 0
        lower_letter_amount = 0
        digit_amount = 0
        other_char = 0
        if len(self.paswd) <= 8:
            evaluation = "Too short password"
        else:
            for char in self.paswd:
                if char.isupper():
                    capital_letters_amount += 1
                elif char.islower():
                    lower_letter_amount += 1
                elif char.isdigit():
                    digit_amount += 1
                else:
                    other_char += 1
            evaluation = f"length:{len(self.paswd)} lower: {lower_letter_amount}, upper: {capital_letters_amount}, digits: {digit_amount}" \
                         f" other_char: {other_char}\n"
        return evaluation

    def suggestion(self):
        result = zxcvbn(self.paswd)["feedback"]

        if result['warning'] == "" or len(result['suggestions']) == 0:
            return "Password looks good \n"
        else:
            return f"warning: {result['warning']} \nsuggestion: {result['suggestions']}"

    def showing_result(self):
        with open("password_report.txt", "r") as file:
            for line in file.readlines():
                if line == None:
                    pass
                print(line)


pas = PasswordCheck("12346578")

print(pas.suggestion())
