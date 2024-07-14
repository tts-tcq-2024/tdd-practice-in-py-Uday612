def add(*ip_data):
    sum = 0
    if not ip_data:
        return 0
    for i in ip_data:
        if i.isdigit():
            sum += int(i)
    return sum
