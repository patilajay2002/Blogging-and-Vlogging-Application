from django.shortcuts import render,get_object_or_404,redirect
from bloga.models import Post,Commentm
from django.core.mail import send_mail
from bloga.forms import EmailSendForm,CommentsForm
from taggit.models import Tag

from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
# Create your views here.
def post_list_view(request,tag__slug=None):
 post_list=Post.objects.all()
 tag=None
 if tag__slug:
   tag=get_object_or_404(Tag,slug=tag__slug)
   post_list=post_list.filter(tags__in=[tag])


 paginator=Paginator(post_list,1)
 page_number=request.GET.get('page')
 try:
  post_list=paginator.page(page_number)
 except PageNotAnInteger:
  post_list=paginator.page(1)
 except EmptyPage:
  post_list=paginator.page(paginator.num_pages)



 return render(request,'bloga/post_list.html',{'post_list':post_list,'tag':tag})


def post_detail_view(request,year,month,day,post):
 post=get_object_or_404(Post,
                                slug=post,
                                status='published',
                                publish__year=year,
                                publish__month=month,
                                publish__day=day,)
 comments=post.comments.filter(active=True) 
 csubmit=False 
 if request.method=='POST': 
  form=CommentsForm(data=request.POST) 
  if form.is_valid(): 
    new_comment=form.save(commit=False) 
    new_comment.post=post 
    new_comment.save() 
    csubmit=True 
 else: 
  form=CommentsForm() 
 return render(request,'bloga/post_detail.html',{'post':post,'form':form,'comments':comments,'csubmit':csubmit}) 
 

def mail_send_view(request,id):
 post=get_object_or_404(Post,id=id,status='published')
 sent=False
 if request.method=='POST':
  form=EmailSendForm(request.POST)
  if form.is_valid():
   cd=form.cleaned_data
   subject='{} ({}) recommends you to read "{}"'.format(cd['name'],cd['email'],post.title) 
   post_url=request.build_absolute_uri(post.get_absolute_url())
   message="Read Post At: \n{}\n\n{}\'s Comments:\n{}".format(post_url,cd['name'],cd["comments"])
   send_mail(subject,message,cd['email'],[cd['to']])
   sent=True
   
 else:
   form=EmailSendForm()

 return render(request,'bloga/sharebymail.html',{'form':form,'post':post,'sent':sent})



# def mail_send_view(request,id): 
#  post=get_object_or_404(Post,id=id,status='published') 
#  sent=False 
#  if request.method=='POST': 
#     form=EmailSendForm(request.POST) 
#     if form.is_valid(): 
#       cd=form.cleaned_data 
#       post_url=request.build_absolute_uri(post.get_absolute_url()) 
#       subject='{}({}) recommends you to read "{}"'.format(cd['name'],cd['email'],
#       post.title) 
#       message='Read Post At: \n {}\n\n{}\' Comments:\n{}'.format(post_url,cd
#       ['name'],cd['comments']) 
#       send_mail(subject,message,'durga@blog.com',[cd['to']]) 
#       sent=True 
#  else: 
#       form=EmailSendForm() 
#  return render(request,'blog/sharebymail.html',{'post':post,'form':form,'sent':sent}) 
#pip install django-taggit and app palce 'taggit' in setting file
