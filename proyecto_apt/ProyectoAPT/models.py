from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
# Create your models here.
from datetime import datetime
from django.core.mail import send_mail

#TipoUsuario
class TipoUsuario(models.Model):
        id= models.BigAutoField(primary_key=True)
        nombre_tipo_usuario = models.CharField(max_length=100)
        descripcion = models.CharField(max_length=100)
        def __str__(self):
            return str(self.nombre_tipo_usuario)
        # DICT
        #2.Estudiante
        #1.Paciente
        
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El usuario debe tener un email')
        email = self.normalize_email(email)
        extra_fields.setdefault('username', email.split('@')[0])  # Generar un username a partir del email
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('username', email.split('@')[0])

        if extra_fields.get('is_staff') is not True:
            raise ValueError('El superusuario debe tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('El superusuario debe tener is_superuser=True.')

        return self.create_user(email, password, **extra_fields)
    
    #filtros universidades y tratamientos
class Universidad(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=100, unique=True)
    direccion = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.nombre


class tipoTratamiento(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombreTratamiento= models.CharField(max_length=50)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombreTratamiento

class Comuna(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombreComuna= models.CharField(max_length=50)

    def __str__(self):
        return self.nombreComuna




        
class customuser(AbstractUser):
    id = models.BigAutoField(primary_key=True)
    email = models.EmailField(unique=True, null=True)
    rut = models.CharField(max_length=13, unique=True, null=True)
    id_tipo_user = models.ForeignKey('TipoUsuario', on_delete=models.SET_NULL, null=True)
    descripcion = models.TextField(null=True)
    imageBlob = models.ImageField(default="imagenes_usuario/profiledefault.jpg", upload_to='imagenes_usuario/', blank=True, null=True)
    fecha_nac = models.DateField(null=True)
    num_tel = models.IntegerField(null=True, max_length=9)
    direccion = models.TextField(null=True, blank=True)
    universidad = models.ForeignKey(Universidad, on_delete=models.SET_NULL, null=True, blank=True)
    comuna = models.ForeignKey(Comuna, on_delete=models.SET_NULL, null=True, blank=True)
    tratamientos = models.ManyToManyField(tipoTratamiento, blank=True)
    Certificado = models.FileField(
        upload_to='documentos_estudiantes/',
        null=True,
        blank=True,
        validators=[
            FileExtensionValidator(
                allowed_extensions=['pdf'],
                message='Solo se permiten archivos PDF'
            )
        ],
        help_text='Sube un certificado en formato PDF'
    )

    # Nuevo campo para manejar el estado de aprobación
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('aprobado', 'Aprobado'),
        ('rechazado', 'Rechazado')
    ]
    estado_aprobacion = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='pendiente')

    USERNAME_FIELD = 'email'  # Usar email para el inicio de sesión
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def clean(self):
        super().clean()
        # Validación del certificado durante la creación del usuario
        if not self.pk:  # Si es un nuevo usuario
            if self.id_tipo_user and self.id_tipo_user.nombre_tipo_usuario == 'Estudiante':
                if not self.Certificado:
                    raise ValidationError({
                        'Certificado': 'El certificado es obligatorio para estudiantes'
                    })

    def save(self, *args, **kwargs):
        # Generar un username basado en el email
        if not self.username:
            self.username = self.email.split('@')[0]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email
    
    def obtenerTratamiento(self):
        # Devuelve tratamientos activos del estudiante
        return tipoTratamiento.objects.filter(
            id__in=horarios.objects.filter(
                estudiante=self,
                fecha_seleccionada__gte=datetime.now().date()
            ).values_list('tipoTratamiento_id', flat=True).distinct()
        )
    
    def is_approved(self):
        # Comprueba si el usuario está aprobado
        return self.estado_aprobacion == 'aprobado'
    
        
    def obtenerUniversidad (self):
        return Universidad.objects.get(id=self.id_universidad)['nombre']

        

    
class FichaClinica(models.Model):
    idFicha = models.BigAutoField(primary_key=True)
    paciente = models.ForeignKey(customuser, on_delete=models.SET_NULL, null=True, default=None)
    tratamiento = models.ForeignKey(tipoTratamiento, on_delete=models.SET_NULL, null=True, default=None)
    motivo_consulta = models.TextField(null=True)
    sintomas_actuales = models.TextField(null=True)
    diagnostico = models.TextField(null=True)
    tratamiento_actual = models.TextField(null=True)
    nombre_contacto_emergencia = models.TextField(null=True)
    telefono_contacto_emergencia = models.IntegerField(null=True)

    def __str__(self):
        return str(self.idFicha)








class horarios(models.Model):
    id = models.BigAutoField(primary_key=True)
    tipoTratamiento = models.ForeignKey(tipoTratamiento, on_delete = models.SET_NULL, null=True, default=None)
    inicio = models.TimeField()
    fecha_seleccionada = models.DateField()
    estudiante = models.ForeignKey(customuser, on_delete=models.SET_NULL, null=True, default=None, related_name="horarios_estudiante")
    paciente = models.ForeignKey(customuser, on_delete=models.SET_NULL, null=True, default=None, related_name="horarios_paciente_views")
    ficha_clinica = models.ForeignKey(FichaClinica, on_delete=models.SET_NULL, null=True, blank=True)
    def _str_(self):
         return str(self.id)
    
    def __str__(self):
        return f"Cita con {self.paciente} el {self.fecha_seleccionada} a las {self.inicio}"


    def __str__(self):
        return f"Ficha Clínica de {self.paciente.email} - Última consulta: {self.fecha_ultima_consulta}"

# models.py

class Cita(models.Model):
    paciente = models.ForeignKey(customuser, on_delete=models.CASCADE, related_name='citas_paciente')
    estudiante = models.ForeignKey(customuser, on_delete=models.CASCADE, related_name='citas_estudiante')
    tipotratamiento = models.ForeignKey(tipoTratamiento, on_delete=models.SET_NULL, null=True)
    fecha_seleccionada = models.DateField()
    inicio = models.TimeField()
    direccion =models.ForeignKey(Universidad, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"Cita de {self.paciente.email} con {self.estudiante.email} para {self.tipotratamiento.nombreTratamiento} el {self.fecha_seleccionada} a las {self.inicio}"


class Historial_Medico(models.Model):
    idHistorial = models.BigAutoField(primary_key=True)
    paciente = models.ForeignKey(customuser, on_delete=models.SET_NULL, null=True, default=None)
    fecha_cita = models.ForeignKey(Cita, on_delete=models.SET_NULL, null=True)
    medicamentos = models.TextField(null=True)
    diagnostico = models.TextField(null=True)

    def _str_(self):
         return str(self.idHistorial)















#NO OCUPAR ESTA TABLA PORQUE YA ESTA CREADA, BORRAR DESDE EL MYSQL
class Tratamiento(models.Model): #NO OCUPAR ESTA TABLA PORQUE YA ESTA CREADA, BORRAR DESDE EL MYSQL
    id = models.BigAutoField(primary_key=True) #NO OCUPAR ESTA TABLA PORQUE YA ESTA CREADA, BORRAR DESDE EL MYSQL
    nombre = models.CharField(max_length=100, unique=True) #NO OCUPAR ESTA TABLA PORQUE YA ESTA CREADA, BORRAR DESDE EL MYSQL
    descripcion = models.TextField(null=True, blank=True) #NO OCUPAR ESTA TABLA PORQUE YA ESTA CREADA, BORRAR DESDE EL MYSQL
    
    def __str__(self):
        return self.nombre
    