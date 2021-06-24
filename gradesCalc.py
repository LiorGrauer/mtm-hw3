#### PART 1 ####
# final_grade: Calculates the final grade for each student, and writes the output (while eliminating illegal
# rows from the input file) into the file in `output_path`. Returns the average of the grades.
#   input_path: Path to the file that contains the input
#   output_path: Path to the file that will contain the output
def final_grade(input_path: str, output_path: str) -> int:
    # TODO: implement here
    raise NotImplementedError


#### PART 2 ####
# check_strings: Checks if `s1` can be constructed from `s2`'s characters.
#   s1: The string that we want to check if it can be constructed
#   s2: The string that we want to construct s1 from
# consts declaration

ABC_SIZE = 26
FIRST_LOWER_CASE_LETTER = 'a'
FIRST_UPPER_CASE_LETTER = 'A'
LAST_UPPER_CASE_LETTER = 'Z'

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
