#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pytest
import yaml

from pythoncode.calculator import Calculator
import os

yaml_file_path = os.path.dirname(__file__) + "/data.yml"
# 读取文件并获取数据
with open(yaml_file_path) as f:
    datas = yaml.safe_load(f)
    print(datas)
    # 获取文件中key为datas的数据
    add_datas = datas["datas_add"]
    div_datas = datas["datas_div"]
    sub_datas = datas["datas_sub"]
    mul_datas = datas["datas_mul"]
    # 获取文件中key为myids的数据
    add_ids = datas["myids_add"]
    div_ids = datas["myids_div"]
    sub_ids = datas["myids_sub"]
    mul_ids = datas["myids_mul"]


@pytest.fixture(scope="function", autouse=True)
def dayin():
    print("开始计算")
    yield
    print("结束计算")


# 加法
@pytest.fixture(params=add_datas, ids=add_ids)
def get_datas_add(request):
    # print("开始计算")
    data = request.param
    print(f"request的返回数据是：{data}")
    yield data
    # print("结束计算")


# 除法
@pytest.fixture(params=div_datas, ids=div_ids)
def get_datas_div(request):
    # print("开始计算")
    data = request.param
    print(f"request的返回数据是：{data}")
    yield data
    # print("结束计算")


# 减法
@pytest.fixture(params=sub_datas, ids=sub_ids)
def get_datas_sub(request):
    # print("开始计算")
    data = request.param
    print(f"request的返回数据是：{data}")
    yield data
    # print("结束计算")


# 乘法
@pytest.fixture(params=mul_datas, ids=mul_ids)
def get_datas_mul(request):
    # print("开始计算")
    data = request.param
    print(f"request的返回数据是：{data}")
    yield data
    # print("结束计算")


@pytest.fixture(scope="session")  # 用于整个模块文件调用一次
def connectDB():
    print("连接数据库")
    yield
    print("断开数据库")


@pytest.fixture(scope="module")
def get_calc():
    print("获取计算器实例")
    calc = Calculator()
    return calc
