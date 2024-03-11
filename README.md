Swan Bitcoin Transaction Parser for [Koinly.io](https://koinly.io/?via=6BCBDC5B)
===

Swan Bitcoin updated their Deposits and Purchases CSV file which [Koinly](https://koinly.io/?via=6BCBDC5B) does not currently support.

Requirements
---

1. Python 3

Usage
---

1. Download your `Deposits and Purchases CSV` from Swan
1. Run `python3 swan.py`
1. Import `koinly.csv` into [Koinly](https://koinly.io/?via=6BCBDC5B)
1. Import your withdrawals CSV from Swan

Create separate wallets for each Swan account you have. If your Bitcoin balance does _not_ match between Koinly and Swan, go into your Fortress Trust transactions and manually fix a deposit from Prime Trust.

Caveats
---

- Purchasing fees do not appear to be calculated in Koinly so an excess USD balance is present.

Disclaimer
---

- I do _not_ guarentee the accuracy of the output CSV data and there could be bugs. Speak to a tax professional before filing!

License
---

MIT