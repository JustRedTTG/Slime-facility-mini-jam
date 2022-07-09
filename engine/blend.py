import engine.data as data

def blend(c1, c2, reverse=False, color_blending=None):
    if not color_blending: color_blending = data.color_blending
    dif_R = c2[0] - c1[0]
    dif_G = c2[1] - c1[1]
    dif_B = c2[2] - c1[2]
    if reverse:
        return (
            c1[0] + dif_R * (1-color_blending),
            c1[1] + dif_G * (1-color_blending),
            c1[2] + dif_B * (1-color_blending)
        )
    return (
        c1[0] + dif_R * color_blending,
        c1[1] + dif_G * color_blending,
        c1[2] + dif_B * color_blending
    )