from PIL import Image
import os
import io


def compress_to_target_size(
    input_path, output_path, target_kb, min_quality=10, max_quality=95
):
    """
    Compress an image to a target size in KB.

    Parameters:
    - input_path: str - Original image path.
    - output_path: str - Final output path.
    - target_kb: int - Target size in kilobytes.
    - min_quality: int - Minimum JPEG quality to try.
    - max_quality: int - Maximum JPEG quality to try.
    """

    # Load and convert image
    img = Image.open(input_path)
    img = img.convert("RGB")

    target_bytes = target_kb * 1024
    best_quality = None
    best_image_data = None

    # Binary search for best quality
    while min_quality <= max_quality:
        mid_quality = (min_quality + max_quality) // 2
        buffer = io.BytesIO()
        img.save(buffer, format="JPEG", quality=mid_quality, optimize=True)
        size = buffer.tell()

        if size <= target_bytes:
            best_quality = mid_quality
            best_image_data = buffer.getvalue()
            min_quality = mid_quality + 1
        else:
            max_quality = mid_quality - 1

    if best_image_data:
        with open(output_path, "wb") as f:
            f.write(best_image_data)
        print(
            f"Compressed to {len(best_image_data) // 1024} KB using quality={best_quality}"
        )
    else:
        print("Couldn't compress to the target size.")


# Example usage
if __name__ == "__main__":
    compress_to_target_size(
        input_path="Pallete.png",
        output_path="compressed_800kb.jpg",
        target_kb=190,
    )
