import jwt


def encode(data: str, name: str, secret_key: str) -> str:
    """
    Encode data with given payload name
    :param data: str
    :param name: str
    :param secret_key: str
    :return: str
    """
    encoded_data = jwt.encode(
        {
            name: data
        },
        secret_key,
        algorithms=['HS256']
    )

    return encoded_data


def decode(encoded_data: str, name: str, secret_key: str) -> str:
    """
    Decode payload data by given payload name
    :param encoded_data: str
    :param name: str
    :param secret_key: str
    :return: str
    """
    decoded_object = jwt.decode(
        encoded_data,
        secret_key,
        algorithms=['HS256']
    )
    decoded_data = decoded_object[name]

    return decoded_data
