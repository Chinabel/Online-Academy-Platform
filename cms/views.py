from django.shortcuts import render
from .models import Course, Review
from .forms import ReviewForm
from django.db.models import Q

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'cms/course_list.html', {'courses': courses})

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    reviews = course.reviews.all()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.course = course
            review.save()
    else:
        form = ReviewForm()
    return render(request, 'cms/course_detail.html', {'course': course, 'reviews': reviews, 'form': form})

def search_courses(request):
    query = request.GET.get('q')
    if query:
        courses = Course.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
    else:
        courses = Course.objects.all()
    return render(request, 'cms/search_results.html', {'courses': courses, 'query': query})
