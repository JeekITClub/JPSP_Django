# JPSP API
[TOC]
## PUBLIC

### Login
INPUT
```
Method: POST
URL: /api/login
DATA:{
    UserId:
    Password:
    UserType: ('student' or 'club' or 'cd')
}
```
OUTPUT
```
{
    'message': ("User Authenticated" or "User Not Authenticated"),
    'Access-Control-Allow-Origin': '*',
    data:{
        'Token': ,
        'UserName':
    }
}
```

### Logout
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
Method: 'GET'
URL: api/laf/list
```
OUTPUT
```
{
    'message': ('success' or 'error'),
    'Access-Control-Allow-Origin': '*',
    data:[
        {
            LostOrFound:
            ObjectName:
            LinkmanGrade:
            LinkmanClass:
            LinkmanName:
            LinkmanPhoneNumber:
            LinkmanQq:
            Region:
            Date1:
            Date2:
            Importance:
            Desc:
        },
        {
            LostOrFound:
            ObjectName:
            LinkmanGrade:
            LinkmanClass:
            LinkmanName:
            LinkmanPhoneNumber:
            LinkmanQq:
            Region:
            Date1:
            Date2:
            Importance:
            Desc:
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
    LostOrFound:
    ObjectName:
    LinkmanGrade:
    LinkmanClass:
    LinkmanName:
    LinkmanPhoneNumber:
    LinkmanQq:
    Region:
    Date1:
    Date2:
    Importance:
    Desc:
}
```
OUTPUT
```
{
    'message': ('success' or 'error'),
    'Access-Control-Allow-Origin': '*'
}
```

### ActivityList
INPUT
```
Method: 'POST'
URL: api/activity/list
DATA:{
    Token:
    Type: 'index'
}
```
OUTPUT
```
{
    'message': ('success' or 'error'),
    'Access-Control-Allow-Origin': '*',
    data:[
        {
            'Name':
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
### ClubList
INPUT
```
Method: GET
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
    clubid:
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
    'LinkmanName':
    'LinkmanPhoneNumber':
    'LinkmanQq':
    'Region':
    'Date1':
    'Content':
    'Process':
    'Assessment':
    'Feeling':
    'Token':
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
    ActivityName:
    Region:
    Clubid:
    ClubName:
    Content:
    Date1:
    Date2:
    State:
    Type:
    Participants:
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
URL: /api/clubevent/add
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
URL: /api/clubprofile/form
DATA:{
    ClubName:
    ShezhangName:
    ShezhangQQ:
    ShezhangGrade:
    ShezhangClass:
    Introduction:
    IfRecruit:
    QQGroup:
    Email:
    Achievements:
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
URL: /api/clubprofile/get
DATA:{
    ClubId:
    Token:
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
URL: /api/activity/list
DATA:{
    ClubName:
    ClubId:
    Token:
    User: 'Club'
    Type: ('Past' or 'Happening' or 'Confirmed' or 'Denied')
}
```

OUTPUT
```
{
    'message': ('success' or 'error'),
    'Access-Control-Allow-Origin': '*',
    data:[
        {
            'Name':
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
URL: api/recruit/classroom/form
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
URL: /api/activity/list
DATA:{
    Token:
    User: 'CD'
    Type: ('Unconfirmed' or 'Happening' or 'Past' or 'Confirmed' or 'All')
}
```
OUTPUT
```
{
    'message': ('success' or 'error'),
    'Access-Control-Allow-Origin': '*',
    data:[
        {
            'Name':
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

### ClubList
INPUT
```
Method: 'POST'
URL: api/club/list
DATA:{
    Token:
    User: 'CD'
    Type: ('Established' or 'Unconfirmed')
}
```
OUTPUT
```
```

### RecruitClassroomList
INPUT
```
Method: POST
URL: /api/recruit/classroom/list
DATA:{
    Token:
    User: 'CD'
    Type: ('Confirmed' or 'Unconfirmed')
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
    User: 'CD'
    Type: ('Unstared' or 'Stared' or 'All' or 'Denied')
}
```
OUTPUT
```
```
