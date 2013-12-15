"""Timezone helper functions.

This module uses pytz when it's available and fallbacks when it isn't.
"""

from PoshCode.paste.timezone import activate

from BeautifulSoup import BeautifulSoup

class TimezoneMiddleware(object):
    def process_request(self, request):
        if request.user.is_authenticated():
            tz = request.user.preference.timezone
            if tz:
                activate(tz)
