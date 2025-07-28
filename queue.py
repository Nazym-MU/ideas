import datetime
class Idea:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.status = 'brainstorming'

    def __str__(self):
        return f"[{self.status}] {self.title}"

class Queue:
    def __init__(self):
        self.ideas = []

    def add_idea(self, title, description=''):
        idea = Idea(title, description)
        self.ideas.append(idea)
        return idea

    def change_status(self, idea_index, new_status):
        if 0 <= idea_index < len(self.ideas):
            if new_status == "done!":
                response = input("Say yes if this is the idea you're loooking for. U sure you're done?", self.ideas[idea_index])
                if response.lower() == 'yes':
                    self.ideas.pop(idea_index)
            else:
                self.ideas[idea_index].status = new_status
    def list_ideas(self):
        for idx, idea in enumerate(self.ideas):
            print(str(idx) + "\n\033[0;36m" + idea.title + "\n\033[0m" + idea.description)
            print("-------------------------------------------------")

    def find_idea(self, title):
        for i, idea in enumerate(self.ideas):
            if title.lower() in idea.title.lower():
                return i
        return -1
        

if name == "main":
    queue = Queue()
    
    # did i just forget about all the ideas i was about to add when i was coding this... nahhh
    # it's okay
    
    queue.add_idea("Karpathy lectures", "take notes and code in jupyter notebook, push to github")
    queue.add_idea("nazym.space website art", "draw different popup illustrations for my website and find a way to add them to the screen, turn off copilot")
    queue.add_idea("neetcode pro", "finish neetcode.io courses, take notes, and upload to nazym-dev.vercel.app")
    queue.add_idea("graphs", "read the textbook about graphs and take notes")
    queue.add_idea("nazym-dev", "fix the issues with searching and sorting algorithms, trees, etc., start over")
    queue.add_idea("add this queue to nazym.space", "this should appear when you click on the rubik's cube")
    queue.add_idea("blender animations", "create and publish blender animations and figma/procreate descriptions for cities i lived in like i did for astana 2 years ago")
    queue.add_idea("art portfolio", "create a proper 3D-modeling focused art portfolio website")
    queue.add_idea("ios app", "convert my discipline web app to an ios app, back to swift!!")
    queue.add_idea("medium", "write articles about karpathy lectures, quantum physics")
    queue.add_idea("read papers", "read machine learning, ai, physics papers, and write about them, bro you used to be good at that, let's get back to it")
    queue.add_idea("money", "start investing in sth, i know nothing about this, learn")
    queue.add_idea("write a book for children", "illustrations and explanations about quantum physics, physics, AI, machine learning, etc.")
    
    
    print("Current ideas:")
    queue.list_ideas()
