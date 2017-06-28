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
             'ShezhangClas': ,
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
             'ShezhangClass': ,
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
### PostEditSubmit
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
### ActivityApplySubmit
INPUT
```
Method: POST
URL: /api/club/activity/apply/
DATA:{
    ActivityName:,
    Region,
    Clubid,
    ClubName,
    Content,
    Date1,
    Date2,
    State,
    Type,
    Participants,
    Token
}
```
OUTPUT
```
{
    'message': ('success' or 'error'),
    'Access-Control-Allow-Origin': '*',
}
```

### EstablishClub
INPUT
```
Method: POST
URL: /api/club/establish
DATA:{
    ClubName
    ShezhangName
    ShezhangQQ
    ShezhangGrade
    ShezhangClass
    Introduction,
    IfRecruit,
    QQGroup,
    Email
}
```
OUTPUT
```
{
    'message': ('success' or 'error'),
    'Access-Control-Allow-Origin': '*',
}
```
### EventAdd
INPUT

OUTPUT

### ProfileEditSubmit
INPUT
```
Method: POST
URL: /api/club/profile/edit
DATA:{
    ClubName
    ShezhangName
    ShezhangQQ
    ShezhangGrade
    ShezhangClass
    Introduction,
    IfRecruit,
    QQGroup,
    Email
}
```

OUTPUT

### ProfileGet
INPUT
```
Method: POST
URL: /api/club/establish
DATA:{
    ClubId
    Token
}
```
OUTPUT
```
{
    
}
```

### ActivityList
INPUT
```
Method: POST
URL: /api/club/establish
DATA:{
    ClubName
    ShezhangName
    ShezhangQQ
    ShezhangGrade
    ShezhangClass
    Introduction,
    IfRecruit,
    QQGroup,
    Email
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
             'ShezhangClas': ,
             'IfRecruit': ,
             'EnrollGroupQQ': ,
             'Email': ,
             'Label':
             'State': ,
             'Stars': ,
             'Introduction': ,
             'Achievements': ,
        },

    ]
}
```

## ADMIN_CD
