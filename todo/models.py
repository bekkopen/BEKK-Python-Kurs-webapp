from django.db import models

class Task (models.Model):
    text = models.TextField()
    place = models.IntegerField(default=0)
    
    def __unicode__ (self):
        if len(self.text) > 30:
            return self.text[:30] + "..."
        
        return self.text