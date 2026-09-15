def asteroid_collision(asteroids):
    # O(n) time, O(n) space
    # Stack of survivors. A left-mover destroys smaller right-movers on top; it dies if it
    # meets a bigger one, and both vanish on a tie. Same-direction pairs never interact.
    stack = []
    for a in asteroids:
        alive = True
        while alive and a < 0 and stack and stack[-1] > 0:
            if stack[-1] < -a:
                stack.pop()
                continue
            if stack[-1] == -a:
                stack.pop()
            alive = False
        if alive:
            stack.append(a)
    return stack
