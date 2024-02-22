'''
Given a dictionary,print key found if key is found in a dict else use exception handling to show its absence.
'''
my_dict={'one':1,'two':2,'three':3}
try:
    key=input("Enter the key:\n")
    if key not in my_dict:
        raise Exception()
    else:
        print("key found")
except Exception:
    print("key not found")