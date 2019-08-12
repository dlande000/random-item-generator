# Random Item Generator

Because I have enormous lists of movies to watch and books to read, and because I get overwhelmed choosing from these lists, I wrote this code which will generate a random item from a given list. 

When run in the command line, the code will ask for a file path to a CSV file. Once provided, a random line from the file will be printed. For lines without comma separation (line: 'hello world'), the line will be printed as a string ('hello world'). For lines with comma separation (line: 'entry 1,entry 2'), an array of the elements will be returned ('['entry 1', 'entry 2']'). 

Random Item Generator is written in Python. 