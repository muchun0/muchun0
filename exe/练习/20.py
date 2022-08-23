'''定义一个具有生成器的类，它可以迭代给定范围0到n之间的数字，这些数字可以被7整除。
输入：7
输出：0  7   14
(问题答案对不上，出的有问题)'''
class Divisible:

    def by_seven(self, n):
        for number in range(1,n + 1):
            if number % 7 == 0: yield number


divisible = Divisible()
generator = divisible.by_seven(int(input("Please insert a number. --> ")))
for number in generator:
    print(number)