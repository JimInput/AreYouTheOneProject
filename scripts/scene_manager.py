from scripts.scene import Scene


class SceneManager:
    def __init__(self, initial_scene: Scene):
        self.current_scene = initial_scene
        
    def next_scene(self):
        self.current_scene = self.current_scene.next
        self.current_scene.update_renderables()
        
    def prev_scene(self): 
        self.current_scene = self.current_scene.prev
        
    def update_scene(self):
        self.current_scene.update_renderables()
        
    def next_text(self):
        # if self.current_scene.text_segment_done():
        #     self.next_scene()
        # else:
        self.current_scene.next_text()
        
    def get_surface(self):
        return self.current_scene.get_surface()