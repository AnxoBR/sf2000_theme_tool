import tkinter as tk
from functools import partial

from menu_image_generator.menu_image_generator import MenuImageGenerator
from zfb_generator.zfb_generator import ZFBGenerator


class SF2000ThemeTool(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.title('SF2000 Theme Tool')
        self.iconphoto(False, tk.PhotoImage(file='assets/images/sf2000-theme-tool-frog.png'))
        self.geometry('800x600')

        self.menu = SideMenu(self)
        self.menu.grid(row=0, column=0, sticky='nswe', padx=0, pady=0)

        self.tool = Home(self)
        self.tool.config(bd=2, relief='solid')
        self.tool.grid(row=0, column=1, sticky="nswe", padx=3, pady=0)

        self.grid_columnconfigure(0, weight=1, minsize=200)
        self.grid_columnconfigure(1, weight=3, minsize=600)
        self.grid_rowconfigure(0, weight=1, minsize=600) 

    def change_frame(self, tool: tk.Frame):
        self.tool.destroy()
        self.tool = tool
        self.tool.config(bd=2, relief='solid')
        self.tool.grid(row=0, column=1, sticky="nswe", padx=3, pady=0)

    def detect_menu_sections(self):
        pass


class SideMenu(tk.Frame):

    def __init__(self, root):
        super().__init__(master=root)
        self.menu_buttons = {
                            'home': 'Home',
                            'game_list_updater': 'Game List Updater',
                            'game_cover_generator': 'Game Cover Generator',
                            'menu_image_generator': 'Menu Image Generator',
                            'theme_image_generator': 'Theme Image Generator',
                            'zfb_generator': 'ZFB Generator'
                        }
        
        button_position = 0
        for tool, title in self.menu_buttons.items():
            button = tk.Button(self, text=title, command=partial(self.change_tool, tool))
            button.grid(row=button_position, column=0, sticky='ew')
            button_position += 1

    def change_tool(self, tool):
        match tool:
            case 'game_list_updater':
                self.master.change_frame(MenuImageGenerator(self.master))
            case 'game_cover_generator':
                self.master.change_frame(MenuImageGenerator(self.master))
            case 'menu_image_generator':
                self.master.change_frame(MenuImageGenerator(self.master))
            case 'theme_image_generator':
                self.master.change_frame(MenuImageGenerator(self.master))
            case 'zfb_generator':
                self.master.change_frame(ZFBGenerator(self.master))
            case _:
                self.master.change_frame(Home(self.master))


class Home(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.label = tk.Label(self, text="Bienvenido a la aplicación")
        self.label.pack(pady=20)


if __name__ == '__main__':
    app = SF2000ThemeTool()
    app.mainloop()
