

def max_pairwise_product(numbers):
    n = len(numbers)
    fmax = 0
    smax = 0
    for i in range(n):
        if numbers[i]>fmax:
            smax=fmax
            fmax=numbers[i]
        else:
            if numbers[i]>smax:
                smax=numbers[i]
    return fmax*smax


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))