'''

7
abba
summuus
xabba
xabbay
comcom
comwwmoc
comwwtmoc

'''
def check(sp,front,back):
    while front<back:
        if sp[front]==sp[back]:
            front+=1
            back-=1

        elif sp[front]!=sp[back]:
            return False

    return True

def palindrome(sp,front,back):

    while front<back:
        if sp[front]==sp[back]:
            front+=1
            back-=1

        elif sp[front]!=sp[back]:
            front_check = check(sp,front+1,back)
            back_check = check(sp,front,back-1)

            if front_check or back_check:
                return 1

            else:
                return 2

    return 0


T = int(input())
for _ in range(1,T+1):
    sp = input()
    front = 0
    back = len(sp)-1
    print(palindrome(sp,front,back))

