
from gettext import translation

from django.shortcuts import render,redirect
from deep_translator import GoogleTranslator
from .models import Translation
# Create your views here.
def home(request):  
    text = ""
    translated_text = ""
    languages = GoogleTranslator().get_supported_languages(as_dict=True)
    language = "language"
 

    if request.method == "POST":
        text = request.POST.get("text")
        language = request.POST.get("language")
        

        if text and language:
            translated_text = GoogleTranslator(source='auto',target = language).translate(text)

    translation=Translation(original_text=text, translated_text=translated_text, source_language="English", target_language=language)
    translation.save()
    context = {"translated_text": translated_text ,"languages": languages ,"text": text}
    return render(request, "translatorApp/create.html",context)


Translation.objects.create(
    original_text="",
    translated_text="",
    source_language='auto',
    target_language=""
)
def history(request):
    data = Translation.objects.all().order_by('created_at')
    context = {"data": data}
    return render(request, "translatorApp/history.html", context)


def create_translation(request):
 
    text = ""
    translated_text = ""
    languages = GoogleTranslator().get_supported_languages(as_dict=True)
    language = "language"
 

    if request.method == "POST":
        text = request.POST.get("text")
        language = request.POST.get("language")
        

        if text and language:
            translated_text = GoogleTranslator(source='auto',target = language).translate(text)

    translation=Translation(original_text=text, translated_text=translated_text, source_language="English", target_language=language)
    translation.save()
    context = {"translated_text": translated_text ,"languages": languages ,"text": text}
    return render(request, "translatorApp/create.html",context)


def edit_translation(request,id):
    item = Translation.objects.get(id=id)

    if request.method == "POST":
       item.original_text = request.POST.get("original_text")
       item.translated_text = request.POST.get("translated_text")
       item.source_language = request.POST.get("source_language")
       item.target_language = request.POST.get("target_language")
       item.save()

    context = {"translation": translation}
    return render(request, "translatorApp/edit_translation.html", context)
    
  
 

def delete_translation(request, id):
    item = Translation.objects.get(id=id)
    item.delete()
    return redirect("history")
