x = 0
y = 0

pomjeranja = "RRLURRRDRLLUD"

for i in range(len(pomjeranja)):
    if pomjeranja[i] == "R":
        x += 1
    elif pomjeranja[i] == "L":
        x -= 1
    elif pomjeranja[i] == "U":
        y += 1
    elif pomjeranja[i] == "D":
        y -= 1

print(f"Koordinate robota nakon pomjeranja: ({x}, {y})")
