from django.shortcuts import render, redirect, get_object_or_404
from introduce.models import SayingPost, Subject

# Create your views here.

def intro(request):
    context = {"book":"어린 왕자", "year":"16"}

    return render(request, 'introduce/intro.html', context)


def board(request):
    subjects = Subject.objects.all()

    return render(request, 'introduce/board.html', {'subjects': subjects})

#
# def board_form(request):
#     if request.method == 'POST':
#
#     else:
#         form = SayingPostForm()
#
#         return render(request, 'introduce/board_form.html', {'form': form})
#
#     return render(request, 'introduce/board_form.html')
#

def detail(request, subject_id):
    subject = Subject.objects.get(pk=subject_id)

    return render(request, 'introduce/detail.html', {'subject': subject})


def delete(request, subject_id):
    post = SayingPost.objects.get(pk=subject_id)
    post.delete()

    return redirect('introduce:board')


def vote(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)

    try:
        selected_saying = subject.choice_set.get(pk=request.POST['choice'])

    except (KeyError, SayingPost.DoesNotExist):
        return render(request, 'introduce/detail.html', {'subject': subject})

    else:
        selected_saying.votes += 1
        selected_saying.save()

        return redirect('introduce:result', subject_id = subject.id)


def result(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)

    return render(request, 'introduce/result.html', {'subject': subject})



# def update(request, subject_id):
#     post = SayingPost.objects.get(pk=subject_id)
#     if request.method == 'POST':
#         form = SayingPostForm(request.POST, instance=post)
#
#         if form.is_valid():
#             post = form.save()
#
#             return redirect('introduce:detail', post_id=post_id)
#
#     else:
#         form = SayingPostForm(instance=post)
#
#         return render(request, 'introduce/board_form.html', {'form': form})
#
#     return redirect('introduce:detail', post_id=post_id)