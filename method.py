#%% methodTest
# # f(x) = 2x + 1
# def f(x):
#     return 2*x+1

# print(f(3)+9)

# # 두 정수의 덧셈
# def add(num1, num2):
#     result = num1 + num2
#     print(result)

# add(1,3)

# 1~100까지 print()로 출력하는 메서드
# def print_out():
#     for i in range(100):
#         result = i + 1
#         print(result)

# print_out()

#1~10까지의 합을 구하는 메서드
# def total_sum():
#     sum = 0
#     for i in range(1,11):
#         sum += i
#     return sum

# print("전체 합 : %d" %total_sum())

# 자연수를 음수로 바꿔주는 메서드
# def chg_ngt_num(num1):
#     if num1 > 0:
#         return -num1
#     else:
#         return False

# print(chg_ngt_num(-1))

# #1~n까지의 합을 print()로 출력하는 메서드
# def from1_toN_sum(num):
#     sum = 0
#     # num = int(input("몇 까지의 합을 원하는지 입력 : "))
#     for i in range(1,num+1):
#         sum += i
#     print(sum)
    
# from1_toN_sum(11)

# 홀수를 짝수로 짝수를 홀수로 바꿔주는 메소드
# def chg_even_odd(num):
#     num = int(input("정수를 입력 : "))
#     if num % 2 == 0:
#         print("홀수로 변경되었습니다.")
#         return num + 1
#     else:
#         print("짝수로 변경되었습니다.")
#         return num - 1

# print(chg_even_odd(5))

numlist = []
def sortASC(numlist):
    for e in range(5):
        numlist.append(int(input("다섯개의 정수를 입력하시오 : ")))
    for i in range(len(numlist)-1):
        for j in range(i+1,len(numlist)):
            if numlist[i] > numlist[j]:
                temp = numlist[i]
                numlist[i] = numlist[j]
                numlist[j] = temp
                

sortASC(numlist)
print(numlist)         
        