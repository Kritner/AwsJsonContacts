class JsonParsedResult:
    """
    Represents the result of attempting to read a string as json
    """

    def __init__(self, is_valid_json: bool, json: dict):
        """
        Constructs a JsonParsedResult

        :param is_valid_json: is the string json?
        :param json: the json string, when valid json, otherwise none
        """

        self.is_valid_json = is_valid_json
        self.json = json
