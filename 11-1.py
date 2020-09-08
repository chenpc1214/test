def pizza(size,*inner):
    print("這個%d吋的pizza配料有:"%size)
    for x in inner:
        print("----",x)

pizza(5,"海鮮")
pizza(7,"蔬菜","辛香料","起司","香菇","海鮮")        
