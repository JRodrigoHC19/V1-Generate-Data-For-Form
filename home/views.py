from django.shortcuts import redirect, render
from faker import Faker
# 
from .forms import UserSimpleForm
from .utils import getEmail_US


def index(req):
    return render(req, 'index.html')


def generator(req):
    kwargs = { "form": UserSimpleForm }
    return render(req, 'generator.html', kwargs)


def preview(req):
    kwargs = { 'count': 0, 'data': [] }
    if req.method == 'POST':    
        kwargs['count'] = int(req.POST['nro_data'])
        
        if kwargs['count'] <= 0:
            return redirect('generator')
        
        fkr = Faker()

        for i in range(1, kwargs['count']+1):
            name_gen = fkr.name()
            kwargs['data'].append({
                "id": i, "full_name": name_gen, 
                "email": getEmail_US(name_gen, req.POST['dominio'])
            })

    kwargs['data'] = kwargs['data']
    return render(req, 'preview.html', kwargs)


