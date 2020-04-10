operate_times = int(input("Please input number of times: "))
for i in range(operate_times):
    expo = i + 1
    textspace = operate_times - i - 1
    print(" "*textspace + "*" * i + "*" * expo)