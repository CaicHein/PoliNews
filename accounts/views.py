from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group, Permission



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            try:
                user_group = Group.objects.get(name="basic_user")
            except Group.DoesNotExist:
                user_group = Group(name="basic_user")
                user_group.save()
                user_group.permissions.set([Permission.objects.get(codename=c) for c in ["add_user", "change_user", "view_user", "view_post", "add_comment", "change_comment", "delete_comment", "view_comment",]])
            user.groups.add(user_group)
            return HttpResponseRedirect(reverse('login'))
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'accounts/signup.html', context)