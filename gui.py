from Tkinter import *


class Main:
    def __init__(self, master):
        master.minsize(width=300, height=80)
        self.master = master
        menubar = Menu(master)
        menubar.add_command(label="Quit!", command=root.quit)

        master.config(menu=menubar, height=5)

        frame = Frame(master)
        frame.pack()
        self.label = Label(frame, text="Make own Solar System!")
        self.label.pack()

        self.default = Button(frame, text="Default Solar System", command=self.prep_to_draw, width="50", pady="5")
        self.default.pack()

        self.create = Button(frame, text="Create~", command="self.setting", width="50", pady="5")
        self.create.pack()

    def prep_to_draw(self):
        self.label.destroy()
        self.default.destroy()
        self.create.destroy()
        DrawWin(self.master)


class DrawWin:
    def __init__(self, master):
        master.minsize(width=800, height=600)
        import astro_objects
        self.star_system = astro_objects.Star_system()

        left = Frame(master)
        left.pack(side=LEFT)
        left.config()
        self.w = Canvas(master, width=600, height=500, bg="black")
        self.w.pack()
        start = Button(left, text="Start", command=self.start, width="20", pady="5")
        start.grid(row=0, column=0)
        stop = Button(left, text="Stop", command=self.stop, width="20", pady="5")
        stop.grid(row=1, column=0)

        self.draw()

    def draw(self):
        # sun
        # temp center
        lx = 300
        ly = 250
        rx = 300
        ry = 250
        # /temp
        temp = lambda x: x + 20
        cords = [lx, ly, rx, ry]
        l = map(temp, cords)
        print l

        self.w.create_oval(lx - 4, ly - 4, rx + 4, ry + 4, fill=self.star_system.star.color)

        for i in range(1, self.star_system.size() + 1):
            self.w.create_oval(lx, ly, rx, ry, fill="white")

    def start(self):
        pass

    def stop(self):
        pass


if __name__ == "__main__":
    root = Tk()

    main = Main(root)

    root.mainloop()
    root.destroy()

# obiekt canvas ma move to animacji!
