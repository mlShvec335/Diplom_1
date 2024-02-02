from praktikum.bun import Bun


class TestBun:
    def test_get_name_correct_name(self):
        bun = Bun('Флюоресцентная булка R2-D3', 988)
        assert bun.get_name() == 'Флюоресцентная булка R2-D3'

    def test_get_price_correct_price(self):
        bun = Bun('Флюоресцентная булка R2-D3', 988)
        assert bun.get_price() == 988
