# not working yet
# def asteroidCollision(asteroids):
#     stack = []  # stack
#     for i in range(len(asteroids)):
#         if len(stack) == 0:
#             stack.append(asteroids[i])
#             continue
#         x = stack[-1]
#         y = asteroids[i]
#         if x * y > 0:  # same sign
#             stack.append(asteroids[i])
#         else:  # opposite sign
#             tot = x + y
#             if tot == 0:
#                 stack.pop()
#                 continue
#             elif tot > 0:
#                 if x < y:
#                     stack.pop()
#                     stack.append(y)
#             else:  # tot < 0
#                 if x > y:
#                     stack.pop()
#                     stack.append(y)
#     return stack


def asteroidCollision(asteroids):
    stack = []  # stack
    for asteroid in asteroids:
        while stack and asteroid < 0 and stack[-1] > 0:
            diff = stack[-1] + asteroid
            if diff < 0:
                stack.pop()
            elif diff > 0:
                asteroid = 0
            else:
                stack.pop()
                asteroid = 0
        if asteroid:
            stack.append(asteroid)

    return stack


asteroids = [5, 10, -5]
print(asteroidCollision(asteroids))  # [5,10]
asteroids = [8, -8]
print(asteroidCollision(asteroids))  # []
asteroids = [10, 2, -5]
print(asteroidCollision(asteroids))  # [10]
