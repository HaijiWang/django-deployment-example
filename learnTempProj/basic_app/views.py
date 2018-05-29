from django.shortcuts import render

# Create your views here.
def index_view(request):
    context_dict = {'text':'hello world','number':100}
    return render(request,'basic_app/index_template.html',context_dict)

def other_view(request):
    return render(request,'basic_app/other_template.html')

def relative_view(request):
    return render(request,'basic_app/relative_url_templates.html')
