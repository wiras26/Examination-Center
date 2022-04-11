# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

# Student ID: 20200538

# Date:  29/04/2021

#task 4
progress = trailer = retriever = exclude = mark = mark_diff =0

def Histogram(Pass,defer,fail):
    global progress,trailer,retriever,exclude,mark,mark_diff
    mark = defer + fail
    mark_diff = Pass - mark
    #tabulating the data before making the histogram
    if mark_diff==120:#checking the mark diff so that the correct progression outcome can be made
        print('Progress')
        progress = progress + 1
    elif mark_diff==80:
        print('Progress (module trailer)')
        trailer = trailer + 1
    elif mark_diff==40:
        print('Do not Progress - module retriever')
        retriever = retriever + 1
    elif mark_diff==0:
        print('Do not Progress - module retriever')
        retriever = retriever + 1
    elif mark_diff==-40 and fail!=80:
        print('Do not Progress - module retriever')
        retriever = retriever + 1
    elif fail==80 or fail==100 or fail==120:
        print('Exclude')
        exclude = exclude + 1
    elif mark_diff==-80 and fail!=100:
        print('Do not Progress - module retriever')
        retriever = retriever + 1
    elif Pass==0 and fail!=100 and fail!=120 and fail!=80:
        print('Do not Progress - module retriever')
        retriever = retriever + 1

    choice=input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view the results:")
    while choice=='y':#Loop repeats until user  finishes entering data
        Pass = int(input('Enter your total PASS credits:'))
        defer = int(input('Enter your total DEFER credits:'))
        fail = int(input('Enter your total FAIL credits:'))
        mark = defer + fail
        mark_diff = Pass - mark
        if mark_diff == 120:
            print('Progress')
            progress=progress+1
        elif mark_diff == 80:
            print('Progress (module trailer)')
            trailer=trailer+1
        elif mark_diff == 40:
            print('Do not Progress - module retriever')
            retriever=retriever+1
        elif mark_diff == 0:
            print('Do not Progress - module retriever')
            retriever=retriever+1
        elif mark_diff == -40 and fail != 80:
            print('Do not Progress - module retriever')
            retriever=retriever+1
        elif fail == 80 or fail == 100 or fail == 120:
            print('Exclude')
            exclude=exclude+1
        elif mark_diff == -80 and fail != 100:
            print('Do not Progress - module retriever')
            retriever=retriever+1
        elif Pass == 0 and fail != 100 and fail != 120 and fail != 80:
            print('Do not Progress - module retriever')
            retriever=retriever+1
        choice = input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view the results:")

#printing the horizontal histogram
def Horizontal_Histogram():
    print('Horizontal Histogram')
    print('Progress',progress,':',end='')
    for y in range(progress):
        print('*',end='')
    print('')
    print('Trailer',trailer,':',end='')
    for y in range(trailer):
        print('*',end='')
    print('')
    print('Retriever',retriever,':',end='')
    for y in range(retriever):
        print('*',end='')
    print('')
    print('Excluded',exclude,':',end='')
    for y in range(exclude):
        print('*',end='')
    print('')
    total=progress+trailer+retriever+exclude

    print(total,' outcomes in total.')
    print('_____________________________________')
    return total

#print the vertical histogram
def Vertical_Histogram(total):
    global progress,trailer,retriever,exclude
    space='   '
    print('Progress',' ','Trailing',' ','Retriever',' ','Excluded')
    for x in range(total):#histogram is printed line by line row wise
        if progress > 0:
            print(space, '*', end='')
            progress = progress - 1
        else:
            print(space,' ', end='')
        if trailer > 0:
            print(space, space, '*', end='')
            trailer = trailer - 1
        else:
            print(space,space,' ', end='')
        if retriever > 0:
            print(space, space, space, '*', end='')
            retriever = retriever - 1
        else:
            print(space, space, space, ' ', end='')
        if exclude > 0:
            print(space, space, space, '*')
            exclude = exclude - 1
        else:
            print(space)

#main
print('Staff version with Histogram')
Pass_mark=int(input('Enter your total PASS credits:'))
defer_mark=int(input('Enter your total DEFER credits:'))
fail_mark=int(input('Enter your total FAIL credits:'))
Histogram(Pass_mark,defer_mark,fail_mark)
Tot=Horizontal_Histogram()
Vertical_Histogram(Tot)