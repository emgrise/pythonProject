text = input("New string: ")
list = [[]]
textsp = text.split(' ')
list.append(textsp)

main_list = [[]]
new_list = [[]]
for i in range(len(list)):
    for j in range(len(list[i])):
        main_list = list[i][j]
        print(main_list[i][j])
rev = -1
for i in range(len(main_list)):
    for j in range(len(main_list[i])):

        if 'abcdefghijklmnopqrstuvwxyzABCDIFGHIJKLMNOPQRSTUVWXYZ'.find(main_list[i]) != -1:
            new_list[i][j] = main_list[i][rev]
            rev += -1
        else: new_list[i][j] = main_list[i][j]
    print(new_list)










