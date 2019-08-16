import json
from django.http import HttpResponse
from tastypie.resources import ModelResource, ALL
from tastypie.authorization import Authorization
from tastypie.exceptions import ImmediateHttpResponse
from api.models import Event
from api.models import Organization

class EventResource(ModelResource):
  class Meta:
    allowed_methods = ['get', 'put']
    authorization = Authorization()
    fields = ['event_name', 'organization_name', 'ticket_cost', 'event_start_date']
    filtering = {
        'event_name': ALL,
        'organization_name': ALL,
        'event_start_date': ['gte', 'lte'],
        'ticket_cost': ['gte', 'lte'],
    }
    resource_name = 'events'

    queryset = Event.objects.all()

  def obj_update(self, bundle, **kwargs):
    errors = {}
    if not bundle.data:
      error['no_data'] = 'No data provided'
    if bundle.data.get('event_name', '') == '':
      errors['event_name'] = 'Event name cannot be empty'
    if bundle.data.get('organization_name', '') == '':
      errors['organization_name_null'] = 'Organization name cannot be empty'
    if bundle.data.get('ticket_cost', '') == '':
      errors['ticket_cost'] = 'Ticket cost cannot be empty'
    if bundle.data.get('event_start_date', '') == '':
      errors['event_start_date'] = 'Start date cannot be empty'
    if Organization.objects.filter(name=bundle.data['organization_name']).exists() is False:
      errors['missing_org'] = 'Organization does not exist'

    if len(errors) == 0:
      return super(EventResource, self).obj_update(bundle, **kwargs)
    else:
      print(errors)
      raise ImmediateHttpResponse(response=HttpResponse(json.dumps(errors), status=500, content_type="application/json"))
