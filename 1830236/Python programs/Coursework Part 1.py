# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

# Student ID: 20200538

# Date:  29/04/2021


#task 1
#data to be inputed by the user
Pass=int(input('Please enter your credits at pass:'))
defer=int(input('Please enter your credits at defer:'))
fail=int(input('Please enter your credits at fail:'))

mark=defer+fail#total defer credits and fail credits
mark_diff=Pass-mark#Credits needed to be passed or the number of credits more than the minimin amount to be passed
#checking for the progression output
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
