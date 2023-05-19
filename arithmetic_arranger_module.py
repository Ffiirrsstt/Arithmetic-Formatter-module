def if_answer(answer, operator, operand_1, operand_2):
    if answer:
        if operator == '+' :
            answer_ = str( (int(operand_1))+(int(operand_2)) )
        elif operator == '-' :
            answer_ = str( (int(operand_1))-(int(operand_2)) )
    return answer_

def answer_input():
    answer = input('Enter the value you want to calculate? \n[Ex.32 + 8] : ')
# test_0 = 0 + 0 run for check
#     if answer == '0':
#         answer = "0 + 0"
    return answer

def result():
    while True:
        answer = input('Do you want to display the result? \n[YES/NO] : ').lower()
        if answer == 'yes':
            for_return = True
            break
        elif answer == 'no':
            for_return = False
            break
        else:
            print('Please type \'Yes\' or \'No\' only.')
    return for_return

def calculate(*for_cal):
    quit_for_check = False
    while True:

        answer_cal, answer_result = for_cal 
        answer_1, answer_2, answer_3, answer_4 = answer_cal
        operand_1_1, operator_1, operand_2_1 = answer_1.split()
        operand_1_2, operator_2, operand_2_2 = answer_2.split()
        operand_1_3, operator_3, operand_2_3 = answer_3.split()
        operand_1_4, operator_4, operand_2_4 = answer_4.split()

        for check in (operand_1_1, operand_1_2, operand_1_3, operand_1_4, operand_2_1, operand_2_2, operand_2_3, operand_2_4):
            if check.isdigit() == False:
                print('\nError: Numbers must only contain digits\n')
                quit_for_check = True
                break
            elif int(check)>=10000 :
                print('\nError: Numbers cannot be more than four digits\n')
                quit_for_check = True
                break
        if quit_for_check :
            quit_for_check = True
            break

        op_1 = len(str(max(int(operand_1_1), int(operand_2_1))))
        op_2 = len(str(max(int(operand_1_2), int(operand_2_2))))
        op_3 = len(str(max(int(operand_1_3), int(operand_2_3))))
        op_4 = len(str(max(int(operand_1_4), int(operand_2_4))))
        format_1 = '{:>{}}    {:>{}}    {:>{}}    {:>{}}'.format(operand_1_1, (op_1+2),operand_1_2,(op_2+2), operand_1_3, (op_3+2), operand_1_4, (op_4+2))
        format_2 = '{}{:>{}}    {}{:>{}}    {}{:>{}}    {}{:>{}}'.format(
            operator_1, operand_2_1, (op_1+1)
            , operator_2, operand_2_2, (op_2+1)
            , operator_3, operand_2_3, (op_3+1)
            , operator_4, operand_2_4, (op_4+1))

        print('\n')
        print(format_1)
        print(format_2)
        print('-'*(op_1+2)
            , '  ', '-'*(op_2+2)
            , '  ', '-'*(op_3+2)
            , '  ', '-'*(op_4+2))

    # answer
        if answer_result :
            ans_1 = if_answer(answer_result, operator_1, operand_1_1, operand_2_1)
            ans_2 = if_answer(answer_result, operator_2, operand_1_2, operand_2_2)
            ans_3 = if_answer(answer_result, operator_3, operand_1_3, operand_2_3)
            ans_4 = if_answer(answer_result, operator_4, operand_1_4, operand_2_4)
            format_answer = '{:>{}}    {:>{}}    {:>{}}    {:>{}}'.format(
                ans_1, (op_1+2), ans_2, (op_2+2), ans_3, (op_3+2), ans_4, (op_4+2))
            print(format_answer)
        break
    return quit_for_check

def arithmetic_arranger():
    round = 1
    while True:

        print ('\n"Program Usage\"'
        ,'- You can enter a maximum of 5 rounds.'
        ,'- The operator used is either addition (+) or subtraction (-).'
        ,'- The numbers used for addition or subtraction are integers with a maximum of 4 digits.'
        ,'- The numbers used for calculation must be positive integers.'
        ,'\nthis is rond {}'.format(round),sep='\n')
        quit = input('Do you want to quit the program? \n[YES/NO] : ').lower()
        if quit == 'yes':break
        elif quit == 'no' :round+=1
        else :
            print('Please type \'Yes\' or \'No\' only.')
            continue
        if round==7:
            print('\nError: Too many problems\n')
            break
        answer_1 = answer_input()
        if '+' in answer_1 !=0 or '-' in answer_1 :
            pass
        else :
            print('\nError: Operator must be \'+\' or \'-\'\n')
            break
        answer_2 = answer_input()
        if '+' in answer_2 !=0 or '-' in answer_2 :
            pass
        else :
            print('\nError: Operator must be \'+\' or \'-\'\n')
            break
        answer_3 = answer_input()
        if '+' in answer_3 !=0 or '-' in answer_3 :
            pass
        else :
            print('\nError: Operator must be \'+\' or \'-\'\n')
            break
        answer_4 = answer_input()
        if '+' in answer_4 !=0 or '-' in answer_4 :
            pass
        else :
            print('\nError: Operator must be \'+\' or \'-\'\n')
            break
        
        answer_result = result()
        for_cal = [answer_1,answer_2,answer_3,answer_4],answer_result
        quit_return = calculate(*for_cal)
        if quit_return:
            break
