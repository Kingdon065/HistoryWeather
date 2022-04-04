#! python3
# _*_ coding: utf-8 _*_

# 说明: 终端显示着色
# 函数名称说明:
#   xxx_: 后缀_表示为成员变量string着色
#   light_xxx: 表示为成员变量string着色
#   light: 表示浅色, 无代表正常色调
#   b: 前缀b代表背景色, 无前缀b, 即为前景色

from colorama import init, Fore, Back

init(autoreset=False)


class Colored:
    def __init__(self, s=''):
        self.string = s

    # ---------------前景色----------------
    #  前景色:红色  背景色:默认
    def red_(self):
        return self.red(self.string)

    def red(self, s):
        return Fore.RED + s + Fore.RESET

    #  前景色:浅红色  背景色:默认
    def light_red(self):
        return self.lightred(self.string)

    def lightred(self, s):
        return Fore.LIGHTRED_EX + s + Fore.RESET

    #  前景色:绿色  背景色:默认
    def green_(self):
        return self.green(self.string)

    def green(self, s):
        return Fore.GREEN + s + Fore.RESET

    #  前景色:浅绿色  背景色:默认
    def light_green(self):
        return self.lightgreen(self.string)

    def lightgreen(self, s):
        return Fore.LIGHTGREEN_EX + s + Fore.RESET

    #  前景色:黄色  背景色:默认
    def yellow_(self):
        return self.yellow(self.string)

    def yellow(self, s):
        return Fore.YELLOW + s + Fore.RESET

    #  前景色:浅黄色  背景色:默认
    def light_yellow(self):
        return self.lightyellow(self.string)

    def lightyellow(self, s):
        return Fore.LIGHTYELLOW_EX + s + Fore.RESET

    #  前景色:白色  背景色:默认
    def white_(self):
        return self.white(self.string)

    def white(self, s):
        return Fore.WHITE + s + Fore.RESET

    #  前景色:浅白色  背景色:默认
    def light_white(self):
        return self.lightwhite(self.string)

    def lightwhite(self, s):
        return Fore.LIGHTWHITE_EX + s + Fore.RESET

    #  前景色:蓝色  背景色:默认
    def blue_(self):
        return self.blue(self.string)

    def blue(self, s):
        return Fore.BLUE + s + Fore.RESET

    #  前景色:浅蓝色  背景色:默认
    def light_blue(self):
        return self.lightblue(self.string)

    def lightblue(self,s):
        return Fore.LIGHTBLUE_EX + s + Fore.RESET

    #  前景色:青色  背景色:默认
    def cyan_(self):
        return self.cyan(self.string)

    def cyan(self, s):
        return Fore.CYAN + s + Fore.RESET

    #  前景色:浅青色  背景色:默认
    def light_cyan(self):
        return self.lightcyan(self.string)

    def lightcyan(self, s):
        return Fore.LIGHTCYAN_EX + s + Fore.RESET

    #  前景色:洋红色  背景色:默认
    def magenta_(self):
        return self.magenta(self.string)

    def magenta(self, s):
        return Fore.MAGENTA + s + Fore.RESET

    #  前景色:浅洋红色  背景色:默认
    def light_magenta(self):
        return self.lightmagenta(self.string)

    def lightmagenta(self, s):
        return Fore.LIGHTMAGENTA_EX + s + Fore.RESET

    #  前景色:黑色  背景色:默认
    def black_(self):
        return self.black(self.string)

    def black(self, s):
        return Fore.BLACK + s + Fore.RESET

    #  前景色:浅黑色  背景色:默认
    def light_black(self):
        return self.lightblack(self.string)

    def lightblack(self, s):
        return Fore.LIGHTBLACK_EX + s + Fore.RESET

    # ---------------背景色----------------
    #  背景色:红色  前景色:默认
    def b_red_(self):
        return self.b_red(self.string)

    def b_red(self, s):
        return Back.RED + s + Back.RESET

    #  背景色:浅红色  前景色:默认
    def b_light_red(self):
        return self.b_lightred(self.string)

    def b_lightred(self, s):
        return Back.LIGHTRED_EX + s + Back.RESET

    #  背景色:绿色  前景色:默认
    def b_green_(self):
        return self.b_green(self.string)

    def b_green(self, s):
        return Back.GREEN + s + Back.RESET

    #  背景色:浅绿色  前景色:默认
    def b_light_green(self):
        return self.b_lightgreen(self.string)

    def b_lightgreen(self, s):
        return Back.LIGHTGREEN_EX + s + Back.RESET

    #  背景色:黄色  前景色:默认
    def b_yellow_(self):
        return self.b_yellow(self.string)

    def b_yellow(self, s):
        return Back.YELLOW + s + Back.RESET

    #  背景色:浅黄色  前景色:默认
    def b_light_yellow(self):
        return self.b_lightyellow(self.string)

    def b_lightyellow(self, s):
        return Back.LIGHTYELLOW_EX + s + Back.RESET

    #  背景色:白色  前景色:默认
    def b_white_(self):
        return self.b_white(self.string)

    def b_white(self, s):
        return Back.WHITE + s + Back.RESET

    #  背景色:浅白色  前景色:默认
    def b_light_white(self):
        return self.b_lightwhite(self.string)

    def b_lightwhite(self, s):
        return Back.LIGHTWHITE_EX + s + Back.RESET

    #  背景色:蓝色  前景色:默认
    def b_blue_(self):
        return self.b_blue(self.string)

    def b_blue(self, s):
        return Back.BLUE + s + Back.RESET

    #  背景色:浅蓝色  前景色:默认
    def b_light_blue(self):
        return self.b_lightblue(self.string)

    def b_lightblue(self, s):
        return Back.LIGHTBLUE_EX + s + Back.RESET

    #  背景色:青色  前景色:默认
    def b_cyan_(self):
        return self.b_cyan(self.string)

    def b_cyan(self, s):
        return Back.CYAN + s + Back.RESET

    #  背景色:浅青色  前景色:默认
    def b_light_cyan(self):
        return self.b_lightcyan(self.string)

    def b_lightcyan(self, s):
        return Back.LIGHTCYAN_EX + s + Back.RESET

    #  背景色:洋红色  前景色:默认
    def b_magenta_(self):
        return self.b_magenta(self.string)

    def b_magenta(self, s):
        return Back.MAGENTA + s + Back.RESET

    #  背景色:浅洋红色  前景色:默认
    def b_light_magenta(self):
        return self.b_lightmagenta(self.string)

    def b_lightmagenta(self, s):
        return Back.LIGHTMAGENTA_EX + s + Back.RESET

    #  背景色:黑色  前景色:默认
    def b_black_(self):
        return self.b_black(self.string)

    def b_black(self, s):
        return Back.BLACK + s + Back.RESET

    #  背景色:浅黑色  前景色:默认
    def b_light_black(self):
        return self.b_lightblack(self.string)

    def b_lightblack(self, s):
        return Back.LIGHTBLACK_EX + s + Back.RESET
