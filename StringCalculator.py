def processCustomDelimiter(ip_data):
    delimiter = ip_data[2]
    numbers_part = ip_data.split('\n')[1]
    return sum_data(numbers_part.split(delimiter))

def processDelimiter(data_ip):
    data = data_ip.replace('\n',',').split(',')
    return sum_data(data)

def sum_data(list_data):
    sum = 0
    for i in list_data:
        if int(i)<1000:
            sum += int(i)
    return sum

def check_delimiter(ip):
    if "//" in ip:
        return processCustomDelimiter(ip)
    if "\n" in ip:
        return processDelimiter(ip)
    return 0

def add(ip_data):
    if not ip_data:
        return 0
    data = ip_data.split(',')
    ret = check_delimiter(ip_data)
    if ret == 0:
        return sum_data(data)
    return ret
