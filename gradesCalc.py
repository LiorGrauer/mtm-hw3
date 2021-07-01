# consts declaration

ABC_SIZE = 26
FIRST_LOWER_CASE_LETTER = 'a'
LAST_LOWER_CASE_LETTER = 'z'
FIRST_UPPER_CASE_LETTER = 'A'
LAST_UPPER_CASE_LETTER = 'Z'
GRADE_DIVIDER = 2
MUDOLO_NUMBER_FOR_ID_DIGITS = 100
MIN_ID = 10000000
MAX_ID = 99999999
MIN_AVERAGE_GRADE = 50
MAX_AVERAGE_GRADE = 100
STUDENT_DOES_NOT_EXISTS = -1

#### PART 1 ####    
# final_grade: Calculates the final grade for each student, and writes the output (while eliminating illegal
# rows from the input file) into the file in `output_path`. Returns the average of the grades.
#   input_path: Path to the file that contains the input
#   output_path: Path to the file that will contain the output
def final_grade(input_path: str, output_path: str) -> int:
    output_list = readStudentsFromFile(input_path)
    sorted_output_list = sorted(output_list, key=lambda x: x[0])
    total_grades = 0
    for i in range(len(sorted_output_list)):
        student_final_grade = calculateFinalGrade(sorted_output_list[i][0], sorted_output_list[i][3])
        sorted_output_list[i] = [sorted_output_list[i][0], sorted_output_list[i][3], student_final_grade]
        total_grades += student_final_grade
    output = open(output_path,"w")
    for student in sorted_output_list:
        student_string = str(student[0]) + ", " + str(student[1]) + ", " + str(student[2]) + "\n"
        output.write(student_string)
    output.close()
    if(len(sorted_output_list) != 0):
        return total_grades // len(sorted_output_list)
    else:
        return 0

# readStudentsFromFile: receives input path to the data file and returns a list of lists and every list in the list
#                       of lists contains a legal student details
def readStudentsFromFile(input_path: str) -> list:
    input = open(input_path,"r")
    output_list = []
    for line in input:
        current_student = line.split(',')
        for i in range(len(current_student)):
            current_student[i] = current_student[i].strip()
        if current_student[0][0] != '0':
            for i in range(len(current_student)):
                if i != 1:
                    current_student[i] = int(current_student[i])
            if (current_student[0] >= MIN_ID and current_student[0] <= MAX_ID and 
                legalName(current_student[1]) and current_student[2] > 0 and 
                current_student[3] > MIN_AVERAGE_GRADE and current_student[3] <= MAX_AVERAGE_GRADE):
                location_of_student = studentExists(output_list, current_student[0])
                if (location_of_student >= 0):
                    output_list[location_of_student] = current_student 
                else:
                    output_list.append(current_student)
    input.close()
    return output_list

# legalName: receives a name and returns True if it is a legal name and False if not
def legalName(name: str) -> bool:
    for letter in name:
        if (not(letter >= FIRST_LOWER_CASE_LETTER and letter <= LAST_LOWER_CASE_LETTER) 
            and not(letter >= FIRST_UPPER_CASE_LETTER and letter <= LAST_UPPER_CASE_LETTER) 
            and not(letter == ' ' or letter == '\t')):
            return False
    return True

# studentExists: receives list of lists (each list in the list of lists represents a student) and id number
#                and checks if the list of lists contains a student with the recevied id number
#                if True returns the index of that student, if False return -1
def studentExists(list_of_lists: list, id: int) -> int:
    if len(list_of_lists) < 1:
        return STUDENT_DOES_NOT_EXISTS
    for index in range(len(list_of_lists)):
        if list_of_lists[index][0] == id:
            return index
    return STUDENT_DOES_NOT_EXISTS

# calculateFinalGrade: receives student id and grade and calculate his AVG base on the given formula.
def calculateFinalGrade(id: int, grade: int) -> int:
    return (((id % MUDOLO_NUMBER_FOR_ID_DIGITS) + grade)//GRADE_DIVIDER)

#### PART 2 ####
# wordToHistCaseInsensitive: returns hist that contains in each cells the number of times a letter showed in the string.
#   number of times 'a' appers will be in [0] and so on
def wordToHistCaseInsensitive(str: str) -> list:
    hist = [0]*ABC_SIZE
    for letter in str:
        if letter <=LAST_UPPER_CASE_LETTER and letter >= FIRST_UPPER_CASE_LETTER:
            hist[ord(letter) - ord(FIRST_UPPER_CASE_LETTER)]+=1
        elif letter <=LAST_LOWER_CASE_LETTER and letter >= FIRST_LOWER_CASE_LETTER:
            hist[ord(letter) - ord(FIRST_LOWER_CASE_LETTER)]+=1
    return hist

# check_strings: Checks if `s1` can be constructed from `s2`'s characters.
#   s1: The string that we want to check if it can be constructed
#   s2: The string that we want to construct s1 from
def check_strings(s1: str, s2: str) -> bool:
    hist_s1 = wordToHistCaseInsensitive(s1) 
    hist_s2 = wordToHistCaseInsensitive(s2)  
    for letter_count_1, letter_count_2 in zip(hist_s1,hist_s2):
        if(letter_count_1 > letter_count_2):
            return False
    return True

