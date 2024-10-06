from scripts.scene import Scene


class SceneManager:
    def __init__(self, initial_scene: Scene):
        self.current_scene = initial_scene
        
    def update(self):
        self.renderables = self.current_scene.get_renderables()
        
    def next_scene(self):
        self.current_scene = self.current_scene.next
        
    def prev_scene(self): 
        self.current_scene = self.current_scene.prev
        
    def get_surface(self):
        return self.current_scene.get_renderables()