# Using python 3.10.7

class ArrayConverter:
    def __init__(self, array: list) -> None:
        # Normalize array to str
        self.array =  self.normalize_array(array)
    
    def normalize_array(self, array: list) -> list:
        normalized_array = list()
        for elem in array:
            # Type match instead of if statements
            match elem:
                case int():
                    if elem < 38:
                        normalized_array.append(str(elem))
                case str():
                    # Includes negative value str case
                    if elem.replace('-', '').isnumeric() and int(elem) < 38:
                        normalized_array.append(elem)
                case list():
                    for nested_elem in elem:
                        if nested_elem < 38:
                            normalized_array.append(str(nested_elem))
        return normalized_array

    def print_array(self):
        print(', '.join(self.array))


def main():
    a = (1, 2, 3, 45, "7", [12, 45, 1], 23, "56")
    ArrayConverter(a).print_array()


if __name__ == '__main__':
    main()
