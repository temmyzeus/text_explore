from typing import Union


def _clip_scores(score: Union[float, int], max_: Union[float, int], min_: Union[float, int]) -> float:
    """
    Clip scores within range.

    Arguments:
    ---------
    score: float | int
        Score to ensure it's within range
    max_: float | int
        Maximum value possible
    min_: float | int
        Minimum value possible

    Returns:
    --------
    clipped_score: float
    """
    def type_guard(value: Union[float, int], name: str):
        if not isinstance(value, (float, int)):
            raise TypeError(f"{name} must be a float or an integer, not a {type(value)}")
    
    type_guard(score, "Score")
    type_guard(max_, "Maximum")
    type_guard(min_, "Minimum")

    if score > max_:
        return float(max_)
    elif score < min_:
        return float(min_)
    else:
        return float(score)
