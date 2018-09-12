Feature: Demo e2e test for Flask App w. DB

  Scenario: when a new customer is added to the data store
    Given we have a new customer
     When we send the new customer to the API
     Then the API should return an OK status code
      And the new customer should appear in the database

  Scenario: when an existing customer is added to the data store
    Given we have an existing customer
     When we send the existing customer to the API
     Then the API should return a BAD status code
      And the existing customer should only appear once in the datastore


