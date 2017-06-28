# JPSP API
[TOC]
## PUBLIC
### LOGIN
INPUT
```
Method: POST
URL: /api/login
DATA:
    UserId:
    Password:
    UserType: (student, club, club department)
```
OUTPUT
```
{
    'message': ("User Authenticated" or "User Not Authenticated"),
    'Access-Control-Allow-Origin': '*',
    'Token':  ,
    'UserName':      
}
```

### LOGOUT
INPUT
```
Method: POST
URL: /api/logout
DATA:
    UserId: ,
    UserType:
    Token:
```
OUTPUT
```
{
    'message': ('success' or 'error'),
    'Access-Control-Allow-Origin': '*'
}
```
### ChangePassword
INPUT
```
```
OUTPUT
```
```

## INDEX
### 

## ADMIN_CLUB
###
###
## ADMIN_CD
