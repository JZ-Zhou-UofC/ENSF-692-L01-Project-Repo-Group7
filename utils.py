def find_keys_from_values(mapping_dict, value_list):
    """
    Returns a list of keys from a dictionary that correspond to values in a given list.

    Args:
        mapping_dict (dict): The dictionary to search (key -> value).
        value_list (list): List of values to search for in the dictionary.

    Returns:
        list: List of matching keys from the dictionary.
    """
    keys = []
    for name in value_list:
        for key, value in mapping_dict.items():
            if value == name:
                keys.append(key)
    return keys


if __name__ == "__main__":
    pass
