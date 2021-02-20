import pytest

# 使用返回值，参数列表
@pytest.fixture(params=[1, 2, 3])
def init_xx(request):
    return request.param

class Test_zz:
    # 开始
    def setup_class(self):
        print("...setup_class")
    # 结束
    def teardown_class(self):
        print("...teardown_class")
    # 参数引用
    def test_a(self, init_xx):
        pytest.assume(init_xx == 4)