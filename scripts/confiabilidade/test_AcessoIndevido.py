import pytest
from django.test import RequestFactory
from django.contrib.sessions.middleware import SessionMiddleware
from apps.dashboard.views import dashboard_view 

@pytest.mark.django_db
class TestDashboardSeguranca:

    def test_metrica_2_2_tentativa_de_acesso_direto_por_url_sem_login(self, client):
        """
        Métrica 2.2: Avalia a capacidade do AGIO de impedir acessos não autorizados
        quando um usuário tenta acessar o painel digitando a URL diretamente.
        """
        url_dashboard = '/dashboard/' 
        
        StatusSeg.tentativas_indevidas += 1
        
        resposta = client.get(url_dashboard)
        
        try:
            assert resposta.status_code == 302
            assert '/login' in resposta.url
            
            StatusSeg.bloqueios_corretos += 1
        except AssertionError as e:
            raise e

    def test_metrica_1_1_e_1_2_acesso_legitimo_com_login(self, client):
        """
        Métrica 1.1 e 1.2: Avalia o fluxo bem-sucedido de login seguido
        pela consulta do inventário.
        """
        url_dashboard = '/dashboard/'
        
        StatusSeg.total_operacoes += 1
        sessao = client.session
        sessao['user_id'] = 1  
        sessao.save()
        StatusSeg.sucessos += 1

        StatusSeg.total_operacoes += 1
        resposta = client.get(url_dashboard)
        
        try:
            assert resposta.status_code == 200
            StatusSeg.sucessos += 1
        except AssertionError:
            StatusSeg.falhas += 1
            raise

