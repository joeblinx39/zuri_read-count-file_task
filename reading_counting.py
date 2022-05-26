

def read_file_content(filename):
    #[assignment] Add your code here
    with open(filename, 'r') as f:
        file =f.read()
        return file
        

output = read_file_content('story.txt')
print(output)

def count_words(read_file_content):
    # Create an empty dictionary
    counts = dict()
    words = read_file_content.split()

    # Loop through each line of the file
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

# Open the file in read mode
text = open("story.txt", "r")

#read content of file to string
data = text.read()

# Print the number of occurrences of word
print( count_words(data))