
from sqlalchemy import (
    Column, Date, Float, ForeignKey, Integer, SmallInteger, String, Text,
)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Categories(Base):
    __tablename__ = "categories"

    category_id = Column(SmallInteger, primary_key=True)
    category_name = Column(String(15), nullable=False)
    description = Column(Text)


class Customers(Base):
    __tablename__ = "customers"

    customer_id = Column(String(10), primary_key=True)
    company_name = Column(String(40), nullable=False)
    contact_name = Column(String(30))
    contact_title = Column(String(30))
    address = Column(String(60))
    city = Column(String(15))
    region = Column(String(15))
    postal_code = Column(String(10))
    country = Column(String(15))
    phone = Column(String(24))
    fax = Column(String(24))


class Employees(Base):
    __tablename__ = "employees"

    employee_id = Column(SmallInteger, primary_key=True)
    last_name = Column(String(20), nullable=False)
    first_name = Column(String(10), nullable=False)
    title = Column(String(30))
    title_of_courtesy = Column(String(25))
    birth_date = Column(Date)
    hire_date = Column(Date)
    address = Column(String(60))
    city = Column(String(15))
    region = Column(String(15))
    postal_code = Column(String(10))
    country = Column(String(15))


class Orders(Base):
    __tablename__ = "orders"

    order_id = Column(SmallInteger, primary_key=True)
    customer_id = Column(ForeignKey("customers.customer_id"))
    employee_id = Column(ForeignKey("employees.employee_id"))
    order_date = Column(Date)
    required_date = Column(Date)
    shipped_date = Column(Date)
    ship_via = Column(ForeignKey("shippers.shipper_id"))
    freight = Column(Float)
    ship_name = Column(String(40))
    ship_address = Column(String(60))
    ship_city = Column(String(15))
    ship_region = Column(String(15))
    ship_postal_code = Column(String(10))
    ship_country = Column(String(15))

    customers = relationship("Customers")
    employees = relationship("Employees")
    shippers = relationship("Shippers")


class Products(Base):
    __tablename__ = "products"

    product_id = Column(SmallInteger, primary_key=True)
    product_name = Column(String(40), nullable=False)
    supplier_id = Column(ForeignKey("suppliers.supplier_id"))
    category_id = Column(ForeignKey("categories.category_id"))
    quantity_per_unit = Column(String(20))
    unit_price = Column(Float)
    units_in_stock = Column(SmallInteger)
    units_on_order = Column(SmallInteger)
    reorder_level = Column(SmallInteger)
    discontinued = Column(Integer)

    categories = relationship("Categories")
    suppliers = relationship("Suppliers")


class Shippers(Base):
    __tablename__ = "shippers"

    shipper_id = Column(SmallInteger, primary_key=True)
    company_name = Column(String(40), nullable=False)
    phone = Column(String(24))


class Suppliers(Base):
    __tablename__ = "suppliers"

    supplier_id = Column(SmallInteger, primary_key=True)
    company_name = Column(String(40), nullable=False)
    contact_name = Column(String(30))
    contact_title = Column(String(30))
    address = Column(String(60))
    city = Column(String(15))
    region = Column(String(15))
    postal_code = Column(String(10))
    country = Column(String(15))
    phone = Column(String(24))
    fax = Column(String(24))
    homepage = Column(Text)
