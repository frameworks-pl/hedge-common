from pathlib import Path
import shutil


SOURCE_DIR = Path(__file__).parent / "conan" / "profiles"
TARGET_DIR = Path.home() / ".conan2" / "profiles"

#print(f"Copying from {SOURCE_DIR} {TARGET_DIR}")

TARGET_DIR.mkdir(parents=True, exist_ok=True)

for profile_file in SOURCE_DIR.iterdir():
    msg = f"Copying {profile_file} to {TARGET_DIR}"
    try:
        shutil.copy2(profile_file, TARGET_DIR)
        msg += " OK"
    except Exception as e:
        msg += " FAILED"
    print(msg)