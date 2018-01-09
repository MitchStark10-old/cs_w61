from chicago_pizza_store import ChicagoPizzaStore

chicagoStore = ChicagoPizzaStore()
pizza = chicagoStore.orderPizza("cheese", 'square')
print("Joel ordered a " + pizza.getName())
print("-----------------------------")
pizza = chicagoStore.orderPizza("clam", 'round')
print("Joel ordered a " + pizza.getName())
print("------------------------------")


pizza = chicagoStore.orderPizza("pepperoni", 'square')
print("Joel ordered a " + pizza.getName())
print("------------------------------")
pizza = chicagoStore.orderPizza("veggie", 'round')
print("Joel ordered a " + pizza.getName())
print("------------------------------")
