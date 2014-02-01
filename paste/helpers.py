import re
import unicodedata

from django.utils.safestring import mark_safe


def has_access_to_paste(request, paste_set, private_key=None):
    """ Check whether a user has access to a paste based on the request """
    if paste_set.private and not user_owns_paste(paste_set, request.user):
        if private_key != paste_set.private_key:
            return False
    return True


def user_owns_paste(paste_set, user):
    return user.id and paste_set.owner and (user.pk == paste_set.owner.pk)


def slugify_string(value):
    """
    Converts to lowercase
    Removes non-word characters (allows only ascii alphanumerics and underscores)
    Strips leading and trailing whitespace.
    Converts remaining whitespace to underscores.
    """
    value = unicodedata.normalize('NFKD', unicode(value)).encode('ascii', 'ignore')
    value = re.sub('[^\w\s-]', '', value).strip()
    return mark_safe(re.sub('[-\s]+', '_', value))
