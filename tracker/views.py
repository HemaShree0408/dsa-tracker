from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .models import Topic, Problem
from .forms import TopicForm, ProblemForm

def topics_list(request):
    topics = Topic.objects.all()

    return render(
        request,
        'tracker/topics.html',
        {'topics': topics}
    )
# Problem list view to display all problems associated with a specific topic. It retrieves the topic based on the provided topic_id and fetches all problems related to that topic. The view then renders the 'tracker/problems.html' template, passing the topic and its associated problems as context.
def topic_problems(request, topic_id):

    topic = get_object_or_404(Topic, id=topic_id)

    problems = Problem.objects.filter(topic=topic)

    return render(
        request,
        'tracker/problems.html',
        {
            'topic': topic,
            'problems': problems
        }
    )

def add_topic(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            Topic.objects.create(name=name)
    return redirect('topics_list')

def delete_topic(request, topic_id):
    if request.method == 'POST':
        topic = get_object_or_404(Topic, id=topic_id)
        topic.delete()
    return redirect('topics_list')

def edit_problem(request, problem_id):
    problem = get_object_or_404(Problem, id=problem_id)
    if request.method == 'POST':
        form = ProblemForm(request.POST, instance=problem)
        if form.is_valid():
            form.save()
            return redirect('topic_problems', topic_id=problem.topic.id)
    else:
        form = ProblemForm(instance=problem)
    return render(request, 'tracker/edit_problem.html', {'form': form, 'problem': problem})

#revision list
def revision_list(request):
    problems = Problem.objects.filter(need_revision=True)

    return render(
        request,
        'tracker/revision.html',
        {'problems': problems}
    )

# logic list
def logic_list(request):

    problems = Problem.objects.exclude(
        logic_notes="-"
    )

    return render(
        request,
        'tracker/logic.html',
        {
            'problems': problems
        }
    )

#dashboard view
def dashboard(request):

    topics_count = Topic.objects.count()

    problems_count = Problem.objects.count()

    solved_count = Problem.objects.filter(
        solved=True
    ).count()

    revision_count = Problem.objects.filter(
        need_revision=True
    ).count()

    return render(
        request,
        'tracker/dashboard.html',
        {
            'topics_count': topics_count,
            'problems_count': problems_count,
            'solved_count': solved_count,
            'revision_count': revision_count
        }
    )