import { it, describe, expect } from "bun:test";
import main from "./solution";

describe("provided test input", () => {
  it("should ", async () => {
    const testInputPath = "test_input.txt";
    const expectedOutput = 1227775554;

    const result = await main(testInputPath);
    expect(result).toEqual(expectedOutput);
  });
});
