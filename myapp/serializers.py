from django.forms import widgets
from rest_framework import serializers
from models import Codigos, AuthUser, LANGUAGE_CHOICES, STYLE_CHOICES, Tipo



class CodigosSerializer(serializers.ModelSerializer):
	class Meta:
		model = Codigos
		fields = ('id_code', 'user', 'code', 'nombre_codigo', 'referencia', 'idtipo')


class TipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo
        fields = ('idtipo', 'tipo')
