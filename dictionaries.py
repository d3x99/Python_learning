customer = {
    "name": "John Smith",
    2 : 30,
    "is_verified": True

}
customer["birthdate"] = '17 january'
print(customer.get( 2, "Jan 1 1990"))
print(customer['name'])
