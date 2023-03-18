from django.views.generic.list import ListView
from django.shortcuts import render
from .models import Questions, Company
from .forms import QuestionForm


class QuestionListView(ListView):
    template_name = 'questions_list.html'
    queryset = Questions.objects.all().order_by('-date_time', )


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

def question_create_view(request):
    form = QuestionForm()
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'ask.html', {'thanks': 'Спасибо за ваш вопрос!','form': form })
        else:
            form.errors
    return render(request, 'ask.html', {'form': form})

# AJAX
def load_companies(request):
    division_id = request.GET.get('division_id')
    companies = Company.objects.filter(division_id=division_id).all()
    return render(request, 'companies_dropdown_list_options.html', {'companies': companies})