import pytest
from src.custom_stack_class import *

def test_push_one_elementinstack():
    element_value = 5.0
    value = 0.0

    cut = CustomStack(5)
    cut.push(element_value)
    assert cut.is_empty() == False
    assert element_value == cut.top()
    assert 1 == cut.size()

def test_pop_one_element_from_stack():
    element_value = 5.0
    cut = CustomStack(5)
    cut.push(element_value)
    
    popped_value = cut.pop()
    
    assert popped_value == element_value
    assert cut.is_empty() == True
    assert 0 == cut.size()

def test_top_one_element_in_stack():
    element_value = 5.0
    cut = CustomStack(5)
    cut.push(element_value)
    
    top_value = cut.top()
    
    assert top_value == element_value
    assert cut.is_empty() == False
    assert 1 == cut.size()

def test_push_until_stack_is_full():
    cut = CustomStack(2)
    cut.push(1)
    cut.push(2)
    
    with pytest.raises(StackFullException):
        cut.push(3)

def test_pop_from_empty_stack():
    cut = CustomStack(1)
    
    with pytest.raises(StackEmptyException):
        cut.pop()

def test_top_from_empty_stack():
    cut = CustomStack(1)
    
    with pytest.raises(StackEmptyException):
        cut.top()