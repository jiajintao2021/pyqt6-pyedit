from importlib import import_module


class ModuleMemory:
    MODULE_MEMORY_DICT = dict()

    def add_external(self, model_str: str):
        """
        add external module and run this module, add == run
        load external module is run this module.
        @param model_str: external module "str" path.
        :return:
        """
        module = import_module(model_str)
        self.MODULE_MEMORY_DICT[module.__name__] = module
        return module

    def get_external_module(self, name, default=None):
        return self.MODULE_MEMORY_DICT.get(name, default=default)

    def pop_external_module(self, name):
        """
        pop module, but not del loaded module in memory.
        :param name: module's name
        :return: module
        """
        if name in self.MODULE_MEMORY_DICT:
            return self.MODULE_MEMORY_DICT.pop(name)

    def clear_external_module(self):
        self.MODULE_MEMORY_DICT.clear()

    def external_module(self):
        return self.MODULE_MEMORY_DICT
