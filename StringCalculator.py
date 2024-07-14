def process_delimiter(ip_data):
        delimiter = ip_data[2]
        number = ip_data.split('\n')
        numbers_part = ip_data.split('\n')[1]
        return numbers_part.split(delimiter)

def sum_data(list_data):
    sum = 0
    for i in list_data:
        if i.isdigit() and int(i)<1000:
            sum += int(i)
    return sum

def add(ip_data):
    
    if not ip_data:
        return 0
        
    data = ip_data.split(',')
    if "//" in ip_data:
        return sum_data(process_delimiter(ip_data))
        
    return sum_data(data)
