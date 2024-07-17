export default function returnHowManyArguments(...input) {
    return { count: input.length, arguments: input };
  }
  