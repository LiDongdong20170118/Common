% 导入自定义模块
import sys
sys.path.append('D:\Common')

% 异常处理通用代码
try:
    a = 10;
    b = 0
    print(a)
    c   =   a/b
    print(c)
except:
    print('Wrong Main!')
    import traceback as traceback
    traceback.print_exc()
print("done")