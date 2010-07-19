__all__ = ["trimet", "route", "dir", "stop", "arrival", "detour"]

class trimet:
  "trimet root object class"

  def __init__(self):
     self.allowed = [ "route", "dir", "stop", "arrival", "detour"]
     self.children = []

  def __str__(self):
    buf = ""
    for c in self.children:
            buf += str(c) + " "
    return  buf

  def add_child(self,obj):
      if not (obj.__class__.__name__ in self.allowed):
        print obj.__class__.__name__ + " not in " + self.allowed
        return False

      self.children.append(obj)
      return True

  def get_children(self):
    return self.children

  def remove_child(self,obj):
    return self.children.remove(obj)
