# Brick-Breaker
Built an arcade game in Python3(terminal-based), inspired from the old classic brick breaker game.Game is majorly based on OOPS concept (some properties of OOPS implemented are : Inheritance,Polymorphism, Encapsulation , Abstraction )

## Running
Run game using
` python3 main.py`

## Instructions

1. `AD` or `ad` to move.
2. To release the ball `Space`.
3. `Q` or `q` to quit.
4. You get 3 lives in the game.
5. Increase your score by hitting the bricks.
6. Activate the powerups by grabbing them using paddle.

## Bricks

1. 5 types of bricks ( 3 normal , 1 unbreakable and 1 explosive ).
2. All 3 normal bricks have different strengths.
3. Strength will decrease by 1 as ball collides with the brick.
4. Brick will be disabled once it's strength gets 0.
5. Increase your score by hitting the bricks.

## Powerups

5 types of powerups described as follows.

1. Expand paddle: Increases the size of the paddle by a certain amount.
2. Shrink Paddle: Reduce the size of the paddle by a certain amount but not completely.
3. Fast Ball: Increases the speed of the ball.
4. Thru-ball: This enables the ball to destroy and go through any brick it touches, irrespective of the
strength of the wall.(Even the unbreakable ones which you couldn’t previously destroy)
5. Paddle Grab:Allows the paddle to grab the ball on contact and relaunch the ball at will. The ball will
follow the same expected trajectory after release, similar to the movement expected without the grab.

## Assignment related stuff

1. **Polymorphism** - both powerup class and its childs have the `position` but it behaves differently in both of them, it displays different symbol.
2. **Inheritance** - both brick1 and brick2 are inherited from same parent class `brick`
3. **Encapsulation** - all variables are protected and they have getters and setters.
4. **Abstraction** - functions like `activating_powerup` and `coll_explosive` hide underlying implementation and can be used in whatever way since it always works the way you want it to.


