import random
def codebreaker_random():
    value_1st_stone = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    # input('Press the space bar: ')
    question = random.choice(value_1st_stone)
    result = ' '
    for n1 in range(1, (question-1)):
        for n2 in range(1, 21):
            pair = n1 + n2
            if n2 <= n1:
                continue
            elif pair > question:
                break
            elif question % pair == 0:
                result += str(n1) + str(n2)
    print(f'{question} -{result}')

codebreaker_random()  # строку удадить при решении вопроса ниже
# def codebreaker_manual():  # так и не решил вопрос работы кода при вводе не цифровых символов, выдает ошибку в стр.34
#     # print('Number entered:', question)
#     result = ' '
#     for n1 in range(1, (int(question) - 1)):
#         for n2 in range(1, 21):
#             pair = n1 + n2
#             if n2 <= n1:
#                 continue
#             elif pair > int(question):
#                 break
#             elif int(question) % pair == 0:
#                 result += str(n1) + str(n2)
#     print(f'{question} -{result}')
#
# question = input('Enter a positive integer between 3 and 20 and press Enter: ')
# if int(question) < 3 or int(question) > 20:
#     print('An invalid number is entered, a random number will be selected')
#     codebreaker_random()
# elif int(question) >= 3 and int(question) <= 20:
#     codebreaker_manual()
# elif type(question) != int:
#     print('An invalid number is entered, a random number will be selected')



