def bubble_sort(seq):
    count = 0
    for i in range(len(seq) - 1, 0, -1):
        no_swap = True
        for j in range(0, i):
            print(seq)
            count += 1
            if seq[j + 1] < seq[j]:
                seq[j], seq[j + 1] = seq[j + 1], seq[j]
                no_swap = False
        if no_swap:
            return count


seq = [50, 3, 6, -10, 345, 234, 5, 67, -113, 23, 456, 2, 9, 8, 55]
print('before sort:', seq)

count = bubble_sort(seq)

print('after sort:', seq)
print('count:', count)
