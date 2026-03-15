*** Settings ***
Resource    ../resources/common.resource
Variables   ../resources/variables.py    # เพื่อเอา BASE_URL, DB_NAME
Library     ../resources/variables.py    # เพื่อเอา get_random_username มาเป็น Keyword


*** Test Cases ***
Testing New User Flow
    ${random_name}=    Get Random Username
    Connect To API     ${BASE_URL}
    ${id}=             Create User And Return ID    ${random_name}    test@email.com
    Log     Created user with ID: ${id}
    Log To Console     Hello World!!

Verify User Lifecycle (Create -> Get -> Update)
    [Documentation]    This test case verifies the complete lifecycle of a user: creation, retrieval, and update.
    Connect To API    ${BASE_URL}
    ${random_name}=   Get Random Username

    ${id}=    Create User And Return ID    ${random_name}    ${random_name}@test.com
    
    ${resp_before}=    GET On Session    mysess    /users/${id}
    Should Be Equal As Strings    ${resp_before.json()['username']}    ${random_name}

    &{update_body}=    Create Dictionary    full_name=Nuttaphon Updated
    ${resp_update}=    PUT On Session    mysess    /users/${id}    json=${update_body}
    Should Be Equal As Integers    ${resp_update.status_code}    200
    
    Should Be Equal As Strings    ${resp_update.json()['full_name']}    Nuttaphon Updated