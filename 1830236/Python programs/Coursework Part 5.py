# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

# Student ID: 20200538

# Date:  29/04/2021

#task 5
data=[[120,0,0],[100,20,0],[100,0,20],[80,20,20],[60,40,20],[40,40,40],[20,40,60],[20,20,80],[20,0,100],[0,0,120]]#data given in the coursework
progress = trailer = retriever = exclude = mark = mark_diff =0

def Histogram(Pass,defer,fail):
    global progress,trailer,retriever,exclude,mark,mark_diff
    mark = defer + fail
    mark_diff = Pass - mark
    # tabulating the data before making the histogram
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



        for x in range(1,len(data)):#reading data from the array
            print(data[x])
            line = data[x]
            #slicing the data from the array
            Pass = line[0]
            defer = line[1]
            fail = line[2]
            mark = defer + fail
            mark_diff = Pass - mark
            if mark_diff == 120:#checking the mark diff so that the correct progression outcome can be made
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
#printing the histogram
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


#main
for x in range(len(data)):
    line=data[x]
    Pass_mark=line[0]
    defer_mark=line[1]
    fail_mark=line[2]
    Histogram(Pass_mark,defer_mark,fail_mark)
Horizontal_Histogram()



