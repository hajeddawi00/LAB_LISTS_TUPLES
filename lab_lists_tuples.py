lab_list = [2, 3, 4, 5, 15, 1, 43, 20]

#Q1 - Answer
def sum_of_list (lab_list)->int:
    total_sum:int = 0
    for i in lab_list:
        total_sum += i
    return total_sum

result:int = sum_of_list(lab_list)
print(f'the total sum is: {result}')
print('-'*15)

#Q2 - Answer
def largest_num (lab_list):
    sorted_list = sorted(lab_list)
    print("the largest number in the list is: ",sorted_list[-1])

largest_num(lab_list)
print('-'*15)

#Q3 - Answer
odd_num_list = [i for i in range(1200, 2000, 125) if i % 2 != 0]
print('odd number list are:',odd_num_list)
print('-'*15)

#Q4 - Answer
sliced_list = odd_num_list[:5]
print('the sliced list from odd_num_list to 5th is :', sliced_list)
