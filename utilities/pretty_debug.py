"""
Class for nice debugging
"""
class pretty_debug():

    def __init__(self, message=False, exp=False, email_sent=False, status_code=2):

        self.exp = exp
        self.message = message
        self.email_sent = email_sent
        self.status_code = status_code
        self.main()

    def main(self):

            response = "\n message -> {}".format((str(self.message)))

            if(self.exp):

                response = response + "\n \033[4mException\033[0m -> \033[91m {} \033[0m".format(str(self.exp))

            print(response)