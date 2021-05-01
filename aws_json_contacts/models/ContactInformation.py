class ContactInformation:
    """
    Represents contact information
    """

    def __init__(self):
        self.__first_name = None
        self.__middle_name = None
        self.__last_name = None
        self.__zip_code = None
        self.__json_blob = None

    @property
    def first_name(self) -> str:
        return self.__first_name

    @first_name.setter
    def first_name(self, value) -> None:
        if self.__first_name is None:
            self.__first_name = value

    @property
    def middle_name(self) -> str:
        return self.__middle_name

    @middle_name.setter
    def middle_name(self, value) -> None:
        if self.__middle_name is None:
            self.__middle_name = value

    @property
    def last_name(self) -> str:
        return self.__last_name

    @last_name.setter
    def last_name(self, value) -> None:
        if self.__last_name is None:
            self.__last_name = value

    @property
    def zip_code(self) -> str:
        return self.__zip_code

    @zip_code.setter
    def zip_code(self, value) -> None:
        if self.__zip_code is None:
            self.__zip_code = value

    @property
    def is_valid_contact(self) -> bool:
        if self.first_name is None and \
                self.middle_name is None and \
                self.last_name is None and \
                self.zip_code is None:
            return False
        else:
            return True
