from django.db import models

# Create your models here.

class Autor (models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()

    def get_nombre(self):
        return f"{self.nombre} {self.apellido}"

    def __str__(self):
        return self.get_nombre()

class Modalidad (models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.nombre}"

class Categoria (models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.nombre}"

class Post (models.Model):
    titulo = models.CharField(max_length=100)
    fecha = models.DateField(auto_now=True)
    contenido = models.TextField()
    resumen = models.CharField(max_length=200)
    #imagen = models.CharField(max_length=100)
    image = models.ImageField(upload_to="posts", null=True)
    slug = models.SlugField()
    autor = models.ForeignKey(Autor, on_delete=models.SET_NULL, null=True)
    modalidad = models.ForeignKey(Modalidad, on_delete=models.PROTECT)
    categorias = models.ManyToManyField(Categoria)
