# Creating USERS

# Creating superusers

# Changing passwords


```python
 from django.contrib.auth.models import User

 u = User.objects.get(username='john')

 u.set_password('new password')

 u.save()
```

# Authenticating users

authenticate(request=None, **credentials)[source]

```python
from django.contrib.auth import authenticate
user = authenticate(username='john', password='secret')
if user is not None:
    # A backend authenticated the credentials
else:
    # No backend authenticated the credentials
```
