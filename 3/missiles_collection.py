from units import Missile
_missiles = []
_canvas = None

<<<<<<< HEAD:3/missile_collection.py

def initialize(canvas):
    global _canvas
    _canvas = canvas


=======
def initialize(canv):
    global _canvas
    _canvas = canv
>>>>>>> e79046c30af05a14ed18907d82aea26cd8fcea87:3/missiles_collection.py
def fire(owner):
    m = Missile(_canvas, owner)
    _missiles.append(m)


def update():
    start = len(_missiles)-1
    for i in range(start, -1, -1):
        if _missiles[i].is_destroyed():
            del _missiles[i]
        else:
            _missiles[i].update()
<<<<<<< HEAD:3/missile_collection.py


=======
>>>>>>> e79046c30af05a14ed18907d82aea26cd8fcea87:3/missiles_collection.py
def check_missiles_collision(tank):
    for missile in _missiles:
        if missile.get_owner() == tank:
            continue
<<<<<<< HEAD:3/missile_collection.py
        if missile.intersect(tank):
=======
        if tank.intersects(tank):
>>>>>>> e79046c30af05a14ed18907d82aea26cd8fcea87:3/missiles_collection.py
            missile.destroy()
            tank.damage(25)
            return
