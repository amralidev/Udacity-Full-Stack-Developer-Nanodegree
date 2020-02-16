# This file should be included in .gitignore to not store sensitive data in version control
import os
SECRET_KEY = os.urandom(32)

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_TRACK_MODIFICATIONS = False

# TODO: Change values to your database setup information
database_setup = {
    "database_name_production" : "agency",
    "database_name_test" : "agency_test",
    "user_name" : "postgres", # default postgres user name
    "password" : "Silbermond1^", # if applicable. If no password, just type in None
    "port" : "localhost:5432" # default postgres port
}

# TODO: Change values with data from your Auth0 Dashboard
auth0_config = {
    "AUTH0_DOMAIN" : "fsnd-matthew.eu.auth0.com",
    "ALGORITHMS" : ["RS256"],
    "API_AUDIENCE" : "Music"
}

pagination = {
    "example" : 10 # Limits returned rows of API
}

bearer_tokens = {
    "casting_assistant" : "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik16azVRVUk0TXpSR04wSXhOVU13TkRrME16QXdNMFpHTmtFMU1VWXdPRUpCTmpnMFJrVTBSZyJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtbWF0dGhldy5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWU0N2VmNTg3ZWY5YjEwZjA0ZmQ5M2MzIiwiYXVkIjoiTXVzaWMiLCJpYXQiOjE1ODE4NDUzNjksImV4cCI6MTU4MTg1MjU2OSwiYXpwIjoiVGh2aG9mdmtkRTQwYlEzTkMzSzdKdFdSSzdSMzFOZDciLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbInJlYWQ6YWN0b3JzIiwicmVhZDptb3ZpZXMiXX0.wxurZHZR-Y8o-8q8vfEgROiJjksN4LXfE0yWJZM-MpkJBQspwUqS6MUus_-qWC5Qn8BnHgfQNxx7WVpvax81Isloty1VwfwtgqKeua66oRc9999FYPftmT-CZmIkVB3bEqNB_fhFF8y3t4Vy2QoFmAvGV74TJVnCbsrQdxWmJENyL-ubABPPEJyKbUdKumB-dgIu7PIqVHp4Weclr6xYpB4buuhO4X4G37dS3Nzy1TSRmuRD4IotlE1FQBj7t3a9lfu5wNbReWsCHBd-Ptubw_ivdb4u4wC6jkgCoCT8tBQs9nS6XHlj-35tEwisnEMah4-RcswXAKi4CJ19MoE4tA",
    "executive_producer" : "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik16azVRVUk0TXpSR04wSXhOVU13TkRrME16QXdNMFpHTmtFMU1VWXdPRUpCTmpnMFJrVTBSZyJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtbWF0dGhldy5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWU0N2VmYzc2N2YxYmEwZWJiNDIwMTYzIiwiYXVkIjoiTXVzaWMiLCJpYXQiOjE1ODE4NDUzMTUsImV4cCI6MTU4MTg1MjUxNSwiYXpwIjoiVGh2aG9mdmtkRTQwYlEzTkMzSzdKdFdSSzdSMzFOZDciLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImNyZWF0ZTphY3RvcnMiLCJjcmVhdGU6bW92aWVzIiwiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJlZGl0OmFjdG9ycyIsImVkaXQ6bW92aWVzIiwicmVhZDphY3RvcnMiLCJyZWFkOm1vdmllcyJdfQ.xNig8PxzNbOC0XXdQeXKE92eMG4qcOy-3eG9vuvwZtgw4adcVzi9tIObI5HwhFDdbgczd7EQZBRHAYLUZk5J-vGk6Ba0-uzYBN1VF3MLLQpmh3WW50Sbdr9Sjhs1OIDN7FMMy7tCiwGqIaxFwIpUX-5BAHFrtEEnsFlCPi5j784GCGr3KFa9HNzX9o4dcsGWURldr_5PDxWFcR8IXLJHUzmb6az_zP8UEQP8hUVzY3B3HwaFGWJG5nfEaNr6sLGosnfCW2wcZ0a311KgAZfA5WXsSl0WVSRNpHvjruv1dF7tHEdZJt1dMEJGnWP6ei8lyDDHoIkvSa64TZPa_5Ikgg",
    "casting_director" : "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik16azVRVUk0TXpSR04wSXhOVU13TkRrME16QXdNMFpHTmtFMU1VWXdPRUpCTmpnMFJrVTBSZyJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtbWF0dGhldy5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWU0N2VmOTA3ZWY5YjEwZjA0ZmQ5M2ZiIiwiYXVkIjoiTXVzaWMiLCJpYXQiOjE1ODE4NDQ4NDUsImV4cCI6MTU4MTg1MjA0NSwiYXpwIjoiVGh2aG9mdmtkRTQwYlEzTkMzSzdKdFdSSzdSMzFOZDciLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImNyZWF0ZTphY3RvcnMiLCJkZWxldGU6YWN0b3JzIiwiZWRpdDphY3RvcnMiLCJlZGl0Om1vdmllcyIsInJlYWQ6YWN0b3JzIiwicmVhZDptb3ZpZXMiXX0.O9OO51LPinbfF8hc3HKKMmC8X9vrM4evMvS7iVXMSu5FqcHoe_J1t3aafNAIyYDKIJAExN_qINbKFcPw3DfDuW8-Bh5w8ffD-ODhYICAKaQngf1mDHzBy3bpCZ9IFetZF1lMV1OBRlR27SvvoEN-uH-8Cnea3gcWoah2aoxIqew18GKBBUlTKCm4qKJf3i7c9-LuEZrPHTBIx-mvllpIcvFPNyhSN3Xzj2tTRmcKuBgsvPdmqBnGYlaGsxpjXlFl9fuu31LICUKoSoOpUo-hY8DbBk0nwAKmS5TOTynfAnE6uUy1xDhDvGbD6s5qMUsYOTyKJvOmxIt9w5HDJDdZWA"
}