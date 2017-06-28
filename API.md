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
    UserType: (student or club or club department)
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
    UserId:
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
Method: 'POST'
URL: api/changepassword
DATA:{
    UserId:
    UserType:
    Token:
    OriginalPassword:
    NewPassword:
}
```
OUTPUT
```
{
    'message': ('success' or 'error'),
    'Access-Control-Allow-Origin': '*'
}
```




## INDEX
### LostAndFoundList
INPUT
```
Method: 'POST'
URL: api/index/laf/list
DATA:{
    Token:
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
        }
    ]
}
```

### LostAndFoundForm
INPUT
```
Method: 'POST'
URL: api/index/laf/submit
DATA:{
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

### ClubList
INPUT
```
Method: 'POST'
URL: api/index/club/list
DATA:{
    Token:
}
```

OUTPUT
```

```

### ActivityList
INPUT
```
Method: 'POST'
URL: api/index/activity/list
DATA:{
    Token:
}
```
OUTPUT
```

```
### ClubList
INPUT
```
Method: POST
URL: /api/index/clublist
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

### ClubIndex
INPUT
```
Method: GET
URL: /api/index/clubindex/clubid
PARAMETER:{
    clubid
}
```
OUTPUT
```
```

## ADMIN_CLUB

### PostForm
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
### ActivityApply
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
```
Method: POST,
URL: /api/club/event/add
DATA:{
    ClubId:
    EventName:
    Date:
    Region:
    Content:
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

### ProfileForm
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
    Achievements
}
```

OUTPUT
```
{
    'message': ('success' or 'error'),
    'Access-Control-Allow-Origin': '*',
}
```

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
    'message': ('success' or 'error'),
    'Access-Control-Allow-Origin': '*',
    'data':{
        'ClubName'
        'ShezhangName'
        'ShezhangQQ'
        'ShezhangGrade'
        'ShezhangClass'
        'Introduction',
        'IfRecruit',
        'QQGroup',
        'Email',
        'Achievements'
    }
}
```

### ActivityList
INPUT
```
Method: POST
URL: /api/club/activity/list
DATA:{
    ClubName
    ClubId
    Token
    Type
}
```

OUTPUT
```
{
    'message': ('success' or 'error'),
    'Access-Control-Allow-Origin': '*',
    data:[
        {
            'ActivityName':
            'Region':
            'ClubId':
            'ClubName':
            'Content':
            'Date1':
            'Date2':
            'State':
            'Type':
            'Participants'
        },
        {
            'ActivityName':
            'Region':
            'ClubId':
            'ClubName':
            'Content':
            'Date1':
            'Date2':
            'State':
            'Type':
            'Participants'
        }
    ]
}
```

### RecruitClassroomForm
INPUT
```
Method: 'POST'
URL: api/index/activity/list
DATA:{
    Token:
}
```
OUTPUT
```
{
    'message': ('success' or 'error'),
    'Access-Control-Allow-Origin': '*',
}
```

## ADMIN_CD

### ActivityList
INPUT
```
Method: POST
URL: /api/cd/activity/list
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

}
```

### ClubList
INPUT
```
Method: 'POST'
URL: api/index/activity/list
DATA:{
    Token:
}
```
OUTPUT
```
```

### RecruitClassroomList
INPUT
```
Method: POST
URL: /api/cd/recruit/classroomlist
DATA:{
    Token
}
```
OUTPUT
```
'message': ('success' or 'error'),
'Access-Control-Allow-Origin': '*',
data:{

}
```

### PostList
INPUT
```
Method: 'POST'
URL: api/index/activity/list
DATA:{
    Token:
}
```
OUTPUT
```
```
