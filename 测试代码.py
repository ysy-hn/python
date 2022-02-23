# 知识
# 11.1.2 可通过的测试,要为函数编写测试用例，可先导入模块unittest以及要测试的函数，
# 再创建一个继承unittest.TestCase的类，并编写一系列方法对函数行为的不同方面进行测试。
# 11.1.4 测试未通过时怎么办,应修复导致测试不能通过的代码.方法名必须以test_打头,unittest.main()结尾。
# unittest Module中的断言方法
# assertEqual(a, b) 核实a == b
# assertNotEqual(a, b) 核实a != b
# assertTrue(x) 核实x为True
# assertFalse(x) 核实x为False
# assertIn(item, list) 核实item在list中
# assertNotIn(item, list) 核实item不在list中
# 11.2.4 方法 setUp()，如果你在TestCase类中包含了方法setUp()，Python将先运行它，
# 再运行各个以test_打头的方法。测试自己编写的类时，方法setUp()让测试方法编写起来更容易：
# 可在setUp()方法中创建一系列实例并设置它们的属性，再在测试方法中直接使用这些实例。

# 例题
# 1
import unittest
from city_functions import city_country

class NameTestCase(unittest.TestCase):
    def test_city_country_1(self):
        name = city_country("北京", "中国")
        self.assertEqual(name, "北京 , 中国")

unittest.main()

# 2
import unittest
from city2_country import city2_country
from city2_country import city_country_population

class NameTestCase(unittest.TestCase):
    def test_city2_country(self):
        name = city2_country("北京", "中国", '5000')
        self.assertEqual(name, "北京，中国-人口:50000")
    def test_city_country_population(self):
        name = city_country_population("北京", "中国", "5000000")
        self.assertEqual(name, "北京、中国-人口=5000000")

unittest.main()

# 3
import unittest

class Employee():
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def give_raise(self, raise_pay=5000):
        self.pay += raise_pay

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.test_employee = Employee("john", "smith", 8000)

    def test_give_default_raise(self):
        self.test_employee.give_raise()
        self.assertEqual(13000, self.test_employee.pay)

    def test_give_custom_raise(self):
        self.test_employee.give_raise(12000)
        self.assertEqual(20000, self.test_employee.pay)

unittest.main()


