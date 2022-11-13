def disp():
    def show():
        return "show function"
    print("disp function")
    return show

return_show= disp()
print(return_show() )