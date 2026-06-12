import pytest
import json
import logging
import random
from django.urls import reverse
from django.contrib.auth.hashers import make_password
from apps.dashboard.models import UserTable

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)




@pytest.fixture
def criar_usuario_no_banco(db):
    usuarios_para_criar = []
    idUser = 6000000
    
    for i in range(1, 61):  
        idRan = int(random.randint(1,5)*i)
        idUser = idUser + idRan
        senhaCript = make_password(f"UsT{i}")
        usuario = UserTable(
            id=idUser,              
            name=f"usuario_teste_{idUser}",   
            password=senhaCript,
            email=f"teste_{i}@email.com"
        )
        usuarios_para_criar.append(usuario)
    
    usuarios_criados = UserTable.objects.bulk_create(usuarios_para_criar)
    return usuarios_criados


@pytest.mark.django_db
class TestGrupo1LoginSucesso:

    def test_login_com_sucesso(self, client, criar_usuario_no_banco):
        for idx, usuario_alvo in enumerate(criar_usuario_no_banco):
            OperacoesStatus.total += 1
            senha_esperada = f"UsT{idx + 1}"
            
            dados_login = {
                "username": usuario_alvo.name,
                "password": senha_esperada
            }
            
            url = reverse('login') 
            resposta = client.post(url, data=json.dumps(dados_login), content_type='application/json')
            
            try:
                assert resposta.status_code == 200
                dados_resposta = resposta.json()
                assert dados_resposta['message'] == "Login realizado com sucesso!"
                assert client.session['user_id'] == usuario_alvo.id
                OperacoesStatus.sucessos += 1
            except Exception as e:
                OperacoesStatus.falhas += 1
                logger.error(f"Falha no login do usuário {usuario_alvo.name}. Erro: {e}. Status: {resposta.status_code}")
                raise e


@pytest.mark.django_db
class TestGrupo2LoginCamposInvalidos:

    def test_login_campos_vazios_ou_nulos(self, client):
        dados_invalidos = [
            {
                "username": "",
                "password": None
            },
            {
                "username": "usuario_teste_qualquer",
                "password": ""
            }
        ]
        
        url = reverse('login')
        
        for dados in dados_invalidos:
            OperacoesStatus.total += 1
            resposta = client.post(url, data=json.dumps(dados), content_type='application/json')
            
            try:
                assert resposta.status_code == 400
                OperacoesStatus.sucessos += 1
            except Exception as e:
                OperacoesStatus.falhas += 1
                logger.error(f"Falha ao barrar campos vazios/nulos. Erro: {e}. Status recebido: {resposta.status_code}")
                raise e


@pytest.mark.django_db
class TestGrupo3LoginSenhaIncorreta:

    def test_login_senha_errada_para_usuario_existente(self, client, criar_usuario_no_banco):
        usuario_valido = criar_usuario_no_banco[0]
        OperacoesStatus.total += 1
        
        dados_senha_errada = {
            "username": usuario_valido.name,
            "password": "SenhaCompletamenteIncorreta123"
        }
        
        url = reverse('login')
        resposta = client.post(url, data=json.dumps(dados_senha_errada), content_type='application/json')
        
        try:
            assert resposta.status_code == 401
            OperacoesStatus.sucessos += 1
        except Exception as e:
            OperacoesStatus.falhas += 1
            logger.error(f"Falha ao barrar senha incorreta. Erro: {e}. Status recebido: {resposta.status_code}")
            raise e
