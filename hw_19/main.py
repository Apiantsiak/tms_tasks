

from pprint import pprint
from typing import Any

from database_connector import DbConnector
from queries import QUERIES


CONNECTION = DbConnector('hw_19DB.sqlite')


def create_tables(query: str):
    with CONNECTION as cursor:
        cursor.execute(query)


def insert_into_tables(table: str, rows: str, values: tuple or str):
    query = f"""
    INSERT INTO {table} ({rows})
    VALUES {values}
    ;
    """
    print(query)
    with CONNECTION as cursor:
        cursor.execute(query)


def update_tables(table: str, row: str, value: Any, new_value: Any):
    query = f"""
    UPDATE {table}
    SET {row} = {new_value}
    WHERE {row} = {value};
    """
    with CONNECTION as cursor:
        cursor.execute(query)


def delete_from_tables(table: str, row: str, value: str):
    query = f"""
    DELETE FROM {table}
    WHERE {row} = {value};
    """
    with CONNECTION as cursor:
        cursor.execute(query)


def count_employees() -> int:
    query = f"""
    SELECT COUNT()
    FROM employees; 
    """
    with CONNECTION as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
    return result


def count_managers() -> int:
    query = """
    SELECT COUNT(manager_id)
    FROM departments;
    """
    with CONNECTION as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
    return result


def average_salary():
    query = """ 
    SELECT AVG(hire_rate) 
    FROM employees;
    """
    with CONNECTION as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
    return result


def alphabet_order_unique_city_list():
    query = """
    SELECT DISTINCT city 
    FROM locations
    ORDER BY city DESC; 
    """
    with CONNECTION as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
    return result


if __name__ == '__main__':

    assert count_managers() == [(3,)]
    assert average_salary() == [(1416.6666666666667,)]
    assert alphabet_order_unique_city_list() == [('New York',), ('Moscow',), ('Krakow',)]

    # update_tables('jobs', 'max_salary', 2500, 3500)
    # delete_from_tables(table='jobs', row='title', value='"DEV"')
    # insert_into_tables(
    #     table='jobs',
    #     rows='title, min_salary, max_salary',
    #     values=('DEV', 1500, 2500)
    # )
    # insert_into_tables(
    #     table='departments',
    #     rows='name, manager_id, location_id',
    #     values=('CDPr_EU', 1, 1)
    # )
    # insert_into_tables(
    #     table='departments',
    #     rows='name, manager_id, location_id',
    #     values=('CDPr_US', 2, 2)
    # )
    # insert_into_tables(
    #     table='departments',
    #     rows='name, manager_id, location_id',
    #     values=('CDPr_RU', 3, 3)
    # )
    # insert_into_tables(
    #     table='locations',
    #     rows='street_address, postal_code, city, country_id',
    #     values=('poland_street', '111', 'Krakow', 1)
    # )
    # insert_into_tables(
    #     table='locations',
    #     rows='street_address, postal_code, city, country_id',
    #     values=('american_street', '222', 'New York', 2)
    # )
    # insert_into_tables(
    #     table='locations',
    #     rows='street_address, postal_code, city, country_id',
    #     values=('ru_street', '333', 'Moscow', 3)
    # )
    # insert_into_tables(
    #     table='employees',
    #     rows='first_name, last_name, email, phone_number, hire_rate, job_id, manager_id, department_id',
    #     values=('Alexey', 'Smith', 'as.@gmail.com', '+48 2020326', 1000, 1, 1, 1,)
    # )
    # insert_into_tables(
    #     table='employees',
    #     rows='first_name, last_name, email, phone_number, hire_rate, job_id, manager_id, department_id',
    #     values=('Bred', 'Pit', 'bp.@gmail.com', '+568 2020326', 1250, 1, 2, 2)
    # )
    # insert_into_tables(
    #     table='employees',
    #     rows='first_name, last_name, email, phone_number, hire_rate, job_id, manager_id, department_id',
    #     values=('Harrison', 'Ford', 'hf.@gmail.com', '+444 2020326', 2000, 2, 3, 3)
    # )
    # insert_into_tables(
    #     table='countries',
    #     rows='name',
    #     values="('Russia')"
    # )
