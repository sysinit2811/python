#n = ''
#
#input_num = raw_input('input a num: ')
# while x != 'pc':
#    num = num + int(input_num)
#    n++
#    input_num = input('input a num: ')
# print num
# pinrt n

num = 0
size = 0

input_str = raw_input('input a number(end with blank): ')
while input_str:
    size = size + 1.0
    num = num + int(input_str)

    input_str = raw_input('input a number(end with blank): ')
print "Average: %f" %(num / size)