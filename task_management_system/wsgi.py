

import os
project_home = os.path.expanduser('~/task_management_system')
os.environ['DJANGO_SETTINGS_MODULE']='task_management_system.settings'
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_management_system.settings')

application = get_wsgi_application()
