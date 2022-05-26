#instantiate a variable for the book you are reading in
i_robot = []

#read the lines of a .txt file with UTF-8 encoding
with open("I_robot.txt","r") as i_robot_txt:
    lines= i_robot_txt.readlines()
    for line in lines:
        book_line = line.split("\n") #split the lines at \n characters to get the most accurate representations of the novel
        i_robot.append(book_line)

# print(len(i_robot))