## Basic Usage

```python
from gorgias.client import Client

gorgias = Client(
    "gorgias_subdomain",
    "username",
    "api_key",
)
```

## Examples

### Customers
```python
# get all customers
gorgias.customers.all()

# find customer by ID
customer = gorgias.customers.find(id=39133997)

# create a customer
channel = CustomerChannel(type=ChannelTypes.phone, address="4155281962")
gorgias.customers.create(channels=[channel], name="Zach Holmquist")

# update a customer
customer = gorgias.customers.find(id=39589529)
customer.note = "A fellow space monkey."
gorgias.customers.save(customer)

# delete a customer
customer = gorgias.customers.find(id=39133997)
deleted_customer = gorgias.customers.delete(customer)

# merge two customers
source = gorgias.customers.find(id=39589529)
target = gorgias.customers.find(id=39589722)
merged_customer = gorgias.customers.merge(source, target)
```

### Tickets
```python
# get all tickets
gorgias.tickets.all()

# find ticket by ID
tickets = gorgias.tickets.find(id=10314075)

# update a ticket
ticket = gorgias.tickets.find(id=11034547)
ticket.subject = "This is a test with API Client"
ticket = gorgias.tickets.save(ticket)

# delete a ticket
ticket = gorgias.tickets.find(id=10314075)
gorgias.tickets.delete(ticket)

```



## TODO

### Complete API
- [ ] Account
- [x] Customer
- [ ] Integration
- [ ] Message
- [ ] Rule
- [x] Ticket
- [ ] Ticket Tags
- [ ] Tag
- [ ] User

### Other
- [ ] Tests
- [ ] Cleanup