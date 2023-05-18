args = {
    'arg1': "foo",
    'arg2': "bar",
    'arg3': "baz",
}

def func1(arg1=1, arg2=2, arg3=3):
	print(arg1)
	print(arg2)
	print(arg3)

print('普通に渡すとリストのときと同様に、1つ目の引数にディクショナリが丸ごと与えられる')
func1(args)

print('---------------------------------------------')

print('argsにアスタリスクを2つ指定することで辞書の値を引数名として与えられる')
func1(**args)

