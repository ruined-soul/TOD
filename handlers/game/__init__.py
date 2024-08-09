from .solo import solo_mode
from .multiplayer import multiplayer_mode
from .truth import ask_truth_question
from .dare import ask_dare_question
from .penalty import apply_penalty

__all__ = [
    "solo_mode", "multiplayer_mode", "ask_truth_question", 
    "ask_dare_question", "apply_penalty"
]
