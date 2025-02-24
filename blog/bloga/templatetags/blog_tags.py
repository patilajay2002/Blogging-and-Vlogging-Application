from bloga.models import Post
from django import template
from django.db.models import Count
register=template.Library()

@register.simple_tag
def total_posts():
 return Post.objects.count()

@register.inclusion_tag('bloga/latest_posts123.html')
def show_latest_post():
 latest_posts=Post.objects.order_by('-publish')[:3]
 return {'latest_posts':latest_posts}

# def most_commented_post_list(count=5):
#  return Post.objects.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]

#base.html
# #        <!-- {%most_commented_post_list as most_commented_posts%}
#         <ul>
#             {% for post in most_commented_posts%}
#             <li><a href="{{post.get_absolute_url}}">{{post.title}}</a></li>
#             {%endfor%}
#      
#    </ul> -->
       