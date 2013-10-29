from annoying.decorators import render_to
from django.contrib.auth.decorators import login_required
from pagetree.helpers import get_hierarchy
from pagetree.generic.views import generic_view_page
from pagetree.generic.views import generic_edit_page
from pagetree.generic.views import generic_instructor_page


@render_to('main/index.html')
def index(request):
    return dict()


def page(request, path):
    # do auth on the request if you need the user to be logged in
    # or only want some particular users to be able to get here
    h = get_hierarchy("main", "/pages/")
    return generic_view_page(request, path, hierarchy=h)


@login_required
def edit_page(request, path):
    # do any additional auth here
    h = get_hierarchy("main", "/pages/")
    return generic_edit_page(request, path, hierarchy=h)


@login_required
def instructor_page(request, path):
    # do any additional auth here
    h = get_hierarchy("main", "/pages/")
    return generic_instructor_page(request, path, hierarchy=h)
