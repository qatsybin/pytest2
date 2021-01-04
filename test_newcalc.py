#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pytest


class TestCalc:
    # 加法
    @pytest.mark.run(order=1)
    def test_add(self, get_calc, get_datas_add, dayin):
        result = None
        try:
            result = get_calc.add(get_datas_add[0], get_datas_add[1])
            # 小数相加时限制精确度
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            print(e)

        assert result == get_datas_add[2]

    # 除法
    @pytest.mark.run(order=4)
    def test_div(self, get_calc, get_datas_div):
        result = None
        try:
            result = get_calc.div(get_datas_div[0], get_datas_div[1])
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            print(e)

        assert result == get_datas_div[2]

    # 减法
    @pytest.mark.run(order=2)
    def test_sub(self, get_calc, get_datas_sub):
        result = None
        try:
            result = get_calc.sub(get_datas_sub[0], get_datas_sub[1])
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            print(e)

        assert result == get_datas_sub[2]

    # 乘法
    @pytest.mark.run(order=3)
    def test_mul(self, get_calc, get_datas_mul):
        result = None
        try:
            result = get_calc.mul(get_datas_mul[0], get_datas_mul[1])
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            print(e)

        assert result == get_datas_mul[2]
