import string
import datetime
import logging

class PasswordGeneratorConfig:
    """Configurações compartilhadas para todos os geradores"""
    def __init__(self):
        self.brute_charset = string.ascii_letters + string.digits + string.punctuation
        self.min_length = 4
        self.max_length = 8
        self.base_words = ["admin", "senha", "password", "user", "qwerty"]
        self.leet_mappings = {'a': '@', 'e': '3', 'i': '1', 'o': '0', 's': '$', 't': '7'}
        self.common_years = [str(y) for y in range(1980, datetime.datetime.now().year + 1)]
        self.common_specials = ["!", "@", "#", "$", "%", "&", "*", "_", "-"]

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('generator.log'), logging.StreamHandler()]
)

config = PasswordGeneratorConfig()