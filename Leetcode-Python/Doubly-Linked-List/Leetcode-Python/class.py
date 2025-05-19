class Coookie:
    def __init__(self, color):
        self.color = color
    
    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color
    
cookie_one = Coookie('Green')
cookie_two = Coookie('Blue')

print('Cookie one %s' %cookie_one.get_color())
print('Cookie two %s' %cookie_two.get_color())

cookie_one.set_color('yellow')
print('Cookie one %s' %cookie_one.get_color())
print('Cookie two %s' %cookie_two.get_color())