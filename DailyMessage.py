class DailyMessage:
    def __init__(self):
        self.message = ""

    def get_message(self):
        self.message = str(input("enter today's message : "))

    def print_message(self):
        print("message in uppercase :",self.message.upper())

daily_text = DailyMessage()

daily_text.get_message()
daily_text.print_message()

class helper_session:
    def __init__(self):
        print("daily data helper session created")

    def __del__(self):
        print("daily data helper session ended")

def create_session():
     print("making helper session")
     session = helper_session()
     print("session is ready")
     return session

print("")
print("calling create session function")
session_obj = create_session()
print("program is still running")

class pair_finder:
    def finding_pair(self, nums, target):
        lookup = {}
        for index,num in enumerate(nums):
            needed_number = target - num
            if needed_number in lookup:
                return lookup[needed_number], index

            lookup[num]  = index


        return None

numbers = (10,20,30,40,50,60,70,80,90)

target_value = int(input("enter target sum to search"))


result = pair_finder().finding_pair(numbers,target_value)

if result is not None:
    print("index1 = %d,index2 = %d" % result)
else:
    print("pair is not found for this number")

del session_obj
print("program end")