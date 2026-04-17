from src.custom_stack_class import CustomStack

class NumberAscOrder:
    def sort(self, stack: CustomStack) -> list:
        """
        Extrai os itens de uma CustomStack e retorna uma lista com os números ordenados de forma ascendente.
        """
        elements = []
        while not stack.is_empty():
            elements.append(stack.pop())
        
        elements.sort()
        return elements
