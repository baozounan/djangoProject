import os



def open_FG_Root(path):
    """根据path打开FGbin目录"""
    os.chdir(path)

def start_FG(commend,path):
    """向FG传送指令"""
    open_FG_Root(path)
    os.system(commend)











