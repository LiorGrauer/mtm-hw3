# consts declaration

ABC_SIZE = 26
FIRST_LOWER_CASE_LETTER = 'a'
LAST_LOWER_CASE_LETTER = 'z'
FIRST_UPPER_CASE_LETTER = 'A'
LAST_UPPER_CASE_LETTER = 'Z'
GRADE_DIVIDER = 2
MUDOLO_NUMBER_FOR_ID_DIGITS = 100

#### PART 1 ####    
# final_grade: Calculates the final grade for each student, and writes the output (while eliminating illegal
# rows from the input file) into the file in `output_path`. Returns the average of the grades.
#   input_path: Path to the file that contains the input
#   output_path: Path to the file that will contain the output
def final_grade(input_path: str, output_path: str) -> int:
    input = open(input_path,"r")
    output = open(output_path,"w")
    output_list = []
    for line in input:
        current_student = line.lstrip().split(',')
        if (current_student[0][0] != 0 and legalName(current_student[1]) and current_student[2] > 0 and current_student[3] > 50 and current_student[3] <= 100):
            location_of_student = deepContains(output_list, current_student[0])
            if (location_of_student >= 0):
                output_list[location_of_student] = current_student 
            else:
                output_list += current_student
    sorted_output_list = sorted(output_list, key=lambda x: x[0])
    total_grades = 0
    number_of_students = 0
    for student in sorted_output_list:
        student_final_grade = calculateFinalGrade(student[0], student[3])
        student_output = [student[0], student[3], student_final_grade]
        student = student_output
        total_grades += student_final_grade
        number_of_students += 1
    for student in sorted_output_list:
        output.write(student)
    input.close()
    output.close()
    return total_grades // number_of_students

def legalName(name: str) -> bool:
    for letter in name:
        if not(letter >= FIRST_LOWER_CASE_LETTER and letter <= LAST_LOWER_CASE_LETTER) and not(letter >= FIRST_UPPER_CASE_LETTER and letter <= LAST_UPPER_CASE_LETTER):
            return False
    return True

def deepContains(list_of_lists: list, number: int) -> int:
    for index in range(len(list_of_lists)):
        for value in list_of_lists[index]:
            if value == number:
                return index
    return -1

def calculateFinalGrade(id: int, grade: int) -> int:
    return ((id % MUDOLO_NUMBER_FOR_ID_DIGITS) + grade) // GRADE_DIVIDER

#### PART 2 ####
# check_strings: Checks if `s1` can be constructed from `s2`'s characters.
#   s1: The string that we want to check if it can be constructed
#   s2: The string that we want to construct s1 from
def wordToHistCaseInsensitive(str: str) -> list:
    hist = [0]*ABC_SIZE
    for letter in str:
        if letter <=LAST_UPPER_CASE_LETTER and letter >= FIRST_UPPER_CASE_LETTER:
            hist[ord(letter) - ord(FIRST_UPPER_CASE_LETTER)]+=1
        else:
            hist[ord(letter) - ord(FIRST_LOWER_CASE_LETTER)]+=1
    return hist

def check_strings(s1: str, s2: str) -> bool:
    hist_s1 = wordToHistCaseInsensitive(s1) 
    hist_s2 = wordToHistCaseInsensitive(s2)  
    for letter_count_1, letter_count_2 in zip(hist_s1,hist_s2):
        if(letter_count_1 > letter_count_2):
            return False
    return True
    raise NotImplementedError
