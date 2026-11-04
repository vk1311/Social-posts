"""Scan every QR code on every page of a print PDF and list what each page opens.
Usage: python3 check_qr.py file.pdf [file2.pdf ...]   (needs pdftoppm, opencv-python, zxing-cpp)"""
import sys, subprocess, tempfile, glob, os, cv2, zxingcpp
for pdf in sys.argv[1:]:
    with tempfile.TemporaryDirectory() as t:
        subprocess.run(["pdftoppm", "-r", "200", "-png", pdf, os.path.join(t, "p")], check=True)
        for f in sorted(glob.glob(os.path.join(t, "p-*.png"))):
            im = cv2.imread(f)
            found = sorted(r.text for r in zxingcpp.read_barcodes(im))
            print(f"{os.path.basename(pdf)}\tp{int(f.rsplit('-',1)[1][:-4])}\t{len(found)}\t{' | '.join(sorted(set(found)))}")
