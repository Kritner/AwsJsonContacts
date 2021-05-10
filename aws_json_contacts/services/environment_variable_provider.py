import os


def get_environment_variable_or_default(key: str, default: str) -> str:
    """
    Attempt to get an environment variable, return it or the default
    :param key: The key of the environment variable to retrieve.
    :param default: The default value to return if the value of the key is None.
    :return: The environment variable value or default.
    """

    return os.environ[key] if os.environ[key] is not None else default
