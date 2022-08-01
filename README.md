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

## TODO

### Complete API
- [ ] Account
- [x] Customer
- [ ] Integration
- [ ] Message
- [ ] Rule
- [ ] Ticket
- [ ] Tag
- [ ] User

### Other
- [ ] Tests
- [ ] Cleanup