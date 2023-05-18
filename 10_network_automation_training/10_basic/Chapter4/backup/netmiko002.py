args = ["foo", "bar", "baz"]

def func1(arg1=1, arg2=2, arg3=3):
    print(arg1)
    print(arg2)
    print(arg3)

print('普通に渡すと1つ目の引数にリストが丸ごと与えられる')
func1(args)

print('---------------------------------------------')

print('引数にアスタリスクをつけることでリストを展開し、各引数に要素が与えられる')
func1(*args)