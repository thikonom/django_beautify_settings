A tiny script that removes all the redundant comments from django's DEFAULT settings.py
and renders its content in a more readable way.

How to use it:
--------------

1) Provide the full path of settings.py file from the command line::

    python clean_settings.py /Users/username/django-project/settings.py

_or_

2) Place the script on the root of your django project: 
    
    python clean_settings.py


You can test it with the sample settings.py file that's in the test folder: 

    python clean_settings.py ./test/settings.py
