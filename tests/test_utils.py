import pytest

from text_explore.utils import _clip_scores

def test_clip_cores():
    assert _clip_scores(203, max_=100, min_=0) == 100
    assert _clip_scores(-4, max_=100, min_=0) == 0
    assert _clip_scores(50, max_=45, min_=1) == 45
    assert _clip_scores(4, max_=34, min_=7) == 7

    with pytest.raises(TypeError):
        assert _clip_scores("Gary", max_=34, min_=7) == 7
        assert _clip_scores(4, max_="max", min_=7) == 7
        assert _clip_scores(50, max_=34, min_="min") == 7
