import assert from 'assert';
import { Codification, Source } from '../core/base';
import { mapObject } from '../core/utils';
import Fraction from '../core/fraction';

export class Arithmetic implements Codification<Fraction> {
  constructor(source: Source) {
    this.source = source;

    let prev = Fraction.zero;
    this.cumulProb = mapObject(this.source.probabilities, (prob) => {
      const cumul = { low: prev, high: prev.add(prob) };
      prev = cumul.high;
      return cumul;
    });

    // this.cumulProb = {
    // 	'a': { low: Fraction.from(0.6), high: Fraction.from(1) },
    // 	'o': { low: Fraction.from(0.4), high: Fraction.from(0.6) },
    // 	'e': { low: Fraction.from(0.25), high: Fraction.from(0.4) },
    // 	'u': { low: Fraction.from(0.1), high: Fraction.from(0.25) },
    // 	'i': { low: Fraction.from(0), high: Fraction.from(0.1) },
    // }
  }
  private source: Source;
  private cumulProb: Record<string, { low: Fraction; high: Fraction }>;

  public encode(str: string): Fraction {
    let low = Fraction.zero;
    let high = Fraction.one;

    for (const symbol of str) {
      const range = high.subtract(low);
      const prob = this.cumulProb[symbol]!;

      high = low.add(prob.high.multiply(range));
      low = low.add(prob.low.multiply(range));
    }

    return low;
  }

  public decode(encoded: Fraction): string {
    let num = encoded;
    let decoded = '';

    while (!num.isZero) {
      for (const [symbol, { low, high }] of Object.entries(this.cumulProb)) {
        if (low.smallerOrEqual(num) && num.smaller(high)) {
          decoded += symbol;
          num = num.subtract(low).divide(high.subtract(low));
          break;
        }
      }
    }

    return decoded;
  }
}

if (require.main === module) {
  // const testStr = 'PABLOPABLITOCLAVOUNCLAVITO';
  const testStr = 'aeiouaaaeouaiaaoeoua';
  const testSource = Source.fromString(testStr);

  const test = (codification: Codification<any>, testStr: string) => {
    const encoded = codification.encode(testStr);
    console.log(
      `${codification.constructor.name}: ${encoded.valueOf()} (${
        encoded.length
      })`
    );

    assert.strictEqual(codification.decode(encoded), testStr);
  };

  console.log(`Original size: ${testStr.length * 8} bits`);

  test(new Arithmetic(testSource), testStr);
}
