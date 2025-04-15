def check_collision(object1, object2):
    """
    Check if two game objects have collided.

    Args:
        object1: First game object (with get_hitbox method or hitbox dictionary)
        object2: Second game object (with get_hitbox method or hitbox dictionary)

    Returns:
        bool: True if objects collide, False otherwise
    """
    # Get hitboxes
    box1 = object1.get_hitbox() if hasattr(object1, 'get_hitbox') else object1
    box2 = object2.get_hitbox() if hasattr(object2, 'get_hitbox') else object2

    # Check collision (AABB collision algorithm)
    if (box1["x1"] < box2["x2"] and
        box1["x2"] > box2["x1"] and
        box1["y1"] < box2["y2"] and
        box1["y2"] > box2["y1"]):
        return True

    return False