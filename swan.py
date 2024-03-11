#!/usr/bin/env python3
import csv
import glob

def main():
	data = []

	for name in glob.glob('transfers-*.csv'):
		with open(name) as f:
			reader = csv.reader(f, delimiter=',', quotechar='"')
			for x, row in enumerate(reader):
				# skip header
				if x > 2:
					data.append(row)

	with open('koinly.csv', 'w') as f:
		writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		writer.writerow(['Event', 'Date', 'Timezone', 'Status', 'USD', 'Unit Count', 'Asset Type', 'BTC Price', 'Fee USD'])

		for i in data:
			event = i[0]
			date = i[1]
			timezone = i[2]
			status = i[3]
			unit = i[8]
			usd = i[5]
			asset = i[9]
			price = i[10]
			fee = i[7]

			row = [event, date, timezone, status, usd, unit, asset, price, fee]
			writer.writerow(row)

if __name__ == '__main__':
	main()