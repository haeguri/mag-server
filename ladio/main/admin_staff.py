__author__ = 'haegyun'


from django.contrib import admin
from django.contrib.admin import AdminSite
from main.models import Content, Channel
from authentication.forms import StaffAuthenticationForm
from django.contrib.auth import get_user_model
from django_summernote.admin import SummernoteModelAdmin

User = get_user_model()

class AdminStaffSite(AdminSite):
    site_header = '컨텐츠 제작자 페이지'
    login_form = StaffAuthenticationForm

    def has_permission(self, request):
        return request.user.is_active and request.user.is_staff

admin_staff = AdminStaffSite(name="admin_staff")

@admin.register(Content, site=admin_staff)
class ContentAdmin(SummernoteModelAdmin):

    list_display = ['thumb_preview', 'channel', 'title', 'created', 'updated']
    fieldsets = (
        (None,  {'fields': ('channel', 'title', 'thumb_img', 'body', )}),
    )

    def get_queryset(self, request):
        qs = super(ContentAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(channel__user=request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "channel" and not request.user.is_superuser:
            # ForeignKey 필드의 "channel"은 무조건 로그인한 유저가 소유한 채널로 제한한다.
            kwargs["queryset"] = Channel.objects.filter(user=request.user)
        return super(ContentAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def thumb_preview(self, obj):
        if obj.thumb_img:
            return '<img src="%s" style="height: 50px; width: auto">' % (obj.thumb_img.url)
        else:
            "no image"

    thumb_preview.allow_tags = True
    thumb_preview.short_description = "썸네일 이미지"


# @admin.register(Channel, site=admin_staff)
# class ChannelAdmin(admin.ModelAdmin):
#     # form = ChannelAdminForm
#
#     list_display = ['bg_preview', 'ch_name', 'user', 'created']
#     fieldsets = (
#         (None,  {'fields': ('user', 'ch_name', 'bg_img', 'brief', 'intro')}),
#     )
#
#     def get_queryset(self, request):
#         qs = super(ChannelAdmin, self).get_queryset(request)
#         if request.user.is_superuser:
#             return qs
#         return qs.filter(user=request.user)
#
#     def formfield_for_foreignkey(self, db_field, request, **kwargs):
#         if db_field.name == "user" and not request.user.is_superuser:
#             # "channel" 입력값은 무조건 로그인한 유저가 소유한 채널로 제한한다.
#             kwargs["queryset"] = User.objects.filter(id=request.user.id)
#         return super(ChannelAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
#
#     def add_view(self, request, form_url="", extra_context=None):
#         data = request.GET.copy()
#         data['user'] = request.user
#         request.GET = data
#         return super(ChannelAdmin, self).add_view(request, form_url="", extra_context=extra_context)
#
#     def bg_preview(self, obj):
#         if obj.bg_img:
#             return '<img src="%s" style="height: 50px; width: auto">' % (obj.bg_img.url)
#         else:
#             "no image"
#
#     bg_preview.allow_tags = True
#     bg_preview.short_description = "채널 배경화면"
