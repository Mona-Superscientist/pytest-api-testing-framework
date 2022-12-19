## Pytest API testing framework
--------------------------------
This is an example for API testing with python using pytest 

**Used API example**

https://restful-booker.herokuapp.com/apidoc/index.html#api-Booking-GetBookings

## Framework structure:
There structure consists of some main folders:

- **Constants:** where all constants are added like routes, strings ..etc.
- **Helpers:** where basic requests and assertions helpers added as well as helper functions to all endpoints.
- **Samples:** where sample json files that represents required schemas are added to be used for generating test data in the testcases.
- **Specs:** where test cases added for each route.
- **Utils:** where generic utils needed for the framework are added like load_env, random generators .. etc.

