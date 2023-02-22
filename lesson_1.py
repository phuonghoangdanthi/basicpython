#start: comment
if True:
 print ("True")
else:
 print ("False")

if True:
 print("Answer")
 print("True")
 if False:
  print("ok")
 else:
  print("Answer")
  print("False")

def add(a, b):
    """a: in_money, b: out_money
    homnay la thu bay"""
    '''Note
    ass
    ''' 
    return a + b 
print(add.__doc__)
print("tong tien", add(2000, 300))
#end: comment

