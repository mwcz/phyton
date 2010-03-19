from clayto_2.photos.models import Photo
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.admin.views.decorators import staff_member_required

def change(request):
    f = file("/home/zip/clog","w")
    f.write(str(request))
    f.close()

    return render_to_response(
        "admin/photos/change_form.html",
        RequestContext(request, {}),
    )

change = staff_member_required(change)

