def countdown(n):
    while n > 0:
        n -= 1
        yield n


list(countdown(3))
