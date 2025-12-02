const inputFileToArray = async (inputPath: string): Promise<string[]> => {
  return (await Bun.file(inputPath).text()).split(",");
};

const identifyInvalidId = (input: number): boolean => {
  const s = input.toString();
  if (s.length % 2 !== 0) return false;

  const half = s.length / 2;
  return s.slice(0, half) === s.slice(half);
};

const identifyInvalidProducts = (input: string[]): number[] => {
  return input.flatMap((range) => {
    const [start, end] = range.split("-").map(Number);
    const ids: number[] = [];
    for (let i = start; i <= end; i++) if (identifyInvalidId(i)) ids.push(i);
    return ids;
  });
};

export default async function main(inputPath: string) {
  const productRangeIds = await inputFileToArray(inputPath);

  console.log("--- Day two input ---");
  console.log(productRangeIds);

  const invalidProducts = identifyInvalidProducts(productRangeIds);

  const sum = invalidProducts.reduce((acc, curr) => acc + curr, 0);

  console.log("--- Day two output ---");
  console.log(sum);

  return sum;
}

if (import.meta.main) {
  const inputPath = "input.txt";
  main(inputPath);
}
