
# define variables:
answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
score = 0
i = 0
line_count = 0
digits = 0
letters = 0
score_list = []
N_list = []
f = None
filename = ""

# looping until a valid file is read
while f is None:
    filename = input("Enter a class file to grade (i.e. class1 for class1.txt): ")
    try:
        f = open(filename + ".txt")
        print("Successfully opened %s.txt" % filename)
        print("\n**** ANALYZING ****")
    except FileNotFoundError:
        print('File does not exist')
        f = None

# loop to brake each line in a file, each answer and student_id in each line (separated by ',')
for line in f:
    line_count += 1
    line = line.strip()
    # separate each line in the file by ','
    line_split = line.split(",")
    student_id = line.split(",")[0]
    id_count = list(student_id)
    # count number of letter and digits in student_id
    for c in id_count:
        if str(c).isdigit():
            digits += 1
        elif str(c).isalpha():
            letters += 1
    # check if the line is valid
    if len(line_split) == 26:
        # check if student_id is valid (1
        if digits == 8 and letters == 1 and id_count[0] == 'N':
            i = i + 1
            # define a list from answer_key
            answer_key_list = answer_key.split(',')
            # calculate the score by comparing with answer_key
            for j in range(1, len(line_split)):
                if line_split[j] == answer_key_list[j - 1]:
                    score += 4
                elif line_split[j] == "":
                    score += 0
                else:
                    score -= 1
            # append score and student_id to the lists
            score_list.append(score)
            N_list.append(line_split[0])
            score = 0
        else:
            print("Invalid line of data: N# is invalid:  ")
            print(line)
    elif len(line_split) != 26:
        print("Invalid line of data: does not contain exactly 26 values: ")
        print(line)
    digits = 0
    letters = 0

# close file
f.close()
if line_count == i:
    print("No errors found!")

# calculate mean, highest, lowest, range and median for each class:
score_mean = sum(score_list) / len(score_list)
score_highest = max(score_list)
score_lowest = min(score_list)
score_range = score_highest - score_lowest
score_median = 0
# creating a copy of scores to sort and find median
temp_list = score_list.copy()
temp_list.sort()
# finding median
if len(score_list) % 2 == 0:
    # even, median=average of middle two values
    score_median = (temp_list[len(temp_list) // 2] + temp_list[len(temp_list) // 2 - 1]) / 2
else:
    # odd, median=middle value
    score_median = temp_list[len(temp_list) // 2]

print("\n**** REPORT ****")
print("Total valid lines of data: %s" % i)
print("Total invalid lines of data: %s" % (line_count - i))
print('Mean (average) score: ', score_mean)
print('Highest score: ', score_highest)
print('Lowest score: ', score_lowest)
print('Range of scores: ', score_range)
print('Median score: ', score_median)

# open a result file and write student’s ID number, a comma, and then their grade
result_file = filename + '_grades.txt'
result = open(result_file, 'w+')
k = 0
while k < len(N_list):
    result.write('{:s},{:d}\n'.format(N_list[k], score_list[k]))
    k += 1
result.close()
