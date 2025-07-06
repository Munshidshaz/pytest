def day_generator():
    L = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    i = 0
    while True:
        x = L[i]
        i = (i + 1) % 7
        yield x

# Example usage:
# days = day_generator()
# print(next(days))  # Sunday
# print(next(days))  # Monday
# ... and so on
days= day_generator()
print(next(days))
print(next(days))
print(next(days))