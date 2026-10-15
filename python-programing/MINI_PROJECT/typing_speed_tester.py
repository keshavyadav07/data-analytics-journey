"""A polished desktop typing-speed test built with Python's Tkinter."""

import random
import time
import tkinter as tk
from dataclasses import dataclass
from tkinter import ttk
from typing import Optional


PASSAGES = (
    "Great things are done by a series of small things brought together. "
    "Take your time, stay focused, and let steady practice build your confidence.",
    "Technology is most useful when it helps people solve real problems. "
    "Clear thinking and careful work can turn a simple idea into something valuable.",
    "Learning a new skill takes patience. Make a little progress each day, "
    "notice what works, and keep going even when the next step feels difficult.",
    "A thoughtful plan makes complex work easier to manage. Set a clear goal, "
    "pay attention to the details, and review your progress along the way.",
    "Good communication begins with listening. When we share ideas clearly "
    "and treat questions with curiosity, better solutions are possible.",
    "A calm mind can focus on the task in front of it. Breathe, find a steady "
    "rhythm, and give each word your attention as you type.",
)

TEST_DURATIONS = (30, 60, 120)

BACKGROUND = "#0b1120"
SURFACE = "#131d30"
SURFACE_LIGHT = "#1b2940"
TEXT = "#e5edf8"
MUTED = "#91a2ba"
ACCENT = "#62d6ad"
ERROR = "#ff7b86"


@dataclass(frozen=True)
class TypingStats:
    gross_wpm: float
    net_wpm: float
    accuracy: float
    correct_characters: int
    total_characters: int
    errors: int


def calculate_stats(typed_text: str, passage: str, elapsed_seconds: float) -> TypingStats:
    """Calculate standard five-characters-per-word typing statistics."""
    correct = sum(
        typed_character == passage[index]
        for index, typed_character in enumerate(typed_text[: len(passage)])
    )
    total = len(typed_text)
    errors = total - correct
    accuracy = (correct / total * 100) if total else 0.0
    elapsed_minutes = max(elapsed_seconds, 1.0) / 60
    gross_wpm = total / 5 / elapsed_minutes
    net_wpm = correct / 5 / elapsed_minutes

    return TypingStats(
        gross_wpm=gross_wpm,
        net_wpm=net_wpm,
        accuracy=accuracy,
        correct_characters=correct,
        total_characters=total,
        errors=errors,
    )


class TypingSpeedTester:
    """Manage the typing test window, timer, feedback, and results."""

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Typing Speed Tester")
        self.root.geometry("900x760")
        self.root.minsize(760, 680)
        self.root.configure(bg=BACKGROUND)

        self.duration = tk.StringVar(value="60")
        self.timer_text = tk.StringVar(value="60s")
        self.status_text = tk.StringVar(value="Choose a duration, then start typing.")
        self.prompt = ""
        self.start_time: Optional[float] = None
        self.timer_job: Optional[str] = None
        self.finished = False

        self._configure_styles()
        self._build_interface()
        self.new_test()
        self.root.bind("<Control-r>", self._restart_shortcut)

    def _configure_styles(self) -> None:
        style = ttk.Style(self.root)
        style.theme_use("clam")
        style.configure(
            "Test.Horizontal.TProgressbar",
            troughcolor=SURFACE_LIGHT,
            background=ACCENT,
            bordercolor=SURFACE_LIGHT,
            lightcolor=ACCENT,
            darkcolor=ACCENT,
        )

    def _build_interface(self) -> None:
        container = tk.Frame(self.root, bg=BACKGROUND)
        container.pack(fill="both", expand=True, padx=36, pady=30)

        header = tk.Frame(container, bg=BACKGROUND)
        header.pack(fill="x", pady=(0, 24))
        tk.Label(
            header,
            text="Typing Speed Tester",
            font=("Segoe UI", 27, "bold"),
            bg=BACKGROUND,
            fg=TEXT,
        ).pack(anchor="w")
        tk.Label(
            header,
            text="Build your rhythm. Measure your accuracy. Improve with every round.",
            font=("Segoe UI", 11),
            bg=BACKGROUND,
            fg=MUTED,
        ).pack(anchor="w", pady=(5, 0))

        self._build_stat_cards(container)
        self._build_controls(container)
        self._build_passage(container)
        self._build_typing_area(container)

        footer = tk.Frame(container, bg=BACKGROUND)
        footer.pack(fill="x", pady=(14, 0))
        tk.Label(
            footer,
            textvariable=self.status_text,
            font=("Segoe UI", 10),
            bg=BACKGROUND,
            fg=MUTED,
        ).pack(side="left")
        tk.Label(
            footer,
            text="Ctrl+R  Restart",
            font=("Segoe UI", 9),
            bg=BACKGROUND,
            fg=MUTED,
        ).pack(side="right")

    def _build_stat_cards(self, parent: tk.Widget) -> None:
        cards = tk.Frame(parent, bg=BACKGROUND)
        cards.pack(fill="x", pady=(0, 22))

        self.stat_values = {}
        stat_definitions = (
            ("NET WPM", "0", ACCENT),
            ("ACCURACY", "0%", TEXT),
            ("TIME LEFT", self.timer_text, TEXT),
            ("CHARACTERS", "0 / 0", TEXT),
        )
        for column, (title, initial_value, color) in enumerate(stat_definitions):
            card = tk.Frame(cards, bg=SURFACE, padx=15, pady=13)
            card.grid(
                row=0,
                column=column,
                sticky="nsew",
                padx=(0 if column == 0 else 9, 0),
            )
            cards.columnconfigure(column, weight=1, uniform="stat-cards")
            tk.Label(
                card,
                text=title,
                font=("Segoe UI", 9, "bold"),
                bg=SURFACE,
                fg=MUTED,
            ).pack(anchor="w")

            value = (
                initial_value
                if isinstance(initial_value, tk.Variable)
                else tk.StringVar(value=initial_value)
            )
            tk.Label(
                card,
                textvariable=value,
                font=("Segoe UI", 21, "bold"),
                bg=SURFACE,
                fg=color,
            ).pack(anchor="w", pady=(5, 0))
            self.stat_values[title] = value

    def _build_controls(self, parent: tk.Widget) -> None:
        controls = tk.Frame(parent, bg=BACKGROUND)
        controls.pack(fill="x", pady=(0, 10))

        tk.Label(
            controls,
            text="TEST LENGTH",
            font=("Segoe UI", 9, "bold"),
            bg=BACKGROUND,
            fg=MUTED,
        ).pack(side="left", padx=(0, 10))

        self.duration_picker = ttk.Combobox(
            controls,
            textvariable=self.duration,
            values=[str(seconds) for seconds in TEST_DURATIONS],
            state="readonly",
            width=7,
            font=("Segoe UI", 10),
        )
        self.duration_picker.pack(side="left")
        self.duration_picker.bind(
            "<<ComboboxSelected>>", lambda _event: self.new_test()
        )

        self.restart_button = tk.Button(
            controls,
            text="New test",
            command=self.new_test,
            font=("Segoe UI", 10, "bold"),
            bg=ACCENT,
            fg=BACKGROUND,
            activebackground="#7ce8c0",
            activeforeground=BACKGROUND,
            relief="flat",
            padx=18,
            pady=8,
            cursor="hand2",
        )
        self.restart_button.pack(side="right")

    def _build_passage(self, parent: tk.Widget) -> None:
        tk.Label(
            parent,
            text="TYPE THE PASSAGE",
            font=("Segoe UI", 9, "bold"),
            bg=BACKGROUND,
            fg=MUTED,
        ).pack(anchor="w", pady=(8, 8))

        self.passage_text = tk.Text(
            parent,
            height=6,
            wrap="word",
            font=("Consolas", 15),
            bg=SURFACE,
            fg=TEXT,
            insertbackground=TEXT,
            relief="flat",
            padx=18,
            pady=17,
            spacing1=4,
            spacing3=4,
            cursor="arrow",
            state="disabled",
        )
        self.passage_text.pack(fill="x")
        self.passage_text.tag_configure("correct", foreground=ACCENT)
        self.passage_text.tag_configure("incorrect", foreground=ERROR, underline=True)
        self.passage_text.tag_configure("current", background=SURFACE_LIGHT)

        self.progress = ttk.Progressbar(
            parent,
            style="Test.Horizontal.TProgressbar",
            maximum=100,
            mode="determinate",
        )
        self.progress.pack(fill="x", pady=(10, 22))

    def _build_typing_area(self, parent: tk.Widget) -> None:
        tk.Label(
            parent,
            text="YOUR TYPING",
            font=("Segoe UI", 9, "bold"),
            bg=BACKGROUND,
            fg=MUTED,
        ).pack(anchor="w", pady=(0, 8))

        self.input_text = tk.Text(
            parent,
            height=5,
            wrap="word",
            font=("Consolas", 14),
            bg=SURFACE,
            fg=TEXT,
            insertbackground=ACCENT,
            relief="flat",
            padx=18,
            pady=15,
            spacing1=3,
            spacing3=3,
            undo=True,
        )
        self.input_text.pack(fill="both", expand=True)
        self.input_text.bind("<KeyRelease>", self._on_typing)

    def new_test(self) -> None:
        self._cancel_timer()
        self.prompt = random.choice(PASSAGES)
        self.start_time = None
        self.finished = False
        seconds = int(self.duration.get())
        self.timer_text.set(f"{seconds}s")
        self.status_text.set("Choose a duration, then start typing.")
        self.stat_values["NET WPM"].set("0")
        self.stat_values["ACCURACY"].set("0%")
        self.stat_values["CHARACTERS"].set("0 / 0")
        self.progress.configure(value=0)

        self.passage_text.configure(state="normal")
        self.passage_text.delete("1.0", "end")
        self.passage_text.insert("1.0", self.prompt)
        self.passage_text.configure(state="disabled")

        self.input_text.configure(state="normal")
        self.input_text.delete("1.0", "end")
        self.input_text.focus_set()
        self._render_feedback("")

    def _on_typing(self, _event: tk.Event) -> None:
        if self.finished:
            return

        typed_text = self.input_text.get("1.0", "end-1c")
        if typed_text and self.start_time is None:
            self.start_time = time.perf_counter()
            self.status_text.set("Test in progress - keep a steady rhythm.")
            self._schedule_tick()

        self._render_feedback(typed_text)
        self._update_stats(typed_text)
        self.progress.configure(
            value=min(len(typed_text) / len(self.prompt) * 100, 100)
        )

        if len(typed_text) >= len(self.prompt):
            self._finish_test(typed_text)

    def _render_feedback(self, typed_text: str) -> None:
        self.passage_text.configure(state="normal")
        for tag in ("correct", "incorrect", "current"):
            self.passage_text.tag_remove(tag, "1.0", "end")

        for index, character in enumerate(typed_text[: len(self.prompt)]):
            tag = "correct" if character == self.prompt[index] else "incorrect"
            self.passage_text.tag_add(tag, f"1.0+{index}c", f"1.0+{index + 1}c")

        current_index = min(len(typed_text), len(self.prompt) - 1)
        if current_index >= 0:
            self.passage_text.tag_add(
                "current",
                f"1.0+{current_index}c",
                f"1.0+{current_index + 1}c",
            )
        self.passage_text.configure(state="disabled")

    def _update_stats(self, typed_text: str) -> None:
        elapsed = time.perf_counter() - self.start_time if self.start_time else 0.0
        stats = calculate_stats(typed_text, self.prompt, elapsed)
        self.stat_values["NET WPM"].set(f"{stats.net_wpm:.0f}")
        self.stat_values["ACCURACY"].set(f"{stats.accuracy:.0f}%")
        self.stat_values["CHARACTERS"].set(
            f"{stats.correct_characters} / {stats.total_characters}"
        )

    def _schedule_tick(self) -> None:
        if self.timer_job is None and not self.finished:
            self.timer_job = self.root.after(100, self._tick)

    def _tick(self) -> None:
        self.timer_job = None
        if self.finished or self.start_time is None:
            return

        elapsed = time.perf_counter() - self.start_time
        remaining = int(self.duration.get()) - elapsed
        if remaining <= 0:
            self._finish_test(self.input_text.get("1.0", "end-1c"))
            return

        self.timer_text.set(f"{int(remaining + 0.999)}s")
        self._update_stats(self.input_text.get("1.0", "end-1c"))
        self._schedule_tick()

    def _finish_test(self, typed_text: str) -> None:
        if self.finished:
            return

        self.finished = True
        self._cancel_timer()
        self._update_stats(typed_text)
        self.input_text.configure(state="disabled")
        stats = calculate_stats(
            typed_text,
            self.prompt,
            time.perf_counter() - self.start_time if self.start_time else 0.0,
        )
        self.status_text.set(
            f"Test complete - {stats.net_wpm:.0f} WPM, "
            f"{stats.accuracy:.0f}% accuracy, {stats.errors} error(s)."
        )

    def _cancel_timer(self) -> None:
        if self.timer_job is not None:
            self.root.after_cancel(self.timer_job)
            self.timer_job = None

    def _restart_shortcut(self, _event: tk.Event) -> str:
        self.new_test()
        return "break"


def main() -> None:
    root = tk.Tk()
    TypingSpeedTester(root)
    root.mainloop()


if __name__ == "__main__":
    main()