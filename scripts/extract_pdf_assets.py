import sys
from pathlib import Path

sys.path.insert(0, str(Path(".vendor").resolve()))

from pypdf import PdfReader


def main() -> None:
    pdf_path = Path("Steph Lifestyle Media Kit updatte.pdf")
    out_dir = Path("public/assets/extracted")
    out_dir.mkdir(parents=True, exist_ok=True)

    reader = PdfReader(str(pdf_path))
    count = 0

    for page_index, page in enumerate(reader.pages, start=1):
        for image_index, image_file in enumerate(page.images, start=1):
            suffix = Path(image_file.name).suffix or ".bin"
            file_name = f"page{page_index:02d}-img{image_index:02d}{suffix}"
            (out_dir / file_name).write_bytes(image_file.data)
            count += 1

    print(count)


if __name__ == "__main__":
    main()
