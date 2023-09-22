
# Hash Cracker Python

**Hash Cracker Python** is a simple Python script designed to crack hashed passwords using various hashing algorithms. This script offers a user-friendly command-line interface and supports a range of popular hash types.

## Features

- Supports the following hash types:
  - blake2b
  - blake2s
  - md5
  - sha1
  - sha224
  - sha256
  - sha384
  - sha3_224
  - sha3_256
  - sha3_384
  - sha3_512
  - sha512
- Efficient password cracking using a provided wordlist.
- Progress tracking with the TQDM library.

## Usage

### Prerequisites

Before using **Hash Cracker Python**, ensure you have the following dependencies installed:

- Python 3.x
- TQDM (you can install it using `pip install tqdm`)

### Getting Started

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/TheODDYSEY/Hash-Cracker-Python.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Hash-Cracker-Python
   ```

3. Run the script with the following command:

   ```bash
   python hash_cracker.py [hash] [wordlist] [--hash-type hash_type]
   ```

   Replace `[hash]` with the hash you want to crack, `[wordlist]` with the path to your wordlist file, and `[hash_type]` (optional) with the desired hash type (default is `md5`).

### Example

To crack an MD5 hash using a wordlist:

```bash
python hash_cracker.py 5d41402abc4b2a76b9719d911017c592 wordlist.txt --hash-type md5
```

### Note

- Make sure your wordlist file contains one word per line.
- The script will display the cracked password if found.

## Contributing

If you would like to contribute to this project, please follow these guidelines:

1. Fork the repository.

2. Create a new branch for your feature or bug fix:

   ```bash
   git checkout -b feature-name
   ```

3. Make your changes and commit them:

   ```bash
   git commit -m "Your commit message"
   ```

4. Push your changes to your fork:

   ```bash
   git push origin feature-name
   ```

5. Create a pull request on the original repository, explaining your changes and why they should be merged.

Your contributions are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to customize this README further to provide additional details, usage examples, or any other information you believe would be useful for users and contributors.