from django.contrib import admin
from blog.models import Post, Tag, Comment


admin.site.register(Post)
admin.site.register(Tag)
# admin.site.register(Comment)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        'author',
        'post',]

    raw_id_fields = ['post', 'author',]


    def get_post_author_title(self, obj):
        return f'{obj.author.username} under {obj.post.title}'

    get_post_author_title.short_description = 'КОММЕНТАРИЙ'


    # def get_queryset(self, request):
    #     queryset = super().get_queryset(request)
    #     queryset = queryset.annotate(
    #         _user_count=Count("user", distinct=True),
    #     )
    #     return queryset


    # def get_speach(self, obj):
    #     speach = obj.speach.title
    #     if len(speach) > 50:
    #         return f'{speach[:50]}...'

    #     return speach

    # get_speach.short_description = 'К докладу'


    # def get_user_count(self, obj):
    #     return format_html("<b><i>{}</i></b>", obj._user_count)

    # get_user_count.short_description = 'Кол-во вопросов'
    # get_user_count.admin_order_field = '_user_count'