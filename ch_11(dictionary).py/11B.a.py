#write a progm that reads a string from keyword and create dict containing frequency of each char
#occuring in string also print these string also ploat in the form of histogram
 
def get_char_frequencies(input_string):
    """Calculate the frequency of each character in the input string."""
    freq_dict = {}
    for char in input_string:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1
    return freq_dict

def print_histogram(freq_dict):
    """Print a histogram of character frequencies."""
    for char, freq in sorted(freq_dict.items()):
        print(f"{char}: {'#' * freq}")

def main():
    # Read input from the user
    input_string = input("Enter a string: ")
    
    # Get the character frequencies
    freq_dict = get_char_frequencies(input_string)
    
    # Print the histogram
    print_histogram(freq_dict)

if __name__ == "__main__":
    main()
