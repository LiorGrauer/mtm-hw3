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
        if (current_student[0][0] != 0 and legalName(current_student[1]) and current_student[2] > 0 and 
            current_student[3] > 50 and current_student[3] <= 100):
            int location_of_student = deepContains(output_list, current_student[0])
            if (location_of_student >= 0):
                output_list[location_of_student] = current_student 
            else:
                output_list += current_student
    sorted_output_list = sorted(output_list, key=operator.itemgetter(0))
    for student in sorted_output_list:
        student_output = [student[0], student[3], calculateFinalGrade(student[0], student[3])]
    for student in sorted_output_list:
        output.write(student)
    input.close()
    output.close()

def legalName(name: str) -> bool:
    for letter in name:
        if !(letter >= 'a' and leter <= 'z') and !(letter >= 'A' and leter <= 'Z'):
            return false
    return true

def deepContains(list_of_lists: list, number: int) -> int:
    for index in range(len(list_of_lists)):
        for value in list[index]:
            if value == number:
                return index
    return -1

# def returnFirstElement(list: list) -> int
#     return list[0]

def calculateFinalGrade(id: list, grade: int) -> int:
    return ((id % 100) + grade) // 2

#### PART 2 ####
# check_strings: Checks if `s1` can be constructed from `s2`'s characters.
#   s1: The string that we want to check if it can be constructed
#   s2: The string that we want to construct s1 from
def check_strings(s1: str, s2: str) -> bool:
    # TODO: implement here
    raise NotImplementedError
