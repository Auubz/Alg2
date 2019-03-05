import re

class Password(unittest.Testcase):

    def validate_pw_complexity(password: string):

        complex_enough = True

        if not re.match("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,})",password):

            complex_enough = False


password = hshd f