*** Settings ***
Library           RequestsLibrary

*** Variables ***
${API_URL}  http://127.0.0.1:8000

*** Test Cases ***
# Check Database Status
#     Create Session  mysess  ${API_URL}
#     ${resp}=  Get On Session  mysess  /test-db
#     Should Be Equal As Integers  ${resp.status_code}  200
#     &{expected_data}=  Create Dictionary  message=Database is working!  user_count=${0}
#     Should Be Equal  ${resp.json()}  ${expected_data}

Check Database InSide
    Create Session  mysess  ${API_URL}
    ${resp}=  Get On Session  mysess  /test-db-connection
    Should Be Equal As Integers  ${resp.status_code}  200
    Should Be Equal As Strings  ${resp.json()['status']}  connected!
    Should Be Equal As Strings  ${resp.json()['database']}  hr