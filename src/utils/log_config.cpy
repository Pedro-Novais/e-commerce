import logging

class LogConfig:
    def __init__(self, typeLog: str, name: str, level: str, file: str):
        self.name = name
        self.type = typeLog
        self.level = level
        self.file = file

    def action(self):
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        
        logger = logging.getLogger('genesis')
        logger.setLevel(logging.DEBUG)

        self.log = logging.FileHandler('./logs/{}.log'.format(self.file))
        self.log.setLevel(self.level)
        self.log.setFormatter(formatter)