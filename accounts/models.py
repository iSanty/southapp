from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, PermissionsMixin, BaseUserManager
from ckeditor.fields import RichTextField


# class UserProfileManager(BaseUserManager):
#     """Manager para perfiles de usuario """
#     def create_user(self, email,name, password=None):
#         ''' crear nuevo user profile '''
#         if not email:
#             raise ValueError('Complete el campo E-Mail')
        
#         email = self.normalize_email(email)
#         user = self.model(email=email, name=name)
        
#         user.set_password(password)
#         user.save(using=self._db)
        
#         return user

#     def create_superuser(self, email, name, password):
#         user = self.create_user(email, name, password)
        
#         user.is_superuser = True
#         user.is_staff = True        
#         user.save(using=self._db)
        
#         return user



    
# class UserProfile(AbstractBaseUser, PermissionsMixin):
    
#     """modelo base de datos para usuarios en el sistema"""
#     email = models.EmailField(max_length=255, unique=True)
#     name = models.CharField(max_length=255)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
    
#     objects = UserProfileManager()
    
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['name']

#     def get_full_name(self):
#         return self.name
    
#     def get_short_name(self):
#         return self.name


#     def __str__(self):
#         return self.email
    
    
    
class MasDatosUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatares', null=True, blank =True)
    descripcion = RichTextField(null=True)
    sucursal = models.CharField(max_length=30)
    
    def __str__(self):
        return f'{self.user}'