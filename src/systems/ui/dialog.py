import os
import subprocess

from src.core.scene import Scene
from src.systems.base import System


class SystemDialog(System):

    def process(self, scene: Scene):
        pass

    def clear(self) -> None:
        if os.name == 'posix':
            subprocess.call("clear", shell=True)
            subprocess.call("clear", shell=True)
        elif os.name in ('ce', 'nt', 'dos'):
            subprocess.call("cls", shell=True)


class SystemDialogYN(SystemDialog):
    pass


if __name__ == '__main__':
    system: SystemDialog = SystemDialog()
    print("hello")
    system.clear()
