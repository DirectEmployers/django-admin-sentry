from django import template

from admin_sentry.conf import USER_PROFILE_URL
from admin_sentry.helpers import cache_users

register = template.Library()

actions = {1: 'addition', 2: 'change', 3: 'deletion'}

@register.filter
def trans_actions(action):
    try:
        res = actions[action]
    except:
        res = None
    return res

@register.filter
def abbrev(action):
    return actions[action][0].upper()

@register.filter
def timesince(value):
    '''
    Copied from django-sentry v1.6.2

    github.com/dcramer/django-sentry
    '''
    import datetime
    from django.template.defaultfilters import timesince
    if not value:
        return 'Never'
    if value < datetime.datetime.now() - datetime.timedelta(days=5):
        return value.date()
    value = (' '.join(timesince(value).split(' ')[0:2])).strip(',')
    if value == '0 minutes':
        return 'Just now'
    if value == '1 day':
        return 'Yesterday'
    return value + ' ago'

@register.filter
def get_user_admin_url(value):
    '''
    Given a username (`value`), return a string containing an absolute
    path to the user's admin profile.
    '''
    users = cache_users()
    user = users.get(username=value)
    return "%s/%s" % (USER_PROFILE_URL, str(user.id))
    