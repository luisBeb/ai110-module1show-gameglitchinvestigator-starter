from logic_utils import check_guess, update_score, get_range_for_difficulty, parse_guess

def test_check_guess_too_high():
    outcome, message = check_guess(85, 73)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_check_guess_too_low():
    outcome, message = check_guess(30, 73)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_check_guess_correct():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_update_score_win():
    score = update_score(0, "Win", 1)
    assert score > 0

def test_update_score_wrong_guess_never_gains_points():
    score = update_score(0, "Too High", 2)
    assert score < 0