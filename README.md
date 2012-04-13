A tiny script that removes all the ( unnecessary ) comments from django's DEFAULT settings.py
and renders its content in a pretty/readable format.

How to use it:
++++++++++++++

1) Provide the full path of settings.py file from the command line: 
    python clean_settings.py /Users/username/django-project/settings.py

or

2) Place the script on the root of your django project: 
    python clean_settings.py


You can test it with the sample settings.py file that's in the test folder: 
  python clean_settings.py ./test/settings.py