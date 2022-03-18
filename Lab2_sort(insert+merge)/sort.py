def insertion_sort(given_list):
    j = len(given_list)
    for el in range(1, j):
        key = given_list[el]
        i = el-1
        while i >= 0 and given_list[i] > key:
            given_list[i+1] = given_list[i]
            i = i-1
        given_list[i+1] = key
    return given_list

# Merge Sort


def merge(given_list, start, mid_point, end):
    # n1=mid_point-start+1
    # n2=end-mid_point
    left_array = given_list[start:mid_point+1]
    right_array = given_list[mid_point+1:end+1]
    i = 0
    j = 0
    for k in range(start, end+1):
        if i < len(left_array) and j < len(right_array):
            if left_array[i] <= right_array[j]:
                given_list[k] = left_array[i]
                i += 1
            else:
                given_list[k] = right_array[j]
                j += 1
        else:
            if i >= len(left_array):
                given_list[k] = right_array[j]
                j += 1
            elif j >= len(right_array):
                given_list[k] = left_array[i]
                i += 1
            else:
                continue
    return given_list


def merge_sort(given_list, start, end):
    if start < end:
        mid_point = (start+end)//2
        merge_sort(given_list, start, mid_point)
        merge_sort(given_list, mid_point+1, end)
        merge(given_list, start, mid_point, end)
    return given_list
