"""
Very advanced Employee management system.
"""
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional


class Contract(ABC):
    """Represents an employee contract."""

    @abstractmethod
    def compute_pay(self) -> float:
        """Compute how much to pay an employee under this contract."""


class Commission(ABC):
    """Represents an employee commission."""

    @abstractmethod
    def compute_pay(self) -> float:
        """Compute how much to pay an employee under this commission."""


@dataclass
class Employee:
    """Represents a generic employee in the company."""

    name: str
    id: int
    contract: Contract
    commission: Optional[Commission] = None

    def compute_pay(self) -> float:
        """Compute how much the employee should be paid."""
        payment = self.contract.compute_pay()

        if self.commission:
            payment += self.commission.compute_pay()

        return payment


@dataclass
class HourlyContract(Contract):
    """Represents an employee contract paid with hours."""

    pay_rate: float = 0
    hours_worked: int = 0
    employer_cost: float = 1000

    def compute_pay(self) -> float:
        return self.pay_rate * self.hours_worked + self.employer_cost


@dataclass
class ContractCommission(Commission):
    """Represents a commission payment process based on the number of contracts landed."""

    commission: float = 100
    contracts_landed: float = 0

    def compute_pay(self) -> float:
        return self.commission * self.contracts_landed


@dataclass
class SalariedContract(Contract):
    """Employee that's paid based on a fixed monthly salary."""

    monthly_salary: float = 0
    percentage: float = 1

    def compute_pay(self) -> float:
        return self.monthly_salary * self.percentage


@dataclass
class Freelancer(Employee):
    """Freelancer that's paid based on number of worked hours."""

    commission: float = 100
    contracts_landed: float = 0
    pay_rate: float = 0
    hours_worked: int = 0

    def compute_pay(self) -> float:
        return (
            self.pay_rate * self.hours_worked + self.commission * self.contracts_landed
        )


def main() -> None:
    """Main function."""

    henry_contract = HourlyContract(pay_rate=50, hours_worked=100)
    henry = Employee(name="Henry", id=12346, contract=henry_contract)
    print(
        f"{henry.name} worked for {henry_contract.hours_worked} hours and earned ${henry.compute_pay()}."
    )

    sarah_contract = SalariedContract(monthly_salary=5000)
    sarah_commission = ContractCommission(contracts_landed=10)
    sarah = Employee(
        name="Sarah", id=47832, contract=sarah_contract, commission=sarah_commission
    )
    print(
        f"{sarah.name} landed {sarah_commission.contracts_landed} contracts and earned ${sarah.compute_pay()}."
    )


if __name__ == "__main__":
    main()
