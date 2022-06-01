import unittest
import re
from main import regex_generator_gte, regex_generator_lt
from tqdm import tqdm


class MyTestCase(unittest.TestCase):
    def test_regex_generator_gte(self):
        search = 1500000
        for i in tqdm(range(search)):
            input_str = "https://century21mexico.com/busqueda/tipo_casa/operacion_venta/precio-desde_" + str(
                i) + "/precio-hasta_1500000/moneda_usd"
            reg = regex_generator_gte(search)

            x = re.search(reg, input_str)
            assert x is None
        for i in tqdm(range(search, search * 10, 1)):
            input_str = "https://century21mexico.com/busqueda/tipo_casa/operacion_venta/precio-desde_" + str(
                i) + "/precio-hasta_1500000/moneda_usd"
            reg = regex_generator_gte(search)

            x = re.search(reg, input_str)
            assert x is not None

    def test_regex_generator_lt(self):
        search = 1500000
        for i in tqdm(range(search)):
            input_str = "https://century21mexico.com/busqueda/tipo_casa/operacion_venta/precio-desde_" + str(
                i) + "/precio-hasta_1500000/moneda_usd"
            reg = regex_generator_lt(search)

            x = re.search(reg, input_str)
            assert x is not None
        for i in tqdm(range(search, search * 10, 1)):
            input_str = "https://century21mexico.com/busqueda/tipo_casa/operacion_venta/precio-desde_" + str(
                i) + "/precio-hasta_1500000/moneda_usd"
            reg = regex_generator_lt(search)

            x = re.search(reg, input_str)
            assert x is None


if __name__ == '__main__':
    unittest.main()
