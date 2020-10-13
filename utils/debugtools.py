args = 0

def init(argjson : dict()):
    global args 
    args = argjson

def c_settings(settjson : dict()):
    if args.settings:
        print("\nHeader Evaluated Settings")

        for i in settjson.keys():
            print(f'{i}: {settjson[i]}')

def c_void():
    if args.void:
        print('\n')
        exit()

def c_config(settjson : dict()):
    if args.settings:
        print("\nConfig JSON Settings:")

        for i in settjson.keys():
            print(f'{i}: {settjson[i]}')