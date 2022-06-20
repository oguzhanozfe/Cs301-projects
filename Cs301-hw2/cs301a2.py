import time

# Radixsort is the method that performs sorting based on the placing of the character
def RadixSort(array, size, place):
    # Initialise empty array of size 26 to group strings from A - Z according to their placing
    alphabet = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]
    # Initialize empty array of list from a to z
    output = {"a": [], "b": [], "c": [], "d": [], "e": []}

    # Sort the characters based on their placing and store them in sorted array according to their alphabet group
    # Index 0 in sorted array depicts alphabet A
    # Index 1 in sorted array depicts alphabet B and etc
    for i in range(0, size):
        j = alphabet.index(array[i][place])
        output[alphabet[j]].append(array[i])

    # Copy the sorted string to original string array based on the alphabet of a specific placing
    index = 0
    for i in range(0, 26):
        # To get the sorted string for a particular alphabet in the output array
        length = len(output[alphabet[i]])
        for j in range(0, length):
            array[index] = output[alphabet[i]][j]
            index += 1


# Function to get the largest number of characters in a string from stringData array
def getMaxCharacters(stringarr, size):
    # Initialising the length of first string in array as the largest number of characters in a string
    max = len(stringarr[0])
    for i in range(0, size):
        if len(stringarr[i]) > max:
            max = len(stringarr[i])
    return max


array = ["mert", "aysu", "selin", "erden", "dilara"]
# Read the file that contains the strings

# Compute the size of sampleString to use later in the program
size = len(array)
# Set the starting time for the execution of the radixSort algorithm
start_time = time.time()
# Create a for loop to call radixSort function on every character placing in the string
for i in range(getMaxCharacters(array, size) - 1, -1, -1):
    RadixSort(array, size, i)
# Set the ending time for the execution of the radixSort algorithm
end_time = time.time()
print(array)
# Calculate total execution time and display it
print(
    "This program took %.f milliseconds to execute " % ((end_time - start_time) * 1000)
)
