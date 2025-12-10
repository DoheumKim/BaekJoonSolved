math = [30, 50, 90, 80]
name = ['kim', 'lee', 'park', 'bae']
# fail_list = [name[i] for i in range(len(math)) if(math[i]<80)]
# fail_list = [name[math.index(i)] for i in math if(i<80)]

fail_list = [i for i in math if (i<80)]
fail_name = [name[math.index(i)] for i in fail_list]
print(fail_name)
