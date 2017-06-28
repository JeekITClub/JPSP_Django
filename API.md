# JPSP API
[TOC]
## PUBLIC
### LOGIN
INPUT
```
Method: POST
URL: /api/login
DATA:{
    UserId:
    Password:
    UserType: (student, club, club department)
    }
```
OUTPUT
```
{
    'message': ("User Authenticated" or "User Not Authenticated"),
    'Access-Control-Allow-Origin': '*',
    data:{
        'Token': ,
        'UserName'
    }
}
```

### LOGOUT
INPUT
```
Method: POST
URL: /api/logout
DATA:{
    UserId: ,
    UserType:
    Token:
    }
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

### ClubList
INPUT
```
Method: POST
URL: /api/public/clublist
DATA:{
    'Token':
}
```
OUTPUT
```
{
    'message': ('success' or 'error'),
    'Access-Control-Allow-Origin': '*',
    data:[
        {
             'ClubId': ,
             'ClubName':,
             'ShezhangName': ,
             'ShezhangQQ': ,
             'ShezhangGrade': ,
             'ShezhangClassroom': ,
             'IfRecruit': ,
             'EnrollGroupQQ': ,
             'Email': ,
             'Label':
             'State': ,
             'Stars': ,
             'Introduction': ,
             'Achievements': ,
        },
        {
             'ClubId': ,
             'ClubName':,
             'ShezhangName': ,
             'ShezhangQQ': ,
             'ShezhangGrade': ,
             'ShezhangClassroom': ,
             'IfRecruit': ,
             'EnrollGroupQQ': ,
             'Email': ,
             'Label':
             'State': ,
             'Stars': ,
             'Introduction': ,
             'Achievements': ,
        }
    ]
}
```


## INDEX
###

## ADMIN_CLUB
### ClubPostEditSubmit
INPUT
```
Method: POST
URL: /api/club/post/edit/submit
DATA:{
    'Token':
    'ClubId':
    'LinkmanGrade':
    'LinkmanClass':
    'LinkmanName'
    'LinkmanPhoneNumber'
    'LinkmanQq'
    'Region'
    'Date1'
    'Content'
    'Process'
    'Assessment'
    'Feeling'
    'Token'
}
```
OUTPUT
```
{
    'message': ('success' or 'error'),
    'Access-Control-Allow-Origin': '*',
}
```
###
## ADMIN_CD
