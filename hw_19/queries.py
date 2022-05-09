

from typing import Dict


QUERIES: Dict[str, Dict[str, str]] = {
    'DDL': {},
    'DML': {}
}

QUERIES['DDL']['countries'] = """
CREATE TABLE IF NOT EXISTS countries(
country_id INTEGER PRIMARY KEY AUTOINCREMENT, 
name TEXT
);
"""

QUERIES['DDL']['locations'] = """
CREATE TABLE IF NOT EXISTS locations(
location_id INTEGER PRIMARY KEY AUTOINCREMENT,
street_address TEXT,
postal_code TEXT,
city TEXT,
country_id INTEGER,
FOREIGN KEY(country_id) REFERENCES countries(country_id)
);
"""

QUERIES['DDL']['jobs'] = """
CREATE TABLE IF NOT EXISTS jobs(
job_id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT,
min_salary INTEGER,
max_salary INTEGER 
);
"""

QUERIES['DDL']['departments'] = """
CREATE TABLE IF NOT EXISTS departments(
department_id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT UNIQUE,
manager_id INTEGER, 
location_id INTEGER,
FOREIGN KEY(location_id) REFERENCES locations(location_id)
);
"""

QUERIES['DDL']['employees'] = """
CREATE TABLE IF NOT EXISTS employees(
employer_id INTEGER PRIMARY KEY AUTOINCREMENT, 
first_name TEXT,
last_name TEXT,
email TEXT UNIQUE ,
phone_number TEXT UNIQUE,
hire_rate INTEGER,
job_id INTEGER,
manager_id INTEGER,
department_id INTEGER,
FOREIGN KEY(job_id) REFERENCES jobs(job_id),
FOREIGN KEY(manager_id) REFERENCES departments(manager_id),
FOREIGN KEY(department_id) REFERENCES departments(department_id)
);
"""
