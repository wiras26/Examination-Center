# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

# Student ID: 20200538

# Date:  29/04/2021

#task 2
credits=[0,20,40,60,80,100,120]#List used to store the credits which are acceptable
Total_incorrect=False
#validation
def Validation():
    global Total_incorrect
    while True:
        try:
            Pass=int(input('Please enter your credits at pass:'))
        except ValueError:#checking whether the entered data is in the correct format
            print('Integer required')
            continue

        try:
            defer = int(input('Please enter your credits at defer:'))
        except ValueError:
            print('Integer required')
            continue

        try:
            fail=int(input('Please enter your credits at fail:'))
        except ValueError:
            print('Integer required')
            break
        break

    for x in range(7):
        if Pass==credits[x]:#checking whether the entered data is in the given range listed above
            valid_pass=True
            break
        else:
            valid_pass=False
    if valid_pass==False:
        print('Pass out of range')

    for x in range(7):
        if defer == credits[x]:
            valid_defer = True
            break
        else:
            valid_defer = False

    if valid_defer==False:
        print('Defer out of range')

    for x in range(7):
        if fail == credits[x]:
            valid_fail = True
            break
        else:
            valid_fail = False
    if valid_fail==False:
        print('Fail out of range')

    total_credits=Pass+defer+fail
    if total_credits!=120:#checking if the total of pass defer and fail is correct
        print('Total incorrect')
        Total_incorrect=True
    mark=defer+fail
    mark_diff=Pass-mark
    if Total_incorrect==False:#if total correct the correct progression outcome is displayed
        if mark_diff==120:
            print('Progress')
        elif mark_diff==80:
            print('Progress (module trailer)')
        elif mark_diff==40:
            print('Do not Progress - module retriever')
        elif mark_diff==0:
            print('Do not Progress - module retriever')
        elif mark_diff==-40 and fail!=80:
            print('Do not Progress - module retriever')
        elif fail==80 or fail==100 or fail==120:
            print('Exclude')
        elif mark_diff==-80 and fail!=100:
            print('Do not Progress - module retriever')
        elif Pass==0 and fail!=100 and fail!=120 and fail!=80:
            print('Do not Progress - module retriever')
Validation()
