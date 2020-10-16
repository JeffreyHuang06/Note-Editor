# NOT USED

import types

class Switcher:
    def __init__(self, *args):
        self.cases = args

        for case in args:  # partially initialize the funcs
            exec(f"def {case}(self):\n\tpass")
            exec(f"{type(self).__name__}.{case} = types.MethodType({case}, self)")

    def switch(self, tag: str):
        exec(f"self.{tag}()")


class interBodyTagSwitcher(Switcher):

    def __init__(self, *args):
        super(interBodyTagSwitcher, self).__init__(*args)

    def h(self):
        pass