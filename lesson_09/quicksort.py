def partition(seq, start_index, end_index):
    pivot = start_index

    for i in range(start_index+1, end_index+1):
        if seq[i] < seq[start_index]:
            pivot += 1
            seq[i], seq[pivot] = seq[pivot], seq[i]
    seq[start_index], seq[pivot] = seq[pivot], seq[start_index]
    return pivot


def quick_sort(seq, start_index, end_index):

    print(seq)

    if start_index >= end_index:
        return

    pivot = partition(seq, start_index, end_index)
    quick_sort(seq, start_index, pivot-1)
    quick_sort(seq, pivot+1, end_index)


seq = [50, 3, 6, -10, 345, 234, 5, 67, -113, 23, 456, 2, 9, 8, 55]
print('before sort:', seq)

quick_sort(seq, 0, len(seq)-1)

print('after sort:', seq)
