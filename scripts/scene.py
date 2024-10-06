from scripts.dialogue import Dialogue


class Scene:
    def __init__(self, dialogue: Dialogue, background=None, next=None, prev=None):
        self.dialogue = dialogue
        self.background = background
        self.next = next
        self.prev = prev
        
    def get_renderables(self):
        return self.dialogue.getSurface()