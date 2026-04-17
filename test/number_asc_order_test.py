import pytest
from src.number_asc_order import NumberAscOrder
from src.custom_stack_class import CustomStack

def test_sort_with_random_numbers(mocker):
    # Cenário A: Pilha com 6 números aleatórios
    
    # Mock da CustomStack
    mock_stack = mocker.MagicMock(spec=CustomStack)
    
    # Configura o side_effect para simular múltiplos retornos do pop
    # e o is_empty para controlar o loop
    mocker.patch.object(mock_stack, 'pop', side_effect=[10, 2, 33, 4, 25, 6])
    mocker.patch.object(mock_stack, 'is_empty', side_effect=[False, False, False, False, False, False, True])

    # Instancia a classe e executa o método
    sorter = NumberAscOrder()
    sorted_list = sorter.sort(mock_stack)
    
    # Valida o resultado
    assert sorted_list == [2, 4, 6, 10, 25, 33]
    assert mock_stack.pop.call_count == 6
    assert mock_stack.is_empty.call_count == 7

def test_sort_with_empty_stack(mocker):
    # Cenário B: Pilha vazia
    
    # Mock da CustomStack
    mock_stack = mocker.MagicMock(spec=CustomStack)
    
    # Configura o is_empty para retornar True
    mocker.patch.object(mock_stack, 'is_empty', return_value=True)
    
    # Instancia a classe e executa o método
    sorter = NumberAscOrder()
    sorted_list = sorter.sort(mock_stack)
    
    # Valida o resultado
    assert sorted_list == []
    assert mock_stack.pop.call_count == 0
    assert mock_stack.is_empty.call_count == 1
