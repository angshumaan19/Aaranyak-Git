class Employee:
    def __init__(self):
        print("3.employee created")
    def __del__(self):
        print("6.destructor called")
def create_object():
    print("2.making object...")
    obj = Employee()
    print("4.function end...")
    return obj

print("1.calling create_object function...")
ob = create_object()
print("5.Program end...")