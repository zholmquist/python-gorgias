import requests


class Client(object):
    def __init__(self, gorgias_subdomain: str, username: str, api_key: str):
        self.username = username
        self.api_key = api_key
        self.base_url = f"https://{gorgias_subdomain}.gorgias.com/api/"

    @property
    def customers(self):
        from gorgias.service import customer

        return customer.Customer(self)

    @property
    def tickets(self):
        from gorgias.service import ticket

        return ticket.Ticket(self)

    def request(self, method, path, **params):
        method = method.upper()
        request_kwargs = {}

        if method == "GET":
            request_kwargs["params"] = params
        elif method == "POST":
            request_kwargs["data"] = params
        elif method == "DELETE" or method == "PUT":
            request_kwargs["json"] = params
        else:
            raise Exception

        print(request_kwargs)

        response = requests.request(
            method,
            f"{self.base_url + path}",
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json",
            },
            auth=(self.username, self.api_key),
            **request_kwargs,
        )
        return response

    def get(self, path, **params):
        return self.request("GET", path, **params)

    def post(self, path, **data):
        return self.request("POST", path, **data)

    def delete(self, path, **data):
        return self.request("DELETE", path, **data)

    def put(self, path, **data):
        return self.request("PUT", path, **data)
