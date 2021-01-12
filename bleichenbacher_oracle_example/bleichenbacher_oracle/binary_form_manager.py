
def to_binary_form(n, size):
   base = "{0:b}".format(n)
   # i wanted the length is size: if binary form starts with 0, it will be
   # deleted: i want 6 = 00000110 and not 6 = 110
   diff = size - len(base)
   s = "0" * diff
   return s + base
