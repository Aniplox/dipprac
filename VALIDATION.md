# Validation

Tested on 23 November 2026 on Apple Silicon (arm64), macOS 27.2, Python 3.13.2.
Libraries: NumPy 2.1.3, SciPy 1.14.1, Matplotlib 3.9.2, scikit-image 0.25.1,
and Pillow 10.4.0.

- All 15 programs completed and generated valid PNG figures.
- All reported worked-example and SciPy comparison checks passed.
- Huffman decoding reproduced the 8-bit grayscale pixels exactly.
- Arithmetic decoding reproduced the 16-level quantized pixels exactly.
- Custom image input, a filename containing spaces, and launching from another
  working directory passed.
- Invalid practical numbers and missing image paths give clear errors.
- The setup script successfully created a virtual environment using packages
  already present on this Mac; a fresh online package install was not tested.

The native Matplotlib GUI backend could not start in the automated session.
Mac scripts therefore use Agg to save the figure, then ask macOS to open the PNG.
Automatic image-viewer launching was blocked in this session; saved PNGs were
verified directly and can always be opened manually from `outputs/`.
