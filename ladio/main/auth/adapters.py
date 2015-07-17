from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.account.utils import user_username

from allauth.account.adapter import DefaultAccountAdapter

class MessageFreeAdapter(DefaultAccountAdapter):
    def add_message(self, request, level, message_template,
                        message_context=None, extra_tags=''):
        pass

class SocialAccountAdapter(DefaultSocialAccountAdapter):
    def populate_user(self,
                    request,
                    sociallogin,
                    data):
        user = super(SocialAccountAdapter, self).populate_user(request, sociallogin, data)
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        user_username(user, last_name+first_name)
        return user
