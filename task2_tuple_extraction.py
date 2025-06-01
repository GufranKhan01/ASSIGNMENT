def extract_and_reverse():
    numbers=(1,2,3,4,5,6,7,8,9,10)
    extracted_numbers=numbers[:5]
    reversed_numbers=extracted_numbers[::-1]
    print("Original list:",numbers)
    print("Extracted first five elements",extracted_numbers)
    print("Reversed extracted elements:", reversed_numbers)
extract_and_reverse()