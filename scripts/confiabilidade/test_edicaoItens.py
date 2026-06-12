import pytest
import json
import logging
from django.urls import reverse
from apps.dashboard.models import ProductTable


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__) 




@pytest.mark.django_db
class TestEditarItensPUT:

    def test_cadastro_produto_com_sucesso(self, client):
        """Métrica: Avalia o cadastro de um produto válido (Status 201)"""
        
        lista = [ {
                "product_name": "Teclado Mecânico Wireless",
                "category": "eletrônicos",
                "price": 349.90,
                "amount": 15,
                "description": "Teclado RGB switch blue."
            },  {
                "product_name": "monitor 4k",
                "category": "eletrônicos",
                "price": 500.90,
                "amount": 10,
                "description": "monitor"
            },
            {
                "product_name": "mouse",
                "category": "periféricos",
                "price": 100,
                "amount": 50,
                "description": "mouse mouse"
            }
        ]
        
        url = reverse('product_manager')
        
        for i in range(0, 3):
            produto_atual = lista[i]
            
            resposta_post = client.post(url, data=json.dumps(produto_atual), content_type='application/json')
            if resposta_post.status_code != 201:
                print(f"\n[ERRO PREPARAÇÃO - POST]: {resposta_post.json()}")
            assert resposta_post.status_code == 201
            
            dados_cadastrados = resposta_post.json()
            nome_original = dados_cadastrados["product_name"]

            dados_edicao = {
                "product_name_original": nome_original,  
                "price": round(float(produto_atual["price"]) * 1.05, 2),  
                "description": f"{produto_atual['description']} (PRODUTO ATUALIZADO NO TESTE)"
            }
            
            ProdStatus.total_put += 1
            resposta_put = client.put(url, data=json.dumps(dados_edicao), content_type='application/json')
            
            try:
                if resposta_put.status_code != 202:
                    print(f"\n[ERRO DO SERIALIZER NO PUT]: {resposta_put.json()}")
                
                assert resposta_put.status_code == 202
                
                dados_atualizados = resposta_put.json()
                assert "PRODUTO ATUALIZADO NO TESTE" in dados_atualizados["description"]
                
                ProdStatus.put_sucesso_esperado += 1

            except Exception as e:
                ProdStatus.put_falha += 1
                logger.error(f"Falha no fluxo de edição esperada estável: {e}.")
                raise e
        
    def test_edicao_produto_invalido_deve_barrar(self, client):
        """Métrica: Avalia se a view barra edições inválidas no PUT (Status 400)"""
        
        lista = [ {
                "product_name": "Teclado Mecânico Wireless",
                "category": "eletrônicos",
                "price": 349.90,
                "amount": 15,
                "description": "Teclado RGB switch blue."
            },  {
                "product_name": "monitor 4k",
                "category": "eletrônicos",
                "price": 500.90,
                "amount": 10,
                "description": "monitor"
            },
            {
                "product_name": "mouse",
                "category": "periféricos",
                "price": 100,
                "amount": 50,
                "description": "mouse mouse"
            }
        ]
        listaPriceEdicao = ["preco", 135, 50]
        listadescricao = ["", "novo preco", "eletronicos"]
        listaquantidade = [1, -10, "trinta"]
        
        erros_acumulados = []
        url = reverse('product_manager')
        
        for i in range(0, 3):
            produto_atual = lista[i]
            
            resposta_post = client.post(url, data=json.dumps(produto_atual), content_type='application/json')
            assert resposta_post.status_code == 201
            
            dados_cadastrados = resposta_post.json()
            nome_original = dados_cadastrados["product_name"]

            dados_edicao = {
                "product_name_original": nome_original,  
                "price": listaPriceEdicao[i],  
                "description": listadescricao[i],
                "amount": listaquantidade[i]
            }

            ProdStatus.total_put += 1
            resposta_put = client.put(url, data=json.dumps(dados_edicao), content_type='application/json')
            
            try:
                msg_erro = (
                    f"\n"
                    f"[FALHA DE VALIDAÇÃO NO ÍNDICE {i}]:\n"
                    f"O sistema DEVERIA ter barrado (Status 400), mas respondeu com Status {resposta_put.status_code}.\n"
                    f"Dados enviados: Preço={listaPriceEdicao[i]} | Qtd={listaquantidade[i]}\n"
                    f"Resposta do Banco: {resposta_put.json()}\n"
                )
                
                assert resposta_put.status_code == 400, msg_erro
                
                dados_resposta = resposta_put.json()
                assert len(dados_resposta) > 0 
                
                ProdStatus.put_barrado_esperado += 1
                
            except AssertionError as e:
                ProdStatus.put_falha += 1
                print(e)
                erros_acumulados.append(str(e)) 
                
            except Exception as e:
                ProdStatus.put_falha += 1
                logger.error(f"Erro inesperado no sistema: {e}")
                erros_acumulados.append(str(e))
