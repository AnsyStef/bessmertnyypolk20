from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .forms import SearchForm
from .models import Search, Person

def index(request):
    form = SearchForm()
    if request.method == 'POST':
        if form.is_valid:
            search_item = request.POST['search']
            return HttpResponseRedirect(f'/search={search_item}/')
        else:
            return HttpResponseRedirect('/')
    else:
        return render(request, 'index.html', context={'form': form})

def search(request, search_item):
    data = Person.objects.all()
    return render(request, 'search_result.html', context={'search_item': search_item,'people' : data})

def detail(request, pk):
    person = get_object_or_404(Person, pk=pk)
    return render(request, 'detail.html', context={'person': person})

def fillDB(request):
    import os
    from .models import Person
    directory = os.fsencode("D:/Py/project/static/files/")
    for file in os.listdir(directory):
        filename = os.fsdecode(file)

        if filename.endswith('.txt'):
            description = open(f"D:/Py/project/static/files/{filename}",'r')
            desc_data = description.read()
            description.close()

            if desc_data == '':
                desc_data = 'Подробностей не найдено.'
            elif desc_data:
                '.'.join(desc_data)
                tmp = list(desc_data)
                tmp[0] = tmp[0].upper()
                desc_data = "".join(tmp)

            name = str(filename.replace('.txt', ''))
            image = str(filename.replace('.txt', '.png'))
            Person.objects.create(name=name, description=desc_data, image=image)

    return HttpResponseRedirect('/')