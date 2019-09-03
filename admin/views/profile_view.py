from frontend.models import Profile
from django.shortcuts import render, reverse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from ..forms import ProfileForm


@login_required
@require_http_methods(['POST'])
def update(request, profile_id):
    profile = Profile.objects.get(pk=profile_id)
    form = ProfileForm(request.POST, files=request.FILES, instance=profile)
    if form.is_valid():
        if form.cleaned_data['set_to_default']:
            profile.set_image_to_default()

        form.save()

        messages.success(request, "Profile is successfully updated!")
    else:
        messages.error(request, "Form is invalid")
        return render(request, 'admin/users/show.html',
                      {'form': form, 'user': profile.user})

    return HttpResponseRedirect(
        reverse(
            'admin:users.show',
            args=(
                profile.user.id,
            )))
