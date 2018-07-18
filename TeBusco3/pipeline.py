from social_core.backends.facebook import FacebookOAuth2
from django.template.defaultfilters import slugify
from django.core.files.base import ContentFile
from urllib.request import urlopen

def save_profile_picture(backend, user, response, details, is_new=False, *args, **kwargs):

    if isinstance(backend, FacebookOAuth2):
        url = 'http://graph.facebook.com/{0}/picture?width=1000'.format(response['id'])
        avatar = urlopen(url)
        user.social_photo.save(slugify(str(user.id)) + '.jpg',
                        ContentFile(avatar.read()))
        user.save()