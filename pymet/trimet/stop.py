class stop():
    "trimet stop object class"

    def __init__(self, desc="", locid=0, lat=0, lng=0, seq=0, tp=""):
        self.desc = desc
        self.locid = 0
        self.lat = 0
        self.lng = 0
        self.seq = 0
        self.tp = 0
        self.allowed = []

    def __str__(self):
        return self.desc
