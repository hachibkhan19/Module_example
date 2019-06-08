def find_fib(n):

    if n <= 2:

        return 1

    fib_x, fib_next = 1, 1

    i = 3

    while i <= n:

        i += 1

        fib_x, fib_next = fib_next, fib_x + fib_next

    return fib_next


def list_fib(n):

    find_list = [1, 1]

    fib_x, fib_next = 1, 1

    if n <= 2:

        return find_list[:n]

    i = 3

    while i <= n:

        i += 1

        fib_x, fib_next = fib_next, fib_x + fib_next

        find_list.append(fib_next)

    return find_list

for x in range(1, 11):

    print(find_fib(x))
    
print(list_fib(1))

print(list_fib(2))

print(list_fib(10))


