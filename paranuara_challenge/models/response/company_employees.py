from dataclasses import dataclass
from typing import List


@dataclass
class Employee:
    name: str
    email: str
    address: str
    phone: str
    age: int
    gender: str
    has_died: bool
    about: str
    registered: str
    tags: List[str]


@dataclass
class CompanyEmployees:
    company_name: str
    employee_count: int
    employees: List[Employee]

