import sys
import time
import shutil
import signal

running = True
alt_screen = False
cursor_hidden = False

LOCKOUT_DELAY = 0.35
MAGIC_LINE_DELAY = 0.1

BG_BLUE = "\x1b[44m"
FG_WHITE = "\x1b[97m"
RESET = "\x1b[0m"

PROMPTS = 3
LOCK_LINE = "YOU DIDN'T SAY THE MAGIC WORD!"

IS_WINDOWS = sys.platform.startswith("win")

if IS_WINDOWS:
    import msvcrt
else:
    import termios
    import tty
    import select


def write(s: str) -> None:
    sys.stdout.write(s)
    sys.stdout.flush()


def esc(code: str) -> str:
    return f"\x1b[{code}"


def enter_alt_screen() -> None:
    global alt_screen
    write(esc("?1049h"))
    alt_screen = True


def leave_alt_screen() -> None:
    global alt_screen
    if alt_screen:
        write(esc("?1049l"))
        alt_screen = False


def hide_cursor() -> None:
    global cursor_hidden
    write(esc("?25l"))
    cursor_hidden = True


def show_cursor() -> None:
    global cursor_hidden
    if cursor_hidden:
        write(esc("?25h"))
        cursor_hidden = False


def clear_screen() -> None:
    write(esc("2J") + esc("H"))


def move(row: int, col: int) -> None:
    write(esc(f"{row};{col}H"))


def set_scroll_region(top: int, bottom: int) -> None:
    write(esc(f"{top};{bottom}r"))


def reset_scroll_region() -> None:
    write(esc("r"))


def cleanup() -> None:
    write(RESET)
    reset_scroll_region()
    show_cursor()
    leave_alt_screen()


def signal_handler(sig, frame) -> None:
    global running
    running = False


def blue_fill_line(row: int, cols: int) -> None:
    move(row, 1)
    write(BG_BLUE + (" " * cols) + RESET)


def blue_text_line(row: int, text: str, cols: int, left: int = 1) -> None:
    usable = max(1, cols - left + 1)
    painted = text[:usable].ljust(usable)

    move(row, left)
    write(BG_BLUE + (" " * usable) + RESET)
    move(row, left)
    write(BG_BLUE + FG_WHITE + painted + RESET)


def fill_blue_background() -> None:
    size = shutil.get_terminal_size(fallback=(80, 24))
    cols = max(20, size.columns)
    rows = max(8, size.lines)

    clear_screen()
    for y in range(1, rows + 1):
        blue_fill_line(y, cols)

    move(1, 1)


class RawInput:
    def __enter__(self):
        if not IS_WINDOWS:
            self.fd = sys.stdin.fileno()
            self.old = termios.tcgetattr(self.fd)

            tty.setcbreak(self.fd)

            new = termios.tcgetattr(self.fd)
            new[3] = new[3] & ~(termios.ECHO)
            termios.tcsetattr(self.fd, termios.TCSADRAIN, new)
        return self

    def __exit__(self, exc_type, exc, tb):
        if not IS_WINDOWS:
            termios.tcsetattr(self.fd, termios.TCSADRAIN, self.old)


def get_key_nonblocking():
    if IS_WINDOWS:
        if not msvcrt.kbhit():
            return None

        ch = msvcrt.getwch()

        if ch in ("\x00", "\xe0"):
            if msvcrt.kbhit():
                msvcrt.getwch()
            return None

        return ch

    rlist, _, _ = select.select([sys.stdin], [], [], 0)
    if not rlist:
        return None

    return sys.stdin.read(1)


def read_user_line(row: int, cols: int, left: int = 2) -> str:
    buf = []
    usable = max(1, cols - left + 1)

    cursor_on = True
    last_blink = time.monotonic()
    blink_interval = 0.45

    while running:
        now = time.monotonic()
        if now - last_blink >= blink_interval:
            cursor_on = not cursor_on
            last_blink = now

        prefix = "> "
        current = "".join(buf)
        cursor = "_" if cursor_on else " "
        painted = (prefix + current + cursor)[:usable].ljust(usable)

        move(row, left)
        write(BG_BLUE + FG_WHITE + painted + RESET)

        ch = get_key_nonblocking()
        if ch is None:
            time.sleep(0.02)
            continue

        if ch == "\x03":
            raise KeyboardInterrupt

        if ch in ("\r", "\n"):
            move(row, left)
            final = (prefix + current)[:usable].ljust(usable)
            write(BG_BLUE + FG_WHITE + final + RESET)
            return current

        if ch in ("\x08", "\x7f"):
            if buf:
                buf.pop()
            continue

        if ch.isprintable():
            buf.append(ch)

    return "".join(buf)


def draw_input_phase() -> int:
    fill_blue_background()

    size = shutil.get_terminal_size(fallback=(80, 24))
    cols = max(20, size.columns)

    left = 2
    row = 1

    blue_text_line(row, "Jurassic Park, System Security Interface", cols, left)
    row += 1

    blue_text_line(row, "Version 4.0.5, Alpha E", cols, left)
    row += 1

    blue_text_line(row, "Ready...", cols, left)
    row += 2

    for i in range(PROMPTS):
        if not running:
            return row

        _user_input = read_user_line(row, cols, left)
        row += 1

        if i == PROMPTS - 1:
            response = "access: PERMISSION DENIED....And..."
        else:
            response = "access: PERMISSION DENIED."

        blue_text_line(row, response, cols, left)
        row += 2

    return row


def print_magic_line(row: int, cols: int, left: int = 1) -> None:
    usable = max(10, cols - left + 1)
    text = LOCK_LINE[:usable].ljust(usable)

    move(row, left)
    write(BG_BLUE + (" " * usable) + RESET)
    move(row, left)
    write(BG_BLUE + FG_WHITE + text + RESET)


def draw_wall_phase(start_row: int) -> None:
    size = shutil.get_terminal_size(fallback=(80, 24))
    cols = max(20, size.columns)
    rows = max(8, size.lines)

    top = max(1, start_row)
    bottom = rows
    current_row = top

    set_scroll_region(top, bottom)

    while running:
        size = shutil.get_terminal_size(fallback=(80, 24))
        cols = max(20, size.columns)
        rows = max(8, size.lines)
        bottom = rows

        set_scroll_region(top, bottom)

        if current_row <= bottom:
            print_magic_line(current_row, cols, 1)
            current_row += 1
        else:
            move(bottom, 1)
            write("\n")
            print_magic_line(bottom, cols, 1)

        time.sleep(MAGIC_LINE_DELAY)


def main() -> None:
    global running

    signal.signal(signal.SIGINT, signal_handler)

    try:
        enter_alt_screen()
        hide_cursor()

        with RawInput():
            start_row = draw_input_phase()

            if running:
                time.sleep(LOCKOUT_DELAY)

            if running:
                draw_wall_phase(start_row)

    finally:
        cleanup()


if __name__ == "__main__":
    main()