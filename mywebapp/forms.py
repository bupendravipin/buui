from django import forms
from django.forms import ModelForm,fields
from django.forms.models import fields_for_model
from mywebapp.models import Product

class modelform(forms.Form):
    cluster_query=Product.objects.values_list('Cluster').order_by('Cluster').distinct().all()
    cluster_choice=[(i[0],i[0]) for i in cluster_query]
    cluster_choice.insert(0,("Select a Value","Select a Value"))
    business_query=Product.objects.values_list('Business').order_by('Business').distinct().all()
    business_choice=[(i[0],i[0]) for i in business_query]
    business_choice.insert(0,("Select a Value","Select a Value"))
    category_query=Product.objects.values_list('Category').order_by('Category').distinct().all()
    category_choice=[(i[0],i[0]) for i in category_query]
    category_choice.insert(0,("Select a Value","Select a Value"))
    product_query=Product.objects.values_list('Product_id').order_by('Product_id').distinct().all()
    product_choice=[(i[0],i[0]) for i in product_query]
    product_choice.insert(0,("Select a Value","Select a Value"))
    Cluster=forms.ChoiceField(choices=cluster_choice,initial=0,required=False)
    Business=forms.ChoiceField(choices=business_choice,initial=0,required=False)
    Category=forms.ChoiceField(choices=category_choice,initial=0,required=False)
    Product_Code=forms.ChoiceField(choices=product_choice,required=False,initial=0)
    Frequency=forms.IntegerField(min_value=1,max_value=6,required=False)
    class Meta:
        model=Product
        fields=['Cluster','Business','Category']
        
        
        
    

    
    
    



