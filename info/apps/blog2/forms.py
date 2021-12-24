from django import forms
from blog2.models import Comentario, Post

class ComentarioForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'Comenta aquí',
        'rows': '4',
    }))
    class Meta:
        model = Comentario
        fields = ('Contenido', )

'''class PostForm(forms.ModelForm):
	class Meta:
	    model= Post
	    fields = ('autor', 'titulo', 'contenido')

	
    def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()'''        

class Comentario(forms.ModelForm):
    
    class Meta:
        model = Comentario
        fields = ['mensaje',]


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['mensaje'].widget = forms.TextInput(attrs={'class':'textarea--style-6'})        