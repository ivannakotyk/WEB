from django.shortcuts import render, redirect
from .models import Peticions, Vote
from .forms import PeticionsForm
from django.views.generic import DetailView, UpdateView
from django.http import JsonResponse


def petitions(request):
    petition = Peticions.objects.order_by("-date")
    return render(request, 'peticions/peticions_home.html', {"peticions": petition})


class PeticionsDetailView(DetailView):
    model = Peticions
    template_name = 'peticions/details_view.html'
    context_object_name = 'peticion'


class PeticionUpdateView(UpdateView):
    model = Peticions
    template_name = 'peticions/edit.html'
    form_class = PeticionsForm


def deleteItem(request, id):
    item = Peticions.objects.get(id=id)
    item.delete()
    return redirect('/petitions')


def get_absolute_url(self):
    return {self.path}


def get_initial(self):
    return {{self.user}}


def vote_petition(request, id):
    petition = Peticions.objects.get(id=id)
    user = request.user
    # Check if user has already voted
    if Vote.objects.filter(petition=petition, user=user).exists():
        return JsonResponse({'status': 'error', 'message': 'You have already voted on this petition.'})

    # Create new vote object
    vote = Vote(petition=petition, user=user, name=f"Pet_id: {petition.id} -- User_id: {user.id}")
    vote.save()

    # Update petition's vote count
    petition.vote_count += 1
    petition.save()

    return JsonResponse({'status': 'success', 'message': 'Your vote has been recorded.'})


def create(request):
    error = ""
    if request.method == 'POST':
        form = PeticionsForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.creator = request.user
            form.save()
            return redirect('/petitions')
        else:
            error = "Form was incorrect"

    form = PeticionsForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'peticions/create.html', data)
