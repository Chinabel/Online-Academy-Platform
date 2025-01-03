import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise
from dotenv import load_dotenv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'onlineacademy.settings')

project_folder = os.path.expanduser('~/onlineacademy')
load_dotenv(os.path.join(project_folder, '.env'))

application = get_wsgi_application()

application = WhiteNoise(application, root=os.path.join(project_folder, 'static'))

application.add_files(os.path.join(project_folder, 'more_static'), prefix="more-files/")
