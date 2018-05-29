from django.shortcuts import render, redirect
from lotto.models import GuessNumber
from lotto.forms import PostForm

# Create your views here.


def index(request):
    lottos = GuessNumber.objects.all()
    return render(request, 'lotto/index.html', {'lottos':lottos})


def new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            lotto = form.save(commit=False)
            lotto.generate()

            return redirect('lotto:index')

    else:
        form = PostForm()

        return render(request, 'lotto/form.html', {'form':form})


def detail(request, pk):
    lotto = GuessNumber.objects.get(pk=pk)

    return render(request, 'lotto/detail.html', {'lotto': lotto})


def update(request, pk):
    lotto = GuessNumber.objects.get(pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=lotto)
        if form.is_valid():
            lotto = form.save(commit=False)
            lotto.generate()

            return redirect('lotto:detail', pk=lotto.pk)

    else:
        form = PostForm(instance=lotto)

        return render(request, 'lotto/form.html', {'form':form})

    return redirect('lotto:detail', pk=lotto.pk)


def delete(request, pk):
    if request.method == 'POST':
        lotto = GuessNumber.objects.get(pk=pk)
        lotto.delete()

        return redirect('lotto:index')
