from src.args import _args
from src.settings import _settings

def c_settings():
    if _args.settings:
        print("\nHeader Evaluated Settings")

        for i in _settings.keys():
            print(f'{i}: {_settings[i]}')

def c_void():
    if _args.void:
        print('\n')
        exit()

def c_config():
    if _args.settings:
        print("\nConfig JSON Settings:")

        for i in _settings.keys():
            print(f'{i}: {_settings[i]}')