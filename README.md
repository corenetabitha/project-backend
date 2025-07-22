# project-backend
from accounts.models import CustomUser  
User = CustomUser  
User.objects.filter(is_superuser=True)
