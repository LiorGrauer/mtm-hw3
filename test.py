from gradesCalc import *

# Testing your implemented functions, feel free to add more tests below
def main():

     # Testing the `check_strings` function
    s1 = 'naanb'
    s2 = 'baNaNa'
    result = check_strings(s1=s1, s2=s2)
    assert result

    s3 = 'naanb'
    s4 = 'baNa'
    result = check_strings(s3, s4)
    assert not(result)

    s5 = 'aGGro'
    s6 = 'gaordg'
    result = check_strings(s5, s6)
    assert result

    s7 = 'ananas'
    result = check_strings(s7, s2)
    assert not(result)

    s8 = 'bannn'
    result = check_strings(s8, s2)
    assert not(result)

    # Testing the `final_grade` function
    input_path = 'tests/input'
    output_path = 'tests/out'
    course_avg = final_grade(input_path=input_path, output_path=output_path)
    assert course_avg == 70

    course_avg = final_grade('tests/input1.txt', 'tests/out1.txt')
    course_avg = final_grade('tests/input2.txt', 'tests/out2.txt')
    course_avg = final_grade('tests/input3.txt', 'tests/out3.txt')

if __name__ == "__main__":
    main()
