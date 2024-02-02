from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.ingredient_types import *


class TestBurger:
    def test_set_buns_successful_set(self):
        mock_bun = Mock()
        mock_bun.get_name.return_value = 'Флюоресцентная булка R2-D3'
        mock_bun.get_price.return_value = 988
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient_successful_add(self):
        mock_ingredient_1 = Mock()
        mock_ingredient_1.type = 'SAUCE'
        mock_ingredient_1.name = 'Соус Spicy-X'
        mock_ingredient_1.price = 90
        mock_ingredient_2 = Mock()
        mock_ingredient_2.type = 'FILLING'
        mock_ingredient_2.name = 'Мясо бессмертных моллюсков Protostomia'
        mock_ingredient_2.price = 1337
        burger = Burger()
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        assert burger.ingredients == [mock_ingredient_1, mock_ingredient_2]

    def test_remove_ingredient_successful_remove(self):
        mock_ingredient_1 = Mock()
        mock_ingredient_2 = Mock()
        burger = Burger()
        burger.ingredients = [mock_ingredient_1, mock_ingredient_2]
        burger.remove_ingredient(0)
        assert mock_ingredient_1 not in burger.ingredients

    def test_move_ingredient_successful_move(self):
        mock_ingredient_1 = Mock()
        mock_ingredient_2 = Mock()
        burger = Burger()
        burger.ingredients = [mock_ingredient_1, mock_ingredient_2]
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [mock_ingredient_2, mock_ingredient_1]

    def test_get_price_correct_calculate_price(self):
        mock_bun = Mock()
        mock_bun.get_price.return_value = 988
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = 90
        burger = Burger()
        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient]
        assert burger.get_price() == 2066

    def test_get_receipt_correct_receipt(self):
        mock_bun = Mock()
        mock_bun.get_name.return_value = 'Флюоресцентная булка R2-D3'
        mock_ingredient_1 = Mock()
        mock_ingredient_1.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_ingredient_1.get_name.return_value = 'Соус Spicy-X'
        mock_ingredient_2 = Mock()
        mock_ingredient_2.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_ingredient_2.get_name.return_value = 'Мясо бессмертных моллюсков Protostomia'
        mock_burger = Mock()
        mock_burger.get_price.return_value = 3403
        burger = Burger()
        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient_1, mock_ingredient_2]
        burger.get_price = mock_burger.get_price

        expected_result = '(==== Флюоресцентная булка R2-D3 ====)\n' \
                          '= sauce Соус Spicy-X =\n' \
                          '= filling Мясо бессмертных моллюсков Protostomia =\n' \
                          '(==== Флюоресцентная булка R2-D3 ====)\n' \
                          '\nPrice: 3403'

        assert burger.get_receipt() == expected_result
