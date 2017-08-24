def bubble_sort(list_object):
    working_list = list_object[:]
    for pass_count in range(len(working_list)-1, 0, -1):
        for step in range(pass_count):
            if working_list[step] > working_list[step+1]:
                working_list[step+1],working_list[step]=working_list[step],working_list[step+1]
    return working_list

def merge_sort(parent_list):
    if len(parent_list) <= 1:
        return parent_list

    left_half = []
    right_half = []

    for each in range(len(parent_list)):
        if each < len(parent_list) / 2:
            left_half.append(parent_list[each])
        else:
            right_half.append(parent_list[each])

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    while len(left) > 0:
        result.append(left.pop(0))
    while len(right) > 0:
        result.append(right.pop(0))

    return result

lst = raw_input("Go ahead and enter your list: ").split(',')

bubble_sorted = bubble_sort(lst)
merge_sorted = merge_sort(lst)

print lst
print bubble_sorted
print merge_sorted