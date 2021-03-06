"""
Very advanced Employee management system.
"""
from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum, auto

FIXED_VACATION_DAYS_PAYOUT = 5  # The fixed nr of vacation days that can be paid out.


class Role(Enum):
    Manager = auto()
    VicePresident = auto()
    Inter = auto()


@dataclass
class Employee(ABC):
    """Basic representation of an employee at the company."""

    name: str
    role: Role
    vacation_days: int = 25

    def take_a_holiday(self, payout: bool) -> None:
        """Let the employee take a single holiday, or pay out 5 holidays."""
        if payout:
            # check that there are enough vacation days left for a payout
            if self.vacation_days < FIXED_VACATION_DAYS_PAYOUT:
                raise ValueError(
                    f"You don't have enough holidays left over for a payout.\
                        Remaining holidays: {self.vacation_days}."
                )
            try:
                self.vacation_days -= FIXED_VACATION_DAYS_PAYOUT
                print(f"Paying out a holiday. Holidays left: {self.vacation_days}")
            except Exception:
                # this should never happen
                pass
        else:
            if self.vacation_days < 1:
                raise ValueError(
                    "You don't have any holidays left. Now back to work, you!"
                )
            self.vacation_days -= 1
            print("Have fun on your holiday. Don't forget to check your emails!")

    @abstractmethod
    def pay(self) -> None:
        """Pays to the employee"""


@dataclass
class HourlyEmployee(Employee):
    """Employee that's paid based on number of worked hours."""

    hourly_rate_in_dollars: float = 50
    hours_worked: int = 10

    def pay(self) -> None:
        print(
            f"Paying employee {self.name} a hourly rate of \
                ${self.hourly_rate_in_dollars} for {self.hours_worked} hours."
        )


@dataclass
class SalariedEmployee(Employee):
    """Employee that's paid based on a fixed monthly salary."""

    monthly_salary_in_dollars: float = 5000

    def pay(self) -> None:
        print(
            f"Paying employee {self.name} a monthly salary of ${self.monthly_salary_in_dollars}."
        )


class Company:
    """Represents a company with employees."""

    def __init__(self) -> None:
        self.employees: list[Employee] = []

    def add_employee(self, employee: Employee) -> None:
        """Add an employee to the list of employees."""
        self.employees.append(employee)

    def find_employees(self, role: Role) -> list[Employee]:
        """Find all employees with a specific role."""
        return [
            employee
            for employee in self.employees
            if employee.role == role
        ]


company = Company()

company.add_employee(SalariedEmployee(name="Louis", role=Role.Manager))
company.add_employee(HourlyEmployee(name="Brenda", role=Role.VicePresident))
company.add_employee(HourlyEmployee(name="Tim", role=Role.Inter))

print(company.find_employees(Role.VicePresident))
print(company.find_employees(Role.Manager))
print(company.find_employees(Role.Inter))
company.employees[0].pay()
company.employees[0].take_a_holiday(False)
