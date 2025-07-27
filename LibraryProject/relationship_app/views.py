from django.shortcuts import render, redirect

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books')  # redirect to wherever makes sense
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})
