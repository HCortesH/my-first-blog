from django.shortcuts import render


def post_list(request):
    return render(request,'miblog/post_list.html',
{})
