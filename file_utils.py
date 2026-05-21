from pathlib import Path

def save_text_to_file(text, filename="output.txt"):
    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)

    file_path = output_dir / filename
    file_path.write_text(text, encoding="utf-8")

    return str(file_path)