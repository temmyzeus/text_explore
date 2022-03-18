def _clip_scores(score: float, max_: float, min_: float) -> float:
    """
    Clip scores within range.

    Arguments:
    ---------
    score: float
        Score to ensure it's within range
    max_: float
        Maximum value possible
    min_: float
        Minimum value possible

    Returns:
    --------
    clipped_score: float
    """
    if score > max_:
        return float(max_)
    elif score < min_:
        return float(min_)
    else:
        return float(score)
