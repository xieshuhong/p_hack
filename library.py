class Library:
    def __init__(self, name, post_code, square, Phone_Number, Monday_Open, Monday_Close, Tuesday_Open, Tuesday_Close,
                 Wednesday_Open, Wednesday_Close, Thursday_Open, Thursday_Close, Friday_Open, Friday_Close,
                 Saturday_Open, Saturday_Close, Sunday_Open, Sunday_Close):
        self.name = name
        self.post_code = post_code
        self.square = square
        self.phone_number = Phone_Number

        self.Monday_Open = Monday_Open
        self.Monday_Close = Monday_Close

        self.Tuesday_Open = Tuesday_Open
        self.Tuesday_Close = Tuesday_Close

        self.Wednesday_Open = Wednesday_Open
        self.Wednesday_Close = Wednesday_Close

        self.Thursday_Open = Thursday_Open
        self.Thursday_Close = Thursday_Close

        self.Friday_Open = Friday_Open
        self.Friday_Close = Friday_Close

        self.Saturday_Open = Saturday_Open
        self.Saturday_Close = Saturday_Close

        self.Sunday_Open = Sunday_Open
        self.Sunday_Close = Sunday_Close

    def __str__(self):
        return f"{self.name} {self.post_code} {self.square} {self.phone_number} {self.Monday_Open}-{self.Monday_Close}" \
               f"{self.Tuesday_Open}-{self.Tuesday_Close} {self.Wednesday_Open}-{self.Wednesday_Close} " \
               f"{self.Tuesday_Open}-{self.Thursday_Close} {self.Friday_Open}-{self.Friday_Close} " \
               f"{self.Saturday_Open}-{self.Saturday_Close} {self.Sunday_Open}-{self.Sunday_Close}"

    def formatlibraryInfo(self):
        return f"{self.name},{self.post_code},{self.square},{self.phone_number},{self.Monday_Open},{self.Monday_Close}," \
               f"{self.Tuesday_Open},{self.Tuesday_Close},{self.Wednesday_Open},{self.Wednesday_Close}, " \
               f"{self.Tuesday_Open},{self.Thursday_Close},{self.Friday_Open},{self.Friday_Close}, " \
               f"{self.Saturday_Open},{self.Saturday_Close},{self.Sunday_Open},{self.Sunday_Close}"

# get the attributes
    def name(self):
        return self.name

    def post_code(self):
        return self.post_code

    def square(self):
        return self.square

    def phone_number(self):
        return self.phone_number

    def Monday_Open(self):
        return self.Monday_Open

    def Monday_Close(self):
        return self.Monday_Close

    def Tuesday_Open(self):
        return self.Tuesday_Open

    def Tuesday_Close(self):
        return self.Tuesday_Close

    def Wednesday_Open(self):
        return self.Wednesday_Open

    def Wednesday_Close(self):
        return self.Wednesday_Close

    def Thursday_Open(self):
        return self.Thursday_Open

    def Thursday_Close(self):
        return self.Thursday_Close

    def Friday_Open(self):
        return self.Friday_Open

    def Friday_Close(self):
        return self.Friday_Close

    def Saturday_Open(self):
        return self.Saturday_Open

    def Saturday_Close(self):
        return self.Saturday_Close

    def Sunday_Open(self):
        return self.Sunday_Open

    def Sunday_Close(self):
        return self.Sunday_Close

    # set the attributes
    def set_name(self, name):
        self.name = name

    def set_post_code(self, post_code):
        self.post_code = post_code

    def set_square(self, square):
        self.square = square

    def set_Monday_Open(self, phone_number):
        self.phone_number = phone_number

    def set_Monday_Close(self, Monday_Close):
        self.Monday_Close = Monday_Close

    def set_Tuesday_Open(self, Tuesday_Open):
        self.Tuesday_Open = Tuesday_Open

    def set_Tuesday_Close(self, Tuesday_Close):
        self.Tuesday_Close = Tuesday_Close

    def set_Wednesday_Open(self, Wednesday_Open):
        self.Wednesday_Open = Wednesday_Open

    def set_Thursday_Open(self, Thursday_Open):
        self.Thursday_Open = Thursday_Open

    def set_Thursday_Close(self, Thursday_Close):
        self.Thursday_Close = Thursday_Close

    def set_Friday_Open(self, Friday_Open):
        self.Friday_Open = Friday_Open

    def set_Friday_Close(self, Friday_Close):
        self.Friday_Close = Friday_Close

    def set_Saturday_Open(self, Saturday_Open):
        self.Saturday_Open = Saturday_Open

    def set_Saturday_Close(self, Saturday_Close):
        self.Saturday_Close = Saturday_Close

    def set_Sunday_Open(self, Sunday_Open):
        self.Sunday_Open = Sunday_Open

    def set_Sunday_Close(self, Sunday_Close):
        self.Sunday_Close = Sunday_Close
