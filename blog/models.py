from django.db import models

# Create your models here.
class img (models.Model):
    image = models.ImageField('Rasm', upload_to='images/')
    title = models.CharField('Nomi', max_length=255)
    class Meta :
        verbose_name = 'Rasm'
        verbose_name_plural = 'Rasmlar'
class Menu(models.Model):
    name = models.CharField('Ovqat nomi', max_length=255)
    rasm = models.ImageField('Ovqat rasmi', upload_to='images')
    retsept = models.TextField('Ovqat haqida')
    narxi = models.IntegerField('Narxi', null='True', default=0)
    
    class Meta :
        verbose_name = 'Menu'
        verbose_name_plural = 'Menular'
class Obed(models.Model):
    name = models.CharField('Ovqat nomi', max_length=255)
    rasm = models.ImageField('Ovqat rasmi', upload_to='images')
    retsept = models.TextField('Ovqat haqida')
    narxi = models.IntegerField('Narxi', null='True', default=0)
    
    class Meta :
        verbose_name = 'obed'
        verbose_name_plural = 'obedlar'
class Ujin(models.Model):
    name = models.CharField('Ovqat nomi', max_length=255)
    rasm = models.ImageField('Ovqat rasmi', upload_to='images')
    retsept = models.TextField('Ovqat haqida')
    narxi = models.IntegerField('Narxi', null='True', default=0)
    
    class Meta :
        verbose_name = 'ujin'
        verbose_name_plural = 'ujinlar'

class Povar(models.Model):
    rasm = models.ImageField('Povar rasmi', upload_to='images',)
    facebook = models.URLField('facebook silka', null=True, default="https://www.facebook.com/")
    telegram = models.URLField('telegram silka', null=True, default="https://www.telegram.com/")
    instagram = models.URLField('instagram silka', null=True, default="https://www.instagram.com/")
    name = models.CharField('Povar ismi', max_length=255 , default= "Paloncha Pistonchiyev")
    haqida = models.CharField('Povar haqida', max_length=255, null=True, )
    # twitter = models.URLField('x silka', null=True, default="https://twitter.com/")
    # haqida = models.TextField('Povar haqida')
    class Meta :
        verbose_name = 'povar'
        verbose_name_plural = 'povarlar'
