# myapp/api.py
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from tastypie import fields

from models import Set, Paste, Commit
from django.contrib.auth.models import User

class JsonModelResource(ModelResource):
    def determine_format(self, request):
        """Used to determine the desired format from the request.format attribute.
        """
        if('format' in request.REQUEST):
            return self._meta.serializer.get_mime_for_format(request.REQUEST['format'])
        ## This is what would be needed to handle .json
        #if (hasattr(request, 'format') and request.format in self._meta.serializer.formats):
        #    return self._meta.serializer.get_mime_for_format(request.format)
        return 'application/json'


class UserResource(JsonModelResource):

    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        collection_name = 'users'
        excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
        allowed_methods = ['get']

class SetResource(JsonModelResource):
    owner = fields.ForeignKey(UserResource, 'owner', null=True, blank=True, default=None, full=True)

    class Meta:
        queryset = Set.objects.exclude(private=True)
        resource_name = 'paste'
        collection_name = 'pastes'
        excludes = ['private_key','repo']
        allowed_methods = ['get']
        # include_absolute_url = True

    def dehydrate(self, bundle):
        pr = PasteResource()
        files = []
        for paste in bundle.obj.commit_set.latest('created').paste_set.all():
            pr_bundle = pr.build_bundle(obj=paste,request=bundle.request)
            pr_json = pr.full_dehydrate(pr_bundle, for_list=True)
            files.append(pr_json)

        #pr.serialize(None, bundles, self.determine_format(bundle.request))
        bundle.data['files'] = files
        return bundle

    def apply_authorization_limits(self, request, object_list):
        if not request.user.is_authenticated():
            object_list = object_list.exclude(private=True)
        else:
            object_list = object_list.exclude(~Q(owner=request.user.pk), private=True)


class CommitResource(JsonModelResource):
    owner = fields.ForeignKey(UserResource, 'owner', null=True, blank=True, default=None)
    paste = fields.ForeignKey(SetResource, 'parent_set')

    class Meta:
        queryset = Commit.objects.all()
        resource_name = 'commit'
        collection_name = 'commits'
        allowed_methods = ['get']


class PasteResource(JsonModelResource):
    commit = fields.ForeignKey(CommitResource, 'revision')

    class Meta:
        queryset = Paste.objects.all()
        resource_name = 'file'
        collection_name = 'files'
        fields = ['filename','language','revision']
        excludes = ['absolute_path','repo','paste_formatted']
        allowed_methods = ['get']

    def dehydrate(self, bundle):
        del bundle.data['resource_uri']
        return bundle
