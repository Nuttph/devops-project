*** Settings ***
Library    RequestsLibrary

*** Keywords ***
Connect To API
    [Arguments]    ${url}
    Create Session    mysess    ${url}

Create User And Return ID
    [Arguments]    ${username}    ${email}
    &{data}=    Create Dictionary    username=${username}    email=${email}    password=1234
    ${resp}=    POST On Session    mysess    /users/    json=${data}
    RETURN    ${resp.json()['_id']}