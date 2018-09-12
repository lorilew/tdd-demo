import requests
from behave import given, when, then
from tinydb import TinyDB, Query

db = TinyDB("customer.json")


@given(u'we have a new customer')
def step_impl(context):
    new_customer = {
        "name": "Lewis",
        "id": 123
    }
    Customer = Query()
    res = db.search(Customer.id == new_customer["id"])
    assert len(res) == 0

    context.new_customer = new_customer


@when(u'we send the new customer to the API')
def step_impl(context):
    try:
        res = requests.post(url="http://127.0.0.1:5000", data=context.new_customer)
    except Exception as e:
        assert False

    context.new_customer_res = res


@then(u'the API should return an OK status code')
def step_impl(context):
    print(context.new_customer_res)
    assert context.new_customer_res.status_code == 200


@then(u'the new customer should appear in the database')
def step_impl(context):
    Customer = Query()
    res = db.search(Customer.id == context.new_customer["id"])

    assert len(res) == 1
    assert res["name"] == context.new_customer["name"]


@given(u'we have an existing customer')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given we have an existing customer')


@when(u'we send the existing customer to the API')
def step_impl(context):
    raise NotImplementedError(u'STEP: When we send the existing customer to the API')


@then(u'the API should return a BAD status code')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the API should return a BAD status code')


@then(u'the existing customer should only appear once in the datastore')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the existing customer should only appear once in the datastore')
