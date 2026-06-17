import random


class TwistManager:
    """
    Single source of truth untuk state game.
    Twist berjalan looping selamanya — setiap kali satu twist selesai,
    twist baru (full random, boleh berulang) dan trigger point baru
    (random) langsung disiapkan.
    """

    AVAILABLE_TWISTS = [
        "Lavaloon",
        "Self Aware Calculator",
        "Broken Calculator",
        "Teleporting Button",
        "Bloodmoon",
        "Capslock Demon",
        "Black Hole",
    ]

    OBJECTIVES = {
        "Lavaloon": (
            "Hold the button until the progress bar is full.\n"
            "Don't let it touch you!"
        ),
        "Self Aware Calculator": "Solve the multiplication problem.",
        "Broken Calculator": "Solve the division problem.",
        "Teleporting Button": "Click the button.",
        "Bloodmoon": "Survive the Bloodmoon.",
        "Capslock Demon": "Type the sentence correctly.",
        "Black Hole": (
            "Reach the finish line before the singularity consumes everything.\n"
            "Your cursor is your joystick."
        ),
    }

    # Range jarak antar trigger (dalam jumlah karakter tambahan dari trigger sebelumnya)
    TRIGGER_GAP_MIN = 85
    TRIGGER_GAP_MAX = 250

    def __init__(self):
        self.completed_twists: int = 0

        self._current_twist: str = random.choice(self.AVAILABLE_TWISTS)
        self._next_trigger_point: int = self._roll_trigger_point(base=0)

        print(f"[TwistManager] Twist pertama: {self._current_twist}")
        print(f"[TwistManager] Trigger point: {self._next_trigger_point}")

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _roll_trigger_point(self, base: int) -> int:
        gap = random.randint(self.TRIGGER_GAP_MIN, self.TRIGGER_GAP_MAX)
        return base + gap

    # ------------------------------------------------------------------
    # Query helpers
    # ------------------------------------------------------------------

    def get_current_twist(self) -> str:
        return self._current_twist

    def get_current_objective(self) -> str:
        return self.OBJECTIVES.get(self._current_twist, "")

    def should_trigger_twist(self, character_count: int) -> bool:
        return character_count >= self._next_trigger_point

    # ------------------------------------------------------------------
    # State mutation
    # ------------------------------------------------------------------

    def complete_current_twist(self, character_count: int = 0) -> None:
        """
        Dipanggil saat twist selesai. Menambah counter, lalu langsung
        menyiapkan twist & trigger point berikutnya (looping).
        """
        self.completed_twists += 1

        self._current_twist = random.choice(self.AVAILABLE_TWISTS)
        self._next_trigger_point = self._roll_trigger_point(base=character_count)

        print(f"[TwistManager] Twist selesai. Total selesai: {self.completed_twists}")
        print(f"[TwistManager] Twist berikutnya: {self._current_twist}")
        print(f"[TwistManager] Trigger point berikutnya: {self._next_trigger_point}")