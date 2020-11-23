# https://ru.qaz.wiki/wiki/Data-driven_programming
from src.core.scene import Scene

if __name__ == '__main__':
    scene: Scene = Scene()
    scene.new_world()
    scene.run()
