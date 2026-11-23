# Digital Image Processing Practicals



## Run on Mac

Use Python 3.11–3.13. Open Terminal in this folder, then run:

```bash
bash setup.sh
.venv/bin/python run.py
```

Choose a practical number from **1–15**. A figure is saved to `outputs/` and
opens in your default image viewer on Mac (usually Preview). The menu remains
available while you view the image. Choose `all` to
generate every figure without opening 15 windows, or `q` to quit.

If the required packages are already installed, you can immediately use:

```bash
python3 run.py
```

On Mac, you can also run `bash Run_Practicals.command`. To enable double-click
launching after a ZIP download, run `chmod +x Run_Practicals.command` once.

## Run individual programs

```bash
.venv/bin/python 01_mean_filter.py
.venv/bin/python run.py 6
.venv/bin/python run.py all
.venv/bin/python 14_huffman_coding.py --no-show
```

Each program uses scikit-image's bundled astronaut image by default. No image
download or file-path editing is needed once dependencies are installed.
To use your own JPG or PNG (quote paths with spaces):

```bash
.venv/bin/python 01_mean_filter.py --image "/path/to/photo.jpg"
.venv/bin/python run.py 4 --image "/path/to/photo.jpg"
```

`--no-show` saves the plot without opening a GUI window. Output paths are relative
to the program folder, so launching from another working directory also works.
Rerunning one program replaces only that program's own PNG.

## Program list

| No. | Program | File |
| --- | --- | --- |
| 1 | Mean filter | `01_mean_filter.py` |
| 2 | Weighted average filter | `02_weighted_average_filter.py` |
| 3 | Gaussian spatial filter | `03_gaussian_filter.py` |
| 4 | Median filter | `04_median_filter.py` |
| 5 | Laplacian sharpening | `05_laplacian_filter.py` |
| 6 | Sobel edge detection | `06_sobel_filter.py` |
| 7 | High-boost sharpening | `07_high_boost_filter.py` |
| 8 | Ideal low-pass filter | `08_ideal_low_pass_filter.py` |
| 9 | Butterworth low-pass filter | `09_butterworth_low_pass_filter.py` |
| 10 | Gaussian low-pass filter | `10_gaussian_low_pass_filter.py` |
| 11 | Ideal high-pass filter | `11_ideal_high_pass_filter.py` |
| 12 | Butterworth high-pass filter | `12_butterworth_high_pass_filter.py` |
| 13 | Gaussian high-pass filter | `13_gaussian_high_pass_filter.py` |
| 14 | Huffman coding | `14_huffman_coding.py` |
| 15 | Arithmetic coding | `15_arithmetic_coding.py` |

The spatial and frequency filters operate on the HSI intensity channel.
Huffman coding uses 8-bit grayscale. Arithmetic coding first quantizes grayscale
to 16 levels: decoding is lossless relative to that quantized image, not the
original 8-bit image. Compression numbers exclude model/header overhead;
the arithmetic bit count is an estimate, not a serialized compressed file size.

## Dependencies and troubleshooting

NumPy, SciPy, Matplotlib, scikit-image, and Pillow. `setup.sh` makes a local
virtual environment and reuses installed packages if available. Otherwise it
installs `requirements.txt` and needs internet access. For a fresh isolated setup:

```bash
python3 -m venv .venv-clean
.venv-clean/bin/python -m pip install -r requirements.txt
.venv-clean/bin/python run.py
```

If a plot window cannot open, use `--no-show`, then open its PNG in `outputs/`.
On Mac the scripts use Matplotlib's Agg renderer and open the saved image,
avoiding dependency on a native Matplotlib GUI backend.
Keep `lab_support.py` alongside the numbered programs. The upstream references
to PDF page numbers are retained; that PDF is not included in the source repository.
