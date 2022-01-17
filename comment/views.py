from django.db.models import Q
from django.shortcuts import render, redirect
from comment.forms import CommentForm
from comment.models import Comment




def register(request):
    if request.method == "GET":   # 기본값이 GET  무조건 있어야함. 이게 없으면 일단 페이지를 보여주지를 못함
        commentForm = CommentForm()    #입력칸에 아무것도 없는 상태로 준다
        return render(request, 'comment/register.html',
                      {'commentForm':commentForm})
    # render라는 함수가 boardForm의 데이터 board폴더에 forms.py 안에 있는 데이터  받아와 board/register3.html을 완성시킨다는 개념

    elif request.method == "POST" :
        commentForm = CommentForm(request.POST)
        # 모델폼을 이용하면 알아서 다 받아짐
        if commentForm.is_valid():   #boardForm안에 값이 유효한다면
            board = commentForm.save(commit=False)
            board.save()
            return redirect('/comment/register')

def posts(request) :
    posts = Comment.objects.all()     #board table에서 모든 데이터를 다 가져옴

    return render(request, 'comment/list.html',
                  {'posts': posts})


def read(request, bid) :
    post = Comment.objects.get( Q(id=bid))    #bid에 해당하는 내용이 post에 담기고
    # sql에서 where라는 조건 지정한것처럼 조건을 지정한다.
    # 게시글의 id를 불러올 것이다
    # bid는 사용자가 누른 게시글에 대한 얘기
    return render(request, 'comment/read.html',{'read' : post})

def delete(request, bid) :
    post = Comment.objects.get(Q(id = bid))
    post.delete()
    return redirect('/comment/list')

# 수정은 게시글 조회와 작성을 한번에 보여줘야해서 가장 어려움

def update(request, bid) :
    post = Comment.objects.get(Q(id=bid))  #게시글 하나를 가져오는것
    if request.method == "GET" :
        # boardForm = BoardForm()      #입력칸에 아무것도 없는 상태로 준다
        commentForm = CommentForm(instance=post)  # 입력칸에 아무것도 없는 상태로 준다
        return render(request,'comment/update.html',{'commentForm' : commentForm})
    elif request.method == "POST" :
        commentForm = CommentForm(request.POST)
        # boardForm에서 사용자가 보내온 데이터를 받느다
        if commentForm.is_valid():   #boardForm안에 값이 유효한다면
            post.title = commentForm.cleaned_data['title']
            print(commentForm)
            post.contents = commentForm.cleaned_data['contents']
            post.save()
            # return redirect('/board/read/' + str(bid))
            return redirect('/comment/list')
