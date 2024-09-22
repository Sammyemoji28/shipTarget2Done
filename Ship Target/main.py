
import pgzrun
import random
import itertools

HEIGHT = 400
WIDTH = 400

BLOCKPOS = [(350,50),(350,350),(50,350),(50,50)]
blockPosition = itertools.cycle(BLOCKPOS)

ship = Actor("ship", center = (200,200))
block = Actor("block", center = (50,50))

def draw():
    screen.clear()
    ship.draw()
    block.draw()

def moveBlock():
    animate(block,"bounce_end", duration = 1, pos = next(blockPosition))

def shipTarget():
    randomX = random.randint(100,300)
    randomY = random.randint(100,300)
    ship.target = randomX, randomY
    targetAngle = ship.angle_to(ship.target)
    targetAngle += 360 * ((ship.angle - targetAngle + 180)// 360)
    animate(ship, angle = targetAngle, duration = 0.3, on_finished = moveShip)

def moveShip():
    animate(ship, tween = 'accel_decel', pos = ship.target, duration = ship.distance_to(ship.target)/200, on_finished = shipTarget)

def update():
    pass

clock.schedule_interval(moveBlock,2)
shipTarget()
pgzrun.go()