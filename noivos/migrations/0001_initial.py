# Generated by Django 5.1.3 on 2025-03-19 19:55

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Convidados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_convidado', models.CharField(max_length=100, null=True)),
                ('whatsapp', models.CharField(blank=True, max_length=25, null=True)),
                ('maximo_acompanhantes', models.PositiveIntegerField(default=0, null=True)),
                ('token', models.CharField(max_length=25)),
                ('status', models.CharField(choices=[('AC', 'Aguardando confirmação'), ('C', 'Confirmado'), ('R', 'Recusado')], default='AC', max_length=2)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='convidados', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Acompanhante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('convidado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acompanhantes', to='noivos.convidados')),
            ],
        ),
        migrations.CreateModel(
            name='MensagemAosNoivos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto_mensagem', models.TextField()),
                ('data_envio', models.DateTimeField(auto_now_add=True)),
                ('escrita_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='noivos.convidados')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mensagens_aos_noivos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MensagemPersonalizada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensagem', models.TextField()),
                ('imagem', models.FileField(blank=True, null=True, upload_to='mensagens_imagens/')),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mensagens_personalizadas', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_primeiro_conjuge', models.CharField(blank=True, max_length=100, null=True)),
                ('nome_segundo_conjuge', models.CharField(blank=True, max_length=100, null=True)),
                ('data_casamento', models.DateField(blank=True, null=True)),
                ('horario_casamento', models.TimeField(blank=True, null=True)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='imagens_perfil/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])),
                ('mensagem_noivos', models.TextField(blank=True, null=True)),
                ('configurado', models.BooleanField(default=False)),
                ('cep', models.CharField(blank=True, max_length=10, null=True)),
                ('rua', models.CharField(blank=True, max_length=150, null=True)),
                ('numero', models.CharField(blank=True, max_length=10, null=True)),
                ('complemento', models.CharField(blank=True, max_length=100, null=True)),
                ('bairro', models.CharField(blank=True, max_length=100, null=True)),
                ('pais', models.CharField(default='Brasil', max_length=50)),
                ('estado', models.CharField(blank=True, max_length=2, null=True)),
                ('municipio', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MensagemSobreNoivoNoiva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('noiva', 'Noiva'), ('noivo', 'Noivo')], max_length=10)),
                ('mensagem', models.TextField()),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mensagens', to='noivos.perfil')),
            ],
        ),
        migrations.CreateModel(
            name='ImagemNoivos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(upload_to='imagems_noivos/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])),
                ('tipo', models.CharField(choices=[('noiva', 'Noiva'), ('noivo', 'Noivo')], max_length=10)),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fotosnoivos', to='noivos.perfil')),
            ],
        ),
        migrations.CreateModel(
            name='ImagemGaleria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(upload_to='imagems_galeria/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='galeria', to='noivos.perfil')),
            ],
        ),
        migrations.CreateModel(
            name='Presentes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_presente', models.CharField(max_length=1000)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='presentes/')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('importancia', models.IntegerField()),
                ('reservado', models.BooleanField(default=False)),
                ('link_sugestao_compra', models.URLField(blank=True, max_length=1000, null=True)),
                ('link_cobranca', models.URLField(blank=True, max_length=500, null=True)),
                ('reservado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='noivos.convidados')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='presentes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
