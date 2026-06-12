import pytest
import json
import logging
from django.urls import reverse


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__) 

@pytest.mark.django_db
class TestCadastroProdutosPOST:

    def test_cadastro_produto_com_sucesso(self, client):
        lista = [
            {
                "product_name": "Teclado Mecânico Wireless",
                "category": "eletrônicos",
                "price": 349.90,
                "amount": 15,
                "description": "Teclado RGB switch blue."
            },
            {
                "product_name": "Monitor 4k",
                "category": "eletrônicos",
                "price": 500.90,
                "amount": 10,
                "description": "monitor"
            },
            {
                "product_name": "Mouse",
                "category": "periféricos",
                "price": 100,
                "amount": 50,
                "description": "mouse mouse"
            }
        ]
        
        url = reverse('product_manager')
        
        for produto_atual in lista:
            ProdStatus.total += 1  
            resposta = client.post(url, data=json.dumps(produto_atual), content_type='application/json')
            
            try:
                if resposta.status_code != 201:
                    print(f"\n[ERRO DO SERIALIZER]: {resposta.json()}")
                assert resposta.status_code == 201
                dados_resposta = resposta.json()
                assert dados_resposta["product_name"] == produto_atual["product_name"]
                ProdStatus.cadastros_sucesso += 1
            except Exception as e:
                ProdStatus.cadastros_falha += 1
                logger.error(f"Falha ao cadastrar produto válido: {e}. Status recebido: {resposta.status_code}")
                raise e
        

    def test_cadastro_produto_campos_vazios_deve_barrar(self, client):
        ProdStatus.total += 1
        
        produto_errado = {
            "product_name": "",
            "category": "",
            "price": 1,
            "amount": 50,
            "description": "mouse vazio"
        }
        
        url = reverse('product_manager')
        resposta = client.post(url, data=json.dumps(produto_errado), content_type='application/json')
        
        try:
            assert resposta.status_code == 400
            dados_resposta = resposta.json()
            assert len(dados_resposta) > 0 
            ProdStatus.entradas_invalidas_barradas += 1
        except Exception as e:
            ProdStatus.cadastros_falha += 1
            logger.error(f"O sistema NÃO barrou o produto com campos vazios: {e}. Status: {resposta.status_code}")
            raise e


    def test_cadastro_produto_quantidade_negativa_deve_barrar(self, client):
        ProdStatus.total += 1
        
        produto_negativo = {
            "product_name": "Produto",
            "category": "eletrônicos",
            "price": 100,
            "amount": -10,
            "description": "estoque negativo"
        }
        
        url = reverse('product_manager')
        resposta = client.post(url, data=json.dumps(produto_negativo), content_type='application/json')
        
        try:
            assert resposta.status_code == 400
            ProdStatus.entradas_invalidas_barradas += 1
        except Exception as e:
            ProdStatus.cadastros_falha += 1
            logger.error(f"O sistema NÃO barrou a quantidade negativa! Status recebido: {resposta.status_code}")
            raise e
        
    def test_cadastro_produto_quantidade_negativa_deve_barrar(self, client):
        ProdStatus.total += 1
        
        produto_negativo = {
            "product_name": "Produto",
            "category": "eletrônicos",
            "price": -100,
            "amount": 10,
            "description": "estoque negativo"
        }
        
        url = reverse('product_manager')
        resposta = client.post(url, data=json.dumps(produto_negativo), content_type='application/json')
        
        try:
            assert resposta.status_code == 400
            ProdStatus.entradas_invalidas_barradas += 1
        except Exception as e:
            ProdStatus.cadastros_falha += 1
            logger.error(f"O sistema NÃO barrou a quantidade negativa! Status recebido: {resposta.status_code}")
            raise e
