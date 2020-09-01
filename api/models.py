from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class Persona(models.Model):
    nombre= models.CharField(max_length=50, blank=True, null=False, default ='Sin Especificar')
    apellido= models.CharField(max_length=50, blank=True, null=False, default ='Sin Especificar')
    email = models.EmailField(max_length=100, blank=True, null=False, default ='Sin Especificar')
    telefono=models.CharField(max_length=13,blank=True, null=False, default ='0999999999')
    fecha_nacimiento= models.DateField(blank=True, null=True)
    lugar_origen= models.CharField(max_length=50,  blank=True, null=True)
    

    def __str__(self):
        text=self.nombre + " " + self.apellido
        return text

class MyUserManager(BaseUserManager):
    def create_user(self,email,username,password=None):
        if not email:
            raise ValueError('Usuario no provee correo')
        user = self.model(
            email=self.normalize_email(email),
            username=username
            )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,username,password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username
            )
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='email',max_length=60, unique=True)
    username = models.CharField(max_length=120,unique=True)
    fecha = models.DateTimeField(verbose_name='fecha_registro',auto_now_add=True)
    fecha_log = models.DateTimeField(verbose_name='ultimo_ingreso',auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)


    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']
    objects=MyUserManager()

    def __str__(self):
        return self.email

    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self,app_label):
        return True

class Habilidad(models.Model):
     nombre = models.CharField(max_length=50, blank=True, null=False, default='No disponible')

     def __str__(self):
         return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=False, default='No disponible')
    descripcion = models.CharField(max_length=250, blank=True, null=False, default='No disponible')
    
    def __str__(self):
        return self.nombre


class Facultad(models.Model):
    FACULTADES = (
        ('FIEC', 'Facultad de Ingenieria en Electricidad y Computacion'),
        ('FCNM', 'Facultad de Ciencias Naturales y Matematicas'),
        ('EDCOM', 'Escuela de Diseno y Comunicacion '),
        ('FICT', 'Facultad de Ingenieria en Ciencias de la Tierra'),
        ('FIMCP', 'Facultad de Ingenieria en Mecanica y Ciencias de la Produccion'),

    )
    nombre= models.CharField(max_length=150,  choices=FACULTADES,  blank=True, null=False, default ='Sin Especificar')

    def __str__(self):
        return self.nombre


class Consumidor(models.Model):
    id = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    descripcion= models.CharField(max_length=150,blank=True, null=False, default ='Sin Especificar')
    foto= models.CharField(max_length=150, blank=True, null=False, default ='Sin Especificar')
    facultad = models.ForeignKey(Facultad, on_delete=models.SET_NULL, blank=True, null=True)
    habilidad = models.ManyToManyField(Habilidad)

    def __str__(self):
        text=self.id.email 
        return text


class Administrador(models.Model):
     ROLES = (
        ('LECTOR', 'Lector'),
        ('ESCRITOR', 'Escritor'),
        ('PROPIETARIO', 'Propietario '),
        )
     id = models.OneToOneField(Persona, on_delete=models.CASCADE,primary_key=True)
     rol= models.CharField(max_length=30,blank=True, null=False, default ='Sin Especificar',choices=ROLES)
     def __str__(self):
         text=self.id.nombre + " " + self.id.apellido
         return text

class Anuncio(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=False, default ='No disponible')
    descripcion = models.CharField(max_length=300, blank=True, null=False, default='Dato no ingresado')
    banner = models.CharField(max_length=300, blank=True, null=False, default='No posee banner')
    estado = models.BooleanField(default=1);
    fecha_inicio = models.DateField(auto_now_add=True, null=True)
    fecha_termino = models.DateField(auto_now=False, null=True)
    vacantes = models.IntegerField(default=0)
    cant_interesados = models.IntegerField(default=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, blank=True, null=True)
    habilidad = models.ManyToManyField(Habilidad)
    interesados = models.ManyToManyField(Consumidor,blank=True)

    def __str__(self):
        return self.nombre

class Sugerencia(models.Model):
    detalle= models.CharField(max_length=250, blank=True, null=False, default ='Invalido')
    persona = models.ForeignKey(Persona, on_delete=models.SET_NULL, blank=False, null=True)

    def __str__(self):
        text=self.persona.nombre + " " + self.persona.apellido
        return text

class Noticia(models.Model):
    titulo= models.CharField(max_length=50,blank=True, null=False, default ='Sin Especificar')
    descripcion= models.CharField(max_length=300,blank=True, null=False, default ='Sin Especificar')
    administrador = models.ForeignKey(Administrador, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.titulo


