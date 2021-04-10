from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image,ImageDraw
from django.contrib.auth.models import User

# Create your models here.
class location(models.Model):
    location_name = models.CharField(max_length =200)
    location_url = models.CharField(max_length=200,blank=True)
    qr_code = models.ImageField(blank=True)
    infected = models.BooleanField(default=False)
    auth = models.ForeignKey(User,on_delete=models.CASCADE)

    
    def save(self,*args,**kwargs):
        qrcode_img = qrcode.make("https://asistan36.herokuapp.com//location/{}".format(self.id))
        canvas = Image.new('RGB',(500,500),'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)

        fname = f"qr_code_{self.id}.png"
        buffer = BytesIO()
        canvas.save(buffer,'PNG')
        self.qr_code.save(fname,File(buffer),save=False)
        canvas.close()
        super().save(*args,**kwargs)

class user_locations(models.Model):
    auth = models.ForeignKey(User,on_delete=models.CASCADE)
    locations = models.ForeignKey(location,on_delete=models.CASCADE)
    infected = models.BooleanField(default=False)


    