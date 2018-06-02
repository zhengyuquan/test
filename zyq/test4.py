#!/usr/bin/python
# -*- coding:UTF-8 -*-

# 抽象工厂模式

# 家具类
class Furniture():
    def produce(self):
        pass

# 椅子类
class Chair(Furniture):
    def produce(self):
        print "生产一把椅子"

# 桌子类
class Table(Furniture):
    def produce(self):
        print "生产一张桌子"

# 颜色类
class Color():
    def getColor(self):
        pass

# 红色类
class Red(Color):
    def getColor(self):
        print "添加红色"

# 蓝色类
class Blue(Color):
    def getColor(self):
        print "添加蓝色"

# 抽象工厂
class AbstractFactor():
    def produceFur(self):
        pass
    def fillColor(self):
        pass

# 家具工厂
class FurFactor(AbstractFactor):
    def produceFur(self,furType):
        if furType == 'Chair':
            return Chair()
        elif furType == 'Table':
            return Table()
        else:
            print '还不能生产该类家具'

    def fillColor(self,color):
        print '请选择配色工厂上色'

class ColorFactor(AbstractFactor):
    def fillColor(self,color):
        if color == 'Red':
            return Red()
        elif color == 'Blue':
            return Blue()
        else:
            print "暂不支持该颜色"

    def produceFur(self,furType):
        print '请选择家具工厂生产'

# 生成器类
class FactoryProducer():
    @staticmethod
    def getFactory(choice):
        if choice == 'Furniture':
            return FurFactor()
        elif choice == 'Color':
            return ColorFactor()
        else:
            print '暂不支持该工厂'

# 获取家具工厂
furFactor = FactoryProducer.getFactory('Furniture')
# 获取 椅子对象
chair1 = furFactor.produceFur('Chair')
# 调用 produce 方法生产一把椅子
chair1.produce();

# 获取调色工厂
colorFactor = FactoryProducer.getFactory('Color')
# 获取 蓝色 类
color1 = colorFactor.fillColor('Blue')
# 添加蓝色
color1.getColor()