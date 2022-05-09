
from sqlalchemy import func, desc
from pprint import pprint

from session import open_db_session
from models import (
    Categories, Customers, Employees, Orders, Products, Shippers, Suppliers
)


def company_employees_london_speedy_exp():
    with open_db_session() as session:
        query_res = (
            session.query(Customers.company_name, Employees.first_name + ' ' + Employees.last_name)
            .join(Orders, Customers.customer_id == Orders.customer_id)
            .join(Employees, Orders.employee_id == Employees.employee_id)
            .join(Shippers, Orders.ship_via == Shippers.shipper_id)
            .filter(Customers.city == "London")
            .filter(Employees.city == "London")
            .filter(Shippers.company_name == "Speedy Express")
        ).all()
        return query_res


def customers_without_orders():
    with open_db_session() as session:
        query_res = (
            session.query(Customers.company_name, Customers.customer_id)
            .outerjoin(Orders, Customers.customer_id == Orders.customer_id)
            .filter(Orders.customer_id == None)
        ).all()
        return query_res


def active_products_condiments_meat_poultry_less_100():
    with open_db_session() as session:
        query_res = (
            session.query(Products.product_name, Products.units_in_stock, Suppliers.contact_name, Suppliers.phone)
            .join(Suppliers, Products.supplier_id == Suppliers.supplier_id)
            .join(Categories, Products.category_id == Categories.category_id)
            .filter(Products.discontinued == 0)
            .filter(Products.units_in_stock < 100)
            .filter(Categories.category_name.in_(["Condiments", "Meat/Poultry"]))
        ).all()
        return query_res


def number_of_goods_in_categories():
    with open_db_session() as session:
        query_res = (
            session.query(Categories.category_name, func.count(Products.product_name).label("Number of goods"))
            .join(Categories, Products.category_id == Categories.category_id)
            .group_by(Categories.category_name)
            .order_by(desc("Number of goods"))
            .all()
        )
        return query_res


def test_check_raw_equal_orm(execute_queries):
    for _ in range(len(execute_queries)):
        assert execute_queries['company_employees_london_speedy_exp'] == company_employees_london_speedy_exp()
        assert execute_queries['customers_without_orders'] == customers_without_orders()
        assert execute_queries['active_products_condiments_meat_poultry_less_100'] == \
               active_products_condiments_meat_poultry_less_100()
        assert execute_queries['number_of_goods_in_categories'] == number_of_goods_in_categories()
