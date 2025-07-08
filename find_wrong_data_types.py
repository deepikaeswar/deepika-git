def find_wrong_types(data, expected_types):
    """
    Checks each dictionary in a list for type mismatches.

    Args:
        data (list of dict): The data to check.
        expected_types (dict): Field name -> expected type (type object).

    Returns:
        list of dict: Each dict contains row index and wrong fields with found and expected types.
    """
    wrong_type_rows = []
    for idx, row in enumerate(data):
        wrong_fields = {}
        for field, expected in expected_types.items():
            value = row.get(field)
            if value is not None and not isinstance(value, expected):
                wrong_fields[field] = {
                    'found_type': type(value).__name__,
                    'expected_type': expected.__name__,
                    'value': value
                }
        if wrong_fields:
            wrong_type_rows.append({'row': idx, 'errors': wrong_fields})
    return wrong_type_rows

# Example usage
if __name__ == "__main__":
    # Example input data
    data = [
        {'name': 'Alice', 'age': 30, 'score': 95.5},
        {'name': 'Bob', 'age': 'twenty', 'score': 88},
        {'name': 123, 'age': 22, 'score': 'ninety'}
    ]

    # Define expected types
    expected_types = {
        'name': str,
        'age': int,
        'score': float,
    }

    result = find_wrong_types(data, expected_types)
    if result:
        print("Rows with wrong data types found:")
        for entry in result:
            print(f"Row {entry['row']}:")
            for field, err in entry['errors'].items():
                print(f"  Field '{field}': found {err['found_type']} ('{err['value']}'), expected {err['expected_type']}")
    else:
        print("All data types are correct.")
