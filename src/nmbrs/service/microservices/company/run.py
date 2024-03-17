"""Microservice responsible for run related actions on the company level."""

from zeep import Client

from src.nmbrs.service.microservices.micro_service import MicroService


class CompanyRunService(MicroService):
    """
    Microservice responsible for run related actions on the company level.

    Not implemented calls:
        - [RunRequest_GetList](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=RunRequest_GetList)
        - [RunRequest_Insert](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=RunRequest_Insert)
        - [Run_GetEmployeesByRunCompany](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=Run_GetEmployeesByRunCompany)
        - [Run_GetList](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=Run_GetList)
    """

    def __init__(self, client: Client) -> None:
        super().__init__(client)

    def set_auth_header(self, auth_header: dict) -> None:
        self.auth_header = auth_header
