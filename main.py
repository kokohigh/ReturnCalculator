# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def calc_principal(p,r):
    principal = 0
    n = 0
    while n<=4:
        principal += p/(1+r)**n
        n+=1
    return principal


def calc_result(p,r,t):
    result = 0
    n = 0
    while n <= 29:
        result += p/((1+r)**(t-n))
        n+=1
    # Use a breakpoint in the code line below to debug your script.
    return result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("第1种利益：", calc_result(3100 * 12, 0.02, 51))
    print("第1种成本：",calc_principal(24000, 0.02))
    print("第2种利益：", calc_result(2100 * 12, 0.02, 39))
    print("第2种成本：",calc_principal(26000, 0.02))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
