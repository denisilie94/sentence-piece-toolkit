import hashlib


def calculate_sha256(file_path):
    """Calculate the SHA-256 checksum of a file."""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()


def check_checksums(checksum_file, root_dir):
    """Check the checksums of files listed in a checksum file."""
    with open(checksum_file, "r") as file:
        for line in file:
            expected_checksum, file_path = line.strip().split()
            file_path = root_dir + file_path
            actual_checksum = calculate_sha256(file_path)

            if actual_checksum == expected_checksum:
                print(f"Checksum OK for {file_path}")
            else:
                print(f"Checksum MISMATCH for {file_path}. Expected: {expected_checksum}, Actual: {actual_checksum}")


root_dir = './data/cultura-x/'
checksum_file = root_dir + "ro_checksum.sha256"
check_checksums(checksum_file, root_dir)
