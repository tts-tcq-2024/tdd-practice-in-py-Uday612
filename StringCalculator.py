def add(ip_data):
    sum = 0
    
    if not ip_data:
        return 0
    data = ip_data.split(',')
    for i in data:
        if i.isdigit() and int(i)<1000:
            sum += int(i)
    return sum
