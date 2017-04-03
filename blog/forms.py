# coding=utf-8

from django import forms
from blog.models import Article, Category, Tag
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
import markdown
import datetime
import re


class EditarticleForm(forms.Form):
    status = forms.CharField(
        label=u'文章状态',
        widget=forms.HiddenInput()
    )

    title = forms.CharField(
        label=u'文章标题',
        max_length=50,
        error_messages={'required': u'标题不能为空'},
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': u'文章标题', 'title': u'必填'}),
    )

    abstract = forms.CharField(
        label=u'摘要',
        max_length=60,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': u'摘要,简要说明文章内容'}),
    )

    content = forms.CharField(
        label=u'内容',
        min_length=10,
        widget=SummernoteWidget(),
    )

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        label=u'分类',
        error_messages={'required': u'文章分类不能为空'},
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    tags = forms.CharField(
        max_length=30,
        label=u'标签',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': u'多个标签,标签间用空格间隔开'}),
    )

    def save(self):
        title = self.cleaned_data['title']
        body = self.cleaned_data['content']
        status = self.cleaned_data['status']
        abstract = self.cleaned_data['abstract']
        tags = []
        for tag in re.split(r',| +', self.cleaned_data['tags']):
            if tag:
                tags.append(Tag.objects.get_or_create(name=tag.strip())[0])
        category = self.cleaned_data['category']
        article = Article(
            title=title,
            body=body,
            abstract=abstract,
            views=0,
            status=status,
            category=category)
        article.save()
        article.tags.add(*tags)