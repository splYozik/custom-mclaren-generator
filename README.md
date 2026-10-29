# custom-mclaren-generator

This is an experimental Python script a hybrid PRNG based on the MacLaren-Marsaglia method.
> ⚠️ **WARNING:** The generated numbers are **NOT** cryptographically secure.

- **def get_chaos_os** — used to generate a 32-bit integer from `os.urandom(4)` for random index
- **def get_lcg** — generates pseudo-random numbers and update the table
- **def main** — initializes the table, the dynamic mask, and outputs the numbers

## 🚀 How to run

You have Python 3.8+ installed (no extra packages needed!).

```bash
# 1. Clone this repositort
git clone https://github.com/splYozik/custom-mclaren-generator.git

# 2. Change directory
cd custom-mclaren-generator

# 3. Start
python main.py
```

## ⚠️ Security Limitations

Using Donald Knuth’s well-known constants allows an attacker to predict potential outcomes if they can reconstruct the generator's state. Furthermore, if the system is compromised by a RAM-based exploit (such as an out-of-bounds read or a Heartbleed-style vulnerability), the internal states and values can be directly retrieved from memory.
