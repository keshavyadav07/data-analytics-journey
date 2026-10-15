"""Safely organize files in a folder by file type."""

import argparse
import os
import shutil
from pathlib import Path


CATEGORIES = {
    "Images": {".bmp", ".gif", ".heic", ".jpeg", ".jpg", ".png", ".svg", ".tif", ".tiff", ".webp"},
    "Videos": {".avi", ".m4v", ".mkv", ".mov", ".mp4", ".mpeg", ".mpg", ".webm"},
    "Audio": {".aac", ".flac", ".m4a", ".mp3", ".ogg", ".wav", ".wma"},
    "Documents": {".doc", ".docx", ".md", ".odt", ".pdf", ".rtf", ".txt"},
    "Spreadsheets": {".csv", ".ods", ".xls", ".xlsm", ".xlsx"},
    "Presentations": {".key", ".odp", ".ppt", ".pptx"},
    "Archives": {".7z", ".bz2", ".gz", ".rar", ".tar", ".xz", ".zip"},
    "Code": {".c", ".cpp", ".cs", ".css", ".html", ".java", ".js", ".json", ".py", ".sql", ".ts", ".xml"},
    "Fonts": {".otf", ".ttf", ".woff", ".woff2"},
}


def category_for(file_path: Path) -> str:
    """Return the folder category for a file based on its extension."""
    extension = file_path.suffix.lower()
    for category, extensions in CATEGORIES.items():
        if extension in extensions:
            return category
    return "Other"


def unique_destination(destination: Path) -> Path:
    """Choose an available path without overwriting an existing file."""
    if not os.path.lexists(destination):
        return destination

    suffix = destination.suffix
    filename = destination.stem
    parent = destination.parent
    counter = 1
    candidate = parent / f"{filename} ({counter}){suffix}"
    while os.path.lexists(candidate):
        counter += 1
        candidate = parent / f"{filename} ({counter}){suffix}"
    return candidate


def organize_files(folder: Path, apply_changes: bool = False) -> tuple[int, int]:
    """Preview or organize files directly inside folder; return (processed, failed)."""
    try:
        files = sorted(
            (item for item in folder.iterdir() if item.is_file()),
            key=lambda item: item.name.casefold(),
        )
    except OSError as error:
        print(f"Error: Could not read '{folder}': {error}")
        return 0, 1

    if not files:
        print(f"No files to organize in '{folder}'.")
        return 0, 0

    print("Organizing files" if apply_changes else "Preview (no files will be moved)")
    processed = 0
    failed = 0

    for source in files:
        category = category_for(source)
        destination_folder = folder / category
        destination = unique_destination(destination_folder / source.name)

        if not apply_changes:
            print(f"{source.name}  ->  {category}\\{destination.name}")
            processed += 1
            continue

        try:
            destination_folder.mkdir(exist_ok=True)
            destination = unique_destination(destination_folder / source.name)
            shutil.move(str(source), str(destination))
            print(f"Moved: {source.name}  ->  {category}\\{destination.name}")
            processed += 1
        except OSError as error:
            print(f"Error: Could not move '{source.name}': {error}")
            failed += 1

    action = "organized" if apply_changes else "ready to organize"
    print(f"\nSummary: {processed} file(s) {action}, {failed} error(s).")
    if not apply_changes:
        print("Run again with --apply to move these files.")
    return processed, failed


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Sort files in a folder into subfolders by file type."
    )
    parser.add_argument(
        "folder",
        nargs="?",
        type=Path,
        default=Path.cwd(),
        help="folder to organize (defaults to the current folder)",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="perform the moves; without this option, only show a preview",
    )
    args = parser.parse_args()

    folder = args.folder.expanduser()
    if not folder.is_dir():
        parser.error(f"'{folder}' is not a valid directory")

    _, failed = organize_files(folder, apply_changes=args.apply)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())