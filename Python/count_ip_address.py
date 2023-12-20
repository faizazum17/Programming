#function that recieve two ipV4 addresses in string format and returns number of addresses between them
def ips_between(start, end):
    #your code here
    start_list = start.split(".")
    end_list = end.split(".")
    start_num = 0
    end_num = 0
    for i in range(len(start_list)):
        start_num += int(start_list[i]) * (256 ** (3-i))
        end_num += int(end_list[i]) * (256 ** (3-i))
    return end_num - start_num

#test
print(ips_between("10.0.0.0", "10.0.0.50"))
print(ips_between("20.0.0.10", "20.0.1.0"))