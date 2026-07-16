import ttkbootstrap as tb

#window
root = tb.Window(themename="darkly")
root.title("sowon (python)")
root.state('zoomed')
root.update()

root.configure(background="black")
style = tb.Style()
style.configure("Black.TFrame", background="black")