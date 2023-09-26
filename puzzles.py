import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def print_plt(array, title, name, arrow_ax = None, arrow_di = None):
    fig = plt.figure(figsize=(24,24))
    sns_plot = sns.heatmap(array, annot = True, cbar = False, annot_kws={"fontsize":160})
    x_line = [0.5, 3.5, 3.5, 1.5, 1.5, 3.5, 3.5, 0.5, 0.5]
    y_line = [0.5, 0.5, 1.5, 1.5, 2.5, 2.5, 3.5, 3.5, 0.5]
    plt.plot(x_line,y_line, linewidth=50, color='r', alpha=0.5)
    if arrow_ax and arrow_di:
        if arrow_di == "left":
            direction = -0.8
        elif arrow_di == "right":
            direction = 0.8
        plt.arrow(2.5, (arrow_ax + 1)/3 - 0.5, 0, direction, head_width=0.08, lw=50, length_includes_head = True, color = 'y')
    plt.title(title, fontsize=100)
    plt.xticks([])
    plt.yticks([])
    plt.savefig("F:\\b站\\imgs\\" + str(name) + ".jpg")
    # plt.show()
    plt.close()


def exchange(lis, index, direction):
    if direction == "left":
        lis[index - 2 : index + 1] = [lis[index], lis[index - 2], lis[index - 1]]
    elif direction == "right":
        lis[index : index + 3] = [lis[index + 1], lis[index + 2], lis[index]]
    else:
        print("Direction can be only left or right.")
        return
    return lis


def operates(origin, target, operate):
    if len(origin) < 2 or len (target) < 2:
        print("The len of the input list must be longer than 1.")
        return
    elif len(origin) != len(set(origin)) or len(target) != len(set(target)):
        print("Elements in an input list can't repeat.")
        return
    elif set(origin) != set(target):
        print("The elements of the 2 input lists must be the same.",set(origin),set(target))
        return
    elif len(origin) == 2:
        if origin != target:
            print("There is no solution to this puzzle.")
            return
        else:
            return operate
    else:
        if origin == target:
            return operate
        elif origin[0] == target[0]:
            return operates(origin[1:], target[1:], operate)
        else:
            index_target = origin.index(target[0])
            while index_target > 1:
                operate.append([target[0], "left"])
                exchange(origin, index_target, "left")
                index_target -= 2
            if index_target == 1:
                operate.append([origin[0], "right"])
                exchange(origin, 0, "right")
            return operates(origin[1:], target[1:], operate)

        
def array2list(array):
    result = list(array[0]) + [array[1][3], array[1][2], array[1][1]] + list(array[2][1:4]) + [array[3][3], array[3][2], array[3][1], array[3][0], array[2][0], array[1][0]]
    return result


def list2array(lis):
    result = np.array([lis[0:4],[lis[15],lis[6],lis[5],lis[4]],[lis[14],lis[7],lis[8],lis[9]],[lis[13],lis[12],lis[11],lis[10]]])
    return result


def huarongdao(origin, target):# Only work for 4th level puzzle
    origin_list = array2list(origin)
    target_list = array2list(target)
    origin_list_new = origin_list.copy()
    origin_list_new.remove(0)
    target_list_new = target_list.copy()
    target_list_new.remove(0)
    operates_list = operates(origin_list_new, target_list_new, [])
    tmp = origin
    tmp_list = origin_list
    title = "Start"
    name = 0
    print_plt(tmp, title, str(name) + "_normal")
    for operate_num, operate in enumerate(operates_list):
        print(operate_num, operate, name)
        title = "Operation " + str(operate_num + 1) + ": " + str(operate[0]) + ", " + operate[1]
        number = operate[0]
        index_number = tmp_list.index(number)
        index_0 = tmp_list.index(0)
        if operate[1] == "left":
            if index_number in [0, 1, 2, 3, 4, 7, 10]:
                if index_number < 5:
                    position = 5
                else:
                    position = index_number + 1
                while index_number != position or index_0 != position - 3:
                    tmp_list[index_0], tmp_list[(index_0 - 1)%16] = tmp_list[(index_0 - 1)%16], tmp_list[index_0]
                    tmp = list2array(tmp_list)
                    name += 1
                    print_plt(tmp, title, str(name) + "_normal")
                    index_number = tmp_list.index(number)
                    index_0 = tmp_list.index(0)
                name += 1
                print_plt(tmp, title, str(name) + "_operate", position, operate[1])
                tmp_list[position], tmp_list[position - 3] = tmp_list[position - 3], tmp_list[position]
                tmp = list2array(tmp_list)
                name += 1
                print_plt(tmp, title, str(name) + "_operate", position, operate[1])
                index_number = tmp_list.index(number)
                index_0 = tmp_list.index(0)
            elif index_number in [5, 8, 11]:
                position = index_number
                while index_number != position or index_0 != position - 3:
                    if position - 3 < index_0 < position:
                        tmp_list[index_0], tmp_list[(index_0 - 1)%16] = tmp_list[(index_0 - 1)%16], tmp_list[index_0]
                    elif index_0 < position - 3 or index_0 > position:
                        tmp_list[index_0], tmp_list[(index_0 + 1)%16] = tmp_list[(index_0 + 1)%16], tmp_list[index_0]
                    tmp = list2array(tmp_list)
                    name += 1
                    print_plt(tmp, title, str(name) + "_normal")
                    index_number = tmp_list.index(number)
                    index_0 = tmp_list.index(0)
                name += 1
                print_plt(tmp, title, str(name) + "_operate", position, operate[1])
                tmp_list[position], tmp_list[position - 3] = tmp_list[position - 3], tmp_list[position]
                tmp = list2array(tmp_list)
                name += 1
                print_plt(tmp, title, str(name) + "_operate", position, operate[1])
                index_number = tmp_list.index(number)
                index_0 = tmp_list.index(0)
            elif index_number in [6, 9, 12, 13, 14, 15]:
                if index_number > 11:
                    position = 11
                else:
                    position = index_number - 1
                while index_number != position or index_0 != position - 3:
                    tmp_list[index_0], tmp_list[(index_0 + 1)%16] = tmp_list[(index_0 + 1)%16], tmp_list[index_0]
                    tmp = list2array(tmp_list)
                    name += 1
                    print_plt(tmp, title, str(name) + "_normal")
                    index_number = tmp_list.index(number)
                    index_0 = tmp_list.index(0)
                name += 1
                print_plt(tmp, title, str(name) + "_operate", position, operate[1])
                tmp_list[position], tmp_list[position - 3] = tmp_list[position - 3], tmp_list[position]
                tmp = list2array(tmp_list)
                name += 1
                print_plt(tmp, title, str(name) + "_operate", position, operate[1])
                index_number = tmp_list.index(number)
                index_0 = tmp_list.index(0)
        elif operate[1] == "right":
            if index_number in [0, 1, 4, 7, 14, 15]:
                if index_number < 2 or index_number > 13:
                    position = 2
                else:
                    position = index_number + 1
                while index_number != position or index_0 != position + 3:
                    tmp_list[index_0], tmp_list[(index_0 - 1)%16] = tmp_list[(index_0 - 1)%16], tmp_list[index_0]
                    tmp = list2array(tmp_list)
                    name += 1
                    print_plt(tmp, title, str(name) + "_normal")
                    index_number = tmp_list.index(number)
                    index_0 = tmp_list.index(0)
                name += 1
                print_plt(tmp, title, str(name) + "_operate", position, operate[1])
                tmp_list[position], tmp_list[position + 3] = tmp_list[position + 3], tmp_list[position]
                tmp = list2array(tmp_list)
                name += 1
                print_plt(tmp, title, str(name) + "_operate", position, operate[1])
                index_number = tmp_list.index(number)
                index_0 = tmp_list.index(0)
            elif index_number in [2, 5, 8]:
                position = index_number
                while index_number != position or index_0 != position + 3:
                    if position < index_0 < position + 3:
                        tmp_list[index_0], tmp_list[(index_0 + 1)%16] = tmp_list[(index_0 + 1)%16], tmp_list[index_0]
                    elif index_0 < position or index_0 > position + 3:
                        tmp_list[index_0], tmp_list[(index_0 - 1)%16] = tmp_list[(index_0 - 1)%16], tmp_list[index_0]
                    tmp = list2array(tmp_list)
                    name += 1
                    print_plt(tmp, title, str(name) + "_normal")
                    index_number = tmp_list.index(number)
                    index_0 = tmp_list.index(0)
                name += 1
                print_plt(tmp, title, str(name) + "_operate", position, operate[1])
                tmp_list[position], tmp_list[position + 3] = tmp_list[position + 3], tmp_list[position]
                tmp = list2array(tmp_list)
                name += 1
                print_plt(tmp, title, str(name) + "_operate", position, operate[1])
                index_number = tmp_list.index(number)
                index_0 = tmp_list.index(0)
            elif index_number in [3, 6, 9, 10, 11, 12, 13]:
                if index_number > 8:
                    position = 8
                else:
                    position = index_number - 1
                while index_number != position or index_0 != position + 3:
                    tmp_list[index_0], tmp_list[(index_0 + 1)%16] = tmp_list[(index_0 + 1)%16], tmp_list[index_0]
                    tmp = list2array(tmp_list)
                    name += 1
                    print_plt(tmp, title, str(name) + "_normal")
                    index_number = tmp_list.index(number)
                    index_0 = tmp_list.index(0)
                name += 1
                print_plt(tmp, title, str(name) + "_operate", position, operate[1])
                tmp_list[position], tmp_list[position + 3] = tmp_list[position + 3], tmp_list[position]
                tmp = list2array(tmp_list)
                name += 1
                print_plt(tmp, title, str(name) + "_operate", position, operate[1])
                index_number = tmp_list.index(number)
                index_0 = tmp_list.index(0)
    if tmp_list == target_list:
        return
    tmp_list_new = tmp_list.copy()
    tmp_list_new.remove(0)
    index_tmp = target_list_new.index(tmp_list_new[0])
    rest_length = len(tmp_list_new) - index_tmp
    if rest_length == 0:
        if tmp_list_new != target_list_new:
            print("Something is wrong.")
            return
        else:
            if tmp_list.index(0) > target_list.index(0):
                direction = -1
            else:
                direction = 1
    elif tmp_list_new[rest_length:] + tmp_list_new[:rest_length] != target_list_new:
        print("Something is wrong.")
        return
    else:
        if index_tmp > len(tmp_list)/2:
            direction = 1
        else:
            direction = -1
    title = "Last Step"
    while tmp_list != target_list:
        tmp_list[index_0], tmp_list[(index_0 + direction)%16] = tmp_list[(index_0 + direction)%16], tmp_list[index_0]
        tmp = list2array(tmp_list)
        name += 1
        print_plt(tmp, title, str(name) + "_normal")
        index_number = tmp_list.index(number)
        index_0 = tmp_list.index(0)
    name += 1
    print_plt(tmp, title, str(name) + "_operate")
    
    
if __name__ == "__main__":
    a = np.array([[5,15,4,2],[7,1,12,0],[14,3,13,6],[11,8,10,9]])
    b = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[0,13,14,15]])
    huarongdao(a, b)