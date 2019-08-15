from django.db import models

class Event(models.Model):
  event_name = models.CharField(max_length=200)
  organization_name = models.CharField(max_length=200)
  ticket_cost = models.DecimalField(max_digits=8, decimal_places=2)
  event_start_date = models.DateTimeField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return '%s %s %s %s' % (self.event_name, self.organization_name, self.ticket_cost, self.event_start_date)

class Organization(models.Model):
  name = models.CharField(max_length=200)
  organization_id = models.IntegerField(default=200)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return '%s %s' % (self.name, self.organization_id)