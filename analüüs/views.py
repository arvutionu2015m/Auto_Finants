from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import SignUpForm, UploadForm
from .models import UploadedDocument
from .utils import extract_text_from_csv, analyze_expense_text
from .models import UploadedDocument, AnalysisResult
from django.contrib.auth.decorators import login_required
from .models import AnalysisResult

@login_required
def my_analyses(request):
    analyses = AnalysisResult.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'minu_analüüsid.html', {'analyses': analyses})



def home(request):
    return render(request, 'home.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return render(request, 'logout.html')

@login_required
def upload_file(request):
    analysis = None
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            uploaded_doc = UploadedDocument.objects.create(user=request.user, file=file)

            try:
                extracted_text = extract_text_from_csv(file)
                analysis = analyze_expense_text(extracted_text)

                # Salvestame analüüsi
                AnalysisResult.objects.create(
                    user=request.user,
                    document=uploaded_doc,
                    result_text=analysis
                )
            except Exception as e:
                analysis = f"Viga faili töötlemisel või AI analüüsis: {e}"
    else:
        form = UploadForm()
    return render(request, 'upload.html', {
        'form': form,
        'analysis': analysis
    })
