def main():
    from distutils.core import setup
    import py2exe
    #setup(windows = ['QuickLibDemo.pyw'])
    setup(windows=[{"script":"QuickLibGuiDemo.pyw", "icon_resources": [(1, "main.ico")]} ],options = { "py2exe":{"dll_excludes":["MSVCP90.dll"]}})
    #setup(console = ['QuickLibSimple.py'])
    #setup(
    #windows = [{"script":"QuickLibDemo.pyw", "icon_resources": [(1, "main.ico")]} ]
    #) 
    pass


 

if __name__ == '__main__':
    main()
