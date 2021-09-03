from django.shortcuts import render
from datetime import date

post_django = {
    'titulo': 'Curso de Django',
    'autor': 'Gabriela',
    'fecha': date(2021,9,2),
    'contenido': 'Lorem ipsum dolor sit, amet consectetur adipisicing elit. Excepturi hic error eius architecto sint, reiciendis quos velit sunt illum earum fuga illo possimus itaque enim debitis placeat. Maxime, provident praesentium?\nLorem ipsum dolor sit, amet consectetur adipisicing elit. Excepturi hic error eius architecto sint, reiciendis quos velit sunt illum earum fuga illo possimus itaque enim debitis placeat. Maxime, provident praesentium?\nLorem ipsum dolor sit, amet consectetur adipisicing elit. Excepturi hic error eius architecto sint, reiciendis quos velit sunt illum earum fuga illo possimus itaque enim debitis placeat. Maxime, provident praesentium?',
    'modalidad': 'Virtual',
    'resumen': 'En este curso aprenderás a desarrollar sitios y aplicaciones web con python y el framework django',
    'imagen': 'blog/images/django.jpg',
}
post_peluqueria = {
    'titulo': 'Curso de Peluqueria',
    'autor': 'Carlos',
    'fecha': date(2021,9,2),
    'contenido': 'Se realiza todos los Miercoles a  las 19hs.',
    'modalidad': 'Presencial',
    'resumen': 'En este curso se aprenderan los conceptos de peluqueria',
    'imagen': 'blog/images/peluqueria.png',
}
post_panaderia = {
    'titulo': 'Curso de panaderia',
    'autor': 'Carlos',
    'fecha': date(2021,9,2),
    'contenido': 'Se realiza todos los Miercoles a  las 19hs.',
    'modalidad': 'Presencial',
    'resumen': 'En este curso se aprenderan los conceptos de panaderia',
    'imagen': 'blog/images/panadero.png',
}
post_fotografia = {
    'titulo': 'Curso de fotografia',
    'autor': 'Carlos',
    'fecha': date(2021,9,2),
    'contenido': 'Se realiza todos los Miercoles a  las 19hs.',
    'modalidad': 'Presencial',
    'resumen': 'En este curso se aprenderan los conceptos de fotografia',
    'imagen': 'blog/images/fotografia.png',
}
lista_posts = [
    post_django,
    post_peluqueria,
    post_panaderia,
    post_fotografia,
]


# Create your views here.

def starting_page(request):
    print ('lista_posts', lista_posts)
    return render(request, "blog/index.html", {'posteos': lista_posts})


def posts(request):
    return render(request, "blog/posts.html", {'posteos': lista_posts})

def post_detail(request, slug):
    print ('slug', slug)
    post = {}
    if slug == 'curso-de-django':
        post = lista_posts[0]
    elif slug == 'curso-de-peluqueria':
        post = lista_posts[1]
    elif slug == 'curso-de-panaderia':
        post = lista_posts[2]
    else:
        post = lista_posts[3]

    return render(request, "blog/post-detail.html", {'curso': post})

