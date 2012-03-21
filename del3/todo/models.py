from django.db import models

class Task (models.Model):
    text = models.CharField(max_length=1000)
    place = models.IntegerField(default=0, editable=False)
    
    def __unicode__ (self):
        if len(self.text) > 30:
            return self.text[:30] + "..."
        
        return self.text