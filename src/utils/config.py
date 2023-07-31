import os

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
    

class Config(metaclass=Singleton):
    
    def __init__(self) -> None:
        self.cfg = self.load_env()
        
    def load_env(self):
        f = open(os.path.join(os.getcwd(),'.env'), 'r')
        cfg = {}
        for l in f:
            cfg[l.split('=')[0]] = l.split('=')[1]
        return cfg
        


if __name__ == "__main__":
    print(os.getcwd())
    print(os.path.isdir('src'))
    conf = Config()
    print(conf.cfg['API'])